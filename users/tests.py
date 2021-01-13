from django.test import TestCase
from .models import User

# Create your tests here.

class UserModelTest(TestCase):

  @classmethod
  def setUpTestData(cls):
    User.objects.create(pk='7ab75ccc-a705-4813-9b20-4262bf338021', first_name='Samuel', last_name='Torimiro', email='efosonaname@gmail.com', phone_number='08149110574', address_line_1='Obafemi Awolowo University', city='ile-ife', zip_code=12000, state='Osun')


  def test_first_name_content(self):
    user = User.objects.get(pk='7ab75ccc-a705-4813-9b20-4262bf338021')
    expected_object_name = f'{user.first_name}'
    self.assertEqual(expected_object_name, 'Samuel')

  def test_last_name_content(self):
    user = User.objects.get(pk='7ab75ccc-a705-4813-9b20-4262bf338021')
    expected_object_name = f'{user.last_name}'
    self.assertEqual(expected_object_name, 'Torimiro')

  def test_email_content(self):
    user = User.objects.get(pk='7ab75ccc-a705-4813-9b20-4262bf338021')
    expected_object_name = f'{user.email}'
    self.assertEqual(expected_object_name, 'efosonaname@gmail.com')

  def test_phone_number_content(self):
    user = User.objects.get(pk='7ab75ccc-a705-4813-9b20-4262bf338021')
    expected_object_name = f'{user.phone_number}'
    self.assertEqual(expected_object_name, '08149110574')

  def test_address_line_1_content(self):
    user = User.objects.get(pk='7ab75ccc-a705-4813-9b20-4262bf338021')
    expected_object_name = f'{user.address_line_1}'
    self.assertEqual(expected_object_name, 'Obafemi Awolowo University')

  def test_city_content(self):
    user = User.objects.get(pk='7ab75ccc-a705-4813-9b20-4262bf338021')
    expected_object_name = f'{user.city}'
    self.assertEqual(expected_object_name, 'ile-ife')

  def test_zip_code_content(self):
    user = User.objects.get(pk='7ab75ccc-a705-4813-9b20-4262bf338021')
    expected_object_name = f'{user.zip_code}'
    self.assertEqual(expected_object_name, '12000')

  def test_state_content(self):
    user = User.objects.get(pk='7ab75ccc-a705-4813-9b20-4262bf338021')
    expected_object_name = f'{user.state}'
    self.assertEqual(expected_object_name, 'Osun')