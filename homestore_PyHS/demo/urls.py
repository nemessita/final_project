from django.urls import path
from . import views
from demo import views

urlpatterns = [
    path('',views.base,name="base")
]
