from django.conf import settings
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from services.open_meteo import third_party_request
from utility.area_data import process_area_data
from utility.logger import get_logger

CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)

logger = get_logger(__name__)


def process_batch_area_data():
    try:
        dataset = process_area_data()
        forecasted_data = {area["name"]: third_party_request(lat=area["lat"], long=area["long"]) for area in dataset["districts"]}
        cache.set("forecasted_data", forecasted_data, timeout=CACHE_TTL)

    except Exception as e:
        logger.debug(repr(e))
        return None

