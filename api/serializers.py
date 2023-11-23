from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from rest_framework import serializers

from utility.data_parser import parse_forecasted_dates
from utility.logger import get_logger
from utility.area_data import process_district_data
from Weather_forecast import settings

logger = get_logger(__name__)
CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)
DISTRICT_DATA = process_district_data()


class TravelDeciderSerializer(serializers.Serializer):
    current_location = serializers.CharField(max_length=20)
    destination = serializers.CharField(max_length=20)
    date_of_travel = serializers.DateField(format="%Y-%m-%d")

    @staticmethod
    def validate_current_location(current_location):
        if current_location.title() not in DISTRICT_DATA:
            raise serializers.ValidationError("The provided current location is invalid")
        return current_location.title()

    @staticmethod
    def validate_destination(destination):
        if destination.title() not in DISTRICT_DATA:
            raise serializers.ValidationError("The provided destination is invalid")
        return destination.title()

    @staticmethod
    def validate_date_of_travel(date_of_travel):
        forecasted_dates = parse_forecasted_dates(cache.get("forecasted_data"))
        if date_of_travel not in forecasted_dates:
            raise serializers.ValidationError("Date of travel should be in between forecasted dates")


