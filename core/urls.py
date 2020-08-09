from django.urls import path, include
from . import views
app_name = 'core'

urlpatterns = [
    path('', views.ContactsListView.as_view(), name='contacts'),
    path('contact/<int:client_id>/', views.ContactDetailView.as_view(), name='detail'),
    path('contact', views.ClientSearchView.as_view(), name='search_contact')
]