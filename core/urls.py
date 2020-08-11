from django.urls import path, include
#views
from . import views

#application namespace
app_name = 'core'

#urls root
urlpatterns = [
    path('', views.ContactsListView.as_view(), name='contacts_list'),#contact listing view
    path('contact/<int:client_id>/', views.ContactDetailView.as_view(), name='detail'),#contact detail view
    path('contact', views.ClientSearchView.as_view(), name='search_contact'),#client searching view
]