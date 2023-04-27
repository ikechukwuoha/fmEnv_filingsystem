from django.urls import path
from users import views as _


app_name = "users"


urlpatterns = [path("", _.landingPage, name="landingPage")]
