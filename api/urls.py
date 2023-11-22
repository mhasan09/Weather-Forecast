from django.urls import path

from api.views import GetCoolestDistrictsAPIView

urlpatterns = [

    path("v1/get-coolest-districts/", GetCoolestDistrictsAPIView.as_view(), name="coolest-districts"),
]


