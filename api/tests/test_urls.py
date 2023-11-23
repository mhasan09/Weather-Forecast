from django.urls import resolve

from api.tests.test_setup import TestWeatherForecastSetup
from api.views import GetCoolestDistrictsAPIView, TravelDeciderAPIView


class TestWeatherForecastAPIViewUrl(TestWeatherForecastSetup):
    def test_coolest_districts_url_name_match(self):
        self.assertEqual(resolve(self.coolest_districts_url).url_name, 'coolest-districts')

    def test_coolest_districts_apiview_match(self):
        self.assertEqual(resolve(self.coolest_districts_url).func.view_class, GetCoolestDistrictsAPIView)


class TestTravelDeciderAPIViewUrl(TestWeatherForecastSetup):
    def test_travel_decider_url_name_match(self):
        self.assertEqual(resolve(self.travel_decider_url).url_name, 'travel-decider')

    def test_travel_decider_apiview_match(self):
        self.assertEqual(resolve(self.travel_decider_url).func.view_class, TravelDeciderAPIView)

