from django.urls import path, include
from . import views
app_name = 'core'

urlpatterns = [
    path('', views.TestView.as_view(), name='test')
]