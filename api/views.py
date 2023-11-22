from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from services.batch_processing import process_batch_area_data
from utility.data_parser import parse_forecasted_data
from utility.logger import get_logger

logger = get_logger(__name__)


class GetCoolestDistrictsAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        forecasted_data = cache.get("forecasted_data", None)
        parsed_data = parse_forecasted_data(forecasted_data)
        if forecasted_data is None:
            forecasted_data = process_batch_area_data()
            parsed_data = parse_forecasted_data(forecasted_data)
        return Response(status=200, data=parsed_data)
