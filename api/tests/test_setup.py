from django.urls import reverse
from rest_framework.test import APITestCase


class TestWeatherForecastSetup(APITestCase):
    def setUp(self):
        self.coolest_districts_url = reverse("coolest-districts")
        self.travel_decider_url = reverse("travel-decider")


def tearDown(self):
    return super(TestWeatherForecastSetup, self).tearDown()
