from django.core.cache import cache
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from rest_framework.views import APIView

from api.serializers import TravelDeciderSerializer
from services.batch_processing import process_batch_area_data
from utility.data_parser import parse_forecasted_data, parse_travel_decision_data
from utility.logger import get_logger
from utility.response_time_decorator import calculate_response_time

logger = get_logger(__name__)


@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(require_http_methods(["GET"]), name='dispatch')
class GetCoolestDistrictsAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    @calculate_response_time
    def get(self, request):
        forecasted_data = cache.get("forecasted_data", None)

        if forecasted_data is None:
            forecasted_data = process_batch_area_data()
            parsed_data = parse_forecasted_data(forecasted_data)
        else:
            parsed_data = parse_forecasted_data(forecasted_data)

        return JsonResponse(parsed_data)


@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(require_http_methods(["POST"]), name='dispatch')
class TravelDeciderAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    @calculate_response_time
    def post(self, request):
        requested_data = request.data
        serializer = TravelDeciderSerializer(data=requested_data)
        serializer.is_valid(raise_exception=True)

        forecasted_data = cache.get("forecasted_data", None)
        if forecasted_data is None:
            forecasted_data = process_batch_area_data()
            parsed_data = parse_travel_decision_data(
                forecasted_data=forecasted_data,
                requested_data=requested_data,
            )
        else:
            parsed_data = parse_travel_decision_data(
                forecasted_data=forecasted_data,
                requested_data=requested_data,
            )

        return JsonResponse({"Decision": parsed_data})
