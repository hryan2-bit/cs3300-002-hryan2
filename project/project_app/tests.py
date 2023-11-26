from django.test import TestCase
from django.test import SimpleTestCase
from django.test import LiveServerTestCase
from django.test import Client
from django.urls import reverse
from .models import *

from selenium import webdriver


# Create your tests here.

# Selenium Tests
driver=webdriver.Chrome()


# Unit tests
class KillerUnitTests(TestCase):
    @classmethod
    #Killer
    def setUpTestData(cls):
        cls.test_killer = Killer.objects.create(title='Test', description='Test descrip')

    @classmethod
    def test_title_content(self):
        killer = Killer.objects.get(id=self.test_killer.id)
        self.assertEqual(killer.title, 'Test')

    @classmethod
    def test_description_content(self):
        killer = Killer.objects.get(id=self.test_killer.id)
        self.assertEqual(killer.description, 'Test descrip')

class AppUserUnitTest(TestCase):
    @classmethod
    #AppUser
    def setUpTestData(cls):
        cls.test_user = AppUser.objects.create(name='Test')

    @classmethod
    def test_title_content(self):
        user = AppUser.objects.get(id=self.test_user.id)
        self.assertEqual(user.name, 'Test')

class PerkUnitTests(TestCase):
    @classmethod
    #Perks
    def setUpTestData(cls):
        cls.test_perks = Perks.objects.create(title='Test', description='Test descrip')

    @classmethod
    def test_title_content(self):
        perk = Perks.objects.get(id=self.test_perks.id)
        self.assertEqual(perk.title, 'Test')

    @classmethod
    def test_description_content(self):
        perk = Perks.objects.get(id=self.test_perks.id)
        self.assertEqual(perk.description, 'Test descrip')
    
