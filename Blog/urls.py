from django.urls import path
from Blog import views

app_name = "Blog"

urlpatterns = [
    path('', views.index, name="home"),
    path('result', views.result, name="result"),
]