from django.core.cache import cache
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from rest_framework.views import APIView
from services.batch_processing import process_batch_area_data
from utility.data_parser import parse_forecasted_data
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
        parsed_data = parse_forecasted_data(forecasted_data)
        if forecasted_data is None:
            forecasted_data = process_batch_area_data()
            parsed_data = parse_forecasted_data(forecasted_data)
        return JsonResponse(parsed_data)


