from django.test import TestCase
from apps.main.models import Platform,Technology


class TestPlatform(TestCase):
	def setUp(self):
		Platform.objects.create(name='test', status='testing')

	def test_platform_creation(self):

		"""Testing an instance of a Platform model created.
		Instance should return the data of a name attribute as 
		the '__str__' of the model, class Project.
		"""
		obj = Platform.objects.get(id=1)

		self.assertTrue(isinstance(obj, Platform)) 
		self.assertEqual(obj.__str__(), 'test')

	def test_not_platform(self):

		"""Testing if not an instance of a Platform model.
		"""
		obj = Technology.objects.create(name='testing-tech')

		self.assertFalse(isinstance(obj, Platform))
		self.assertNotEqual(obj.__str__(), 'test')

	def test_data_for_instance_of_platform_model(self):
		"""
		Testing an instance data is correct
		"""
		ins = Platform.objects.get(id=1)
		self.assertEqual(ins.status, 'testing')

	def test_data_not_for_instance_of_platform_model(self):
		"""
		Testing an instance data is not correct
		"""
		ins = Platform.objects.get(id=1)
		self.assertNotEqual(ins.status, 'This is not your data')


class TestTechnology(TestCase):
	def setUp(self):
		Technology.objects.create(name='test-tech')

	def test_technology_creation(self):

		"""Testing an instance of a Technology model created.
		Instance should return the data of a name attribute as 
		the '__str__' of the model, class Project.
		"""
		obj = Technology.objects.get(id=1)

		self.assertTrue(isinstance(obj, Technology)) 
		self.assertEqual(obj.__str__(), 'test-tech')

	def test_not_technology(self):

		"""Testing if not an instance of a Technology model.
		"""
		obj = Platform.objects.create(name='testing-platform')

		self.assertFalse(isinstance(obj, Technology))
		self.assertNotEqual(obj.__str__(), 'test-tech')

	def test_data_for_instance_of_tech_model(self):
		"""
		Testing an instance data is correct
		"""
		ins = Technology.objects.get(id=1)
		self.assertEqual(ins.name, 'test-tech')

	def test_data_not_for_instance_of_tech_model(self):
		"""
		Testing an instance data is not correct
		"""
		ins = Technology.objects.get(id=1)
		self.assertNotEqual(ins.name, 'This is not your data')