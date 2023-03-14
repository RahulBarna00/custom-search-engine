from django.urls import path
from .views import *

app_name = "searchEngineApp"

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('crawler',crawler, name='crawler'),
    path('validate',validate,name='validate')
]