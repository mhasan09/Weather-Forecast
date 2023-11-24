from django.urls import reverse
from rest_framework.test import APITestCase
from django.core.cache import cache

from utility.data_parser import parse_forecasted_dates


class TestWeatherForecastSetup(APITestCase):
    def setUp(self):
        self.forecasted_data = cache.get("forecasted_data", None)
        self.forecasted_dates = parse_forecasted_dates(self.forecasted_data)
        self.coolest_districts_url = reverse("coolest-districts")
        self.travel_decider_url = reverse("travel-decider")

        self.travel_decider_payload = {
            "current_location": "Chattogram",
            "destination": "sylhet",
            "date_of_travel": "2023-11-25"
        }


def tearDown(self):
    return super(TestWeatherForecastSetup, self).tearDown()
