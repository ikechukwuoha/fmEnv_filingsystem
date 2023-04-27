from django.urls import path
from docsmgt import views as mgt_views


app_name = "docsmgt"


urlpatterns = [path("docsmgt/", mgt_views.mgtSystems, name="landingPage")]
