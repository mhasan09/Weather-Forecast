import time
from django.http import JsonResponse


def calculate_response_time(view_func):
    def wrapper(request, *args, **kwargs):
        start_time = time.time()
        response = view_func(request, *args, **kwargs)
        duration = time.time() - start_time
        response["X-Elapsed-Time"] = str(duration)
        if duration > 0.5:  # 500 milliseconds
            return JsonResponse({"message": "Response time has exceeded 500 ms. No response."})

        return response

    return wrapper
