from django.urls import path
from api import views as api_view


app_name = "api"


urlpatterns = [path("api", api_view.apI, name="landingPage")]
