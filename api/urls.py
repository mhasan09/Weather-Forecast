from django.urls import path

from api.views import GetCoolestDistrictsAPIView, TravelDeciderAPIView

urlpatterns = [

    path("v1/get-coolest-districts/", GetCoolestDistrictsAPIView.as_view(), name="coolest-districts"),
    path("v1/travel-decider/", TravelDeciderAPIView.as_view(), name="travel-decider"),
]


