import openmeteo_requests
import pandas as pd
from Weather_forecast import settings
from utility.logger import get_logger

logger = get_logger(__name__)


def third_party_request(lat, long):
    try:
        client = openmeteo_requests.Client()
        params = {
            "latitude": lat,
            "longitude": long,
            "hourly": "temperature_2m",
            "timezone": "Asia/Dhaka",
        }
        responses = client.weather_api(settings.FORECAST_URL, params=params)
        if responses is None:
            return None

        response = responses[0]
        logger.debug(f"Coordinates {response.Latitude()}°E {response.Longitude()}°N")
        logger.debug(f"Elevation {response.Elevation()} m asl")
        logger.debug(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
        logger.debug(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        hourly_data = {"date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s"),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s"),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        )}
        logger.debug({"hourly_data": hourly_data})
        hourly_data["temperature_2m"] = hourly_temperature_2m
        return hourly_data

    except Exception as e:
        logger.error({"exception_errors": repr(e)})
        return None


"""
            required_time_index = []
            for i in range(len(hourly_data["date"])):
                if hourly_data["date"].time[20].hour == 14:
                    required_time_index.append(i)

            logger.debug({"required_time_index": required_time_index})

            sum_of_temperature = 0
            for i in required_time_index:
                sum_of_temperature += hourly_data["temperature_2m"][i]

            average_temp = sum_of_temperature / 7
            logger.debug({"average_temp": average_temp})
"""
