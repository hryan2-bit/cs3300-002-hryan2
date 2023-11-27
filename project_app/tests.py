from django.test import TestCase
from django.test import SimpleTestCase
from django.test import LiveServerTestCase
from django.test import Client
from django.urls import reverse
from .models import *

from selenium import webdriver
from selenium.webdriver.common.by import By


# Create your tests here.

# Unit tests
class KillerUnitTests(TestCase):
    @classmethod
    #Killer
    def setUpTestData(cls):
        cls.test_killer = Killer.objects.create(title='Test', description='Test descrip')

    def test_title_content(self):
        killer = Killer.objects.get(id=self.test_killer.id)
        self.assertEqual(killer.title, 'Test')

    def test_description_content(self):
        killer = Killer.objects.get(id=self.test_killer.id)
        self.assertEqual(killer.description, 'Test descrip')

class AppUserUnitTest(TestCase):
    @classmethod
    #AppUser
    def setUpTestData(cls):
        cls.test_user = AppUser.objects.create(name='Test')

    def test_title_content(self):
        user = AppUser.objects.get(id=self.test_user.id)
        self.assertEqual(user.name, 'Test')

class PerkUnitTests(TestCase):
    @classmethod
    #Perks
    def setUpTestData(cls):
        cls.test_perks = Perks.objects.create(title='Test', description='Test descrip')

    def test_title_content(self):
        perk = Perks.objects.get(id=self.test_perks.id)
        self.assertEqual(perk.title, 'Test')

    def test_description_content(self):
        perk = Perks.objects.get(id=self.test_perks.id)
        self.assertEqual(perk.description, 'Test descrip')
    
# Selenium Tests
class SeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(SeleniumTests, cls).setUpClass()
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        super(SeleniumTests, self).tearDownClass()
    
    def test_register(self):
        self.driver.get("http://127.0.0.1:8000/accounts/register/")
        self.driver.find_element(By.NAME, "username").send_keys("test1")
        self.driver.find_element(By.NAME, "email").send_keys("test1@123.123")
        self.driver.find_element(By.NAME, "password1").send_keys("omenxiii2")
        self.driver.find_element(By.NAME, "password2").send_keys("omenxiii2")
        self.driver.find_element(By.NAME, "Create User").click()

    def test_login(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element(By.NAME, "username").send_keys("test1")
        self.driver.find_element(By.NAME, "password").send_keys("omenxiii2")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='login']").click()
    
