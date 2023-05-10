from django.urls import path
from bar_codes import views as _


app_name = "bar_codes"


urlpatterns = [
    path("codes/", _.codes, name="codes"),
]
