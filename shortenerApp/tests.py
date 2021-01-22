from django.test import TestCase

# Create your tests here.
from shortenerApp.models import Urls

urls = {
    "Digikala": "https://www.digikala.com/",
    "DigiPay": "https://www.mydigipay.com/"
}


class AnimalTestCase(Urls):
    def setUp(self):
        Urls.objects.create(url=urls["Digikala"])
        Urls.objects.create(url=urls["DigiPay"])

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Urls.objects.get(url=urls["Digikala"])
        cat = Urls.objects.get(url=urls["DigiPay"])
        self.assertEqual(lion.speak(), urls["Digikala"])
        self.assertEqual(cat.speak(), urls["DigiPay"])
