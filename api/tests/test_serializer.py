from api.serializers import TravelDeciderSerializer
from api.tests.test_setup import TestWeatherForecastSetup


class TestTravelDeciderSerializerSerializer(TestWeatherForecastSetup):
    def test_travel_decider_serializer_validation_success(self):
        serializer = TravelDeciderSerializer(data=self.travel_decider_payload)
        self.assertTrue(serializer.is_valid())

    def test_current_location_validation_max_length_fail(self):
        self.travel_decider_payload.update({
            "current_location": "ChattogramChattogramChattogram "
        })
        serializer = TravelDeciderSerializer(data=self.travel_decider_payload)
        if not serializer.is_valid():
            error_response = {**serializer.errors}
            self.assertEqual(error_response["current_location"][0].title(),
                             "Ensure This Field Has No More Than 20 Characters.")
        self.assertFalse(serializer.is_valid())

    def test_destination_validation_max_length_fail(self):
        self.travel_decider_payload.update({
            "destination": "ChattogramChattogramChattogram "
        })
        serializer = TravelDeciderSerializer(data=self.travel_decider_payload)
        if not serializer.is_valid():
            error_response = {**serializer.errors}
            self.assertEqual(error_response["destination"][0].title(),
                             "Ensure This Field Has No More Than 20 Characters.")
        self.assertFalse(serializer.is_valid())

    def test_current_location_validation_not_found_fail(self):
        self.travel_decider_payload.update({
            "current_location": "Chittagong"
        })
        serializer = TravelDeciderSerializer(data=self.travel_decider_payload)
        if not serializer.is_valid():
            error_response = {**serializer.errors}
            self.assertEqual(error_response["current_location"][0].title(),
                             "The Provided Current Location Is Invalid")
        self.assertFalse(serializer.is_valid())

    def test_destination_validation_not_found_fail(self):
        self.travel_decider_payload.update({
            "destination": "Mumbai "
        })
        serializer = TravelDeciderSerializer(data=self.travel_decider_payload)
        if not serializer.is_valid():
            error_response = {**serializer.errors}
            self.assertEqual(error_response["destination"][0].title(),
                             "The Provided Destination Is Invalid")
        self.assertFalse(serializer.is_valid())

    def test_date_validation_failed(self):
        self.travel_decider_payload.update({
            "date_of_travel": "2024-11-11"
        })
        serializer = TravelDeciderSerializer(data=self.travel_decider_payload)
        if not serializer.is_valid():
            error_response = {**serializer.errors}
            self.assertEqual(error_response["date_of_travel"][0].title(),
                             "Date Of Travel Should Be In Between Forecasted Dates")
        self.assertFalse(serializer.is_valid())