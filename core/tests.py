from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class ContactsListViewTest(TestCase):

    #test de contacts list page with authentification)
    def test_contacts_list_page_unauthorized_return_401(self):
        #get request to the contacts list page
        response = self.client.get(reverse('core:contacts_list'))
        #test by comparing the get response status code with the expected one
        self.assertEqual(response.status_code, 401)


