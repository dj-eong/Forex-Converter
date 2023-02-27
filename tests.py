from unittest import TestCase
from app import app
from flask import flash
from converter import get_currency_codes, are_valid_inputs, get_converted_amount

app.config['TESTING'] = True


class Tests(TestCase):

    def test_get_currency_codes(self):
        currency_codes = get_currency_codes()
        self.assertIn('USD', currency_codes)
        self.assertIn('KRW', currency_codes)
        self.assertNotIn('ZZZ', currency_codes)

    def test_are_valid_inputs(self):
        self.assertTrue(are_valid_inputs('USD', 'EUR', '1'))
        self.assertTrue(are_valid_inputs('KRW', 'ZWL', '3.1415926'))
        self.assertFalse(are_valid_inputs('US D', 'EUR', '1'))
        self.assertFalse(are_valid_inputs('USD', 'EUR', '-1'))
        self.assertFalse(are_valid_inputs('', '', ''))

    def test_get_converted_amount(self):
        self.assertEqual(get_converted_amount(
            'USD', 'USD', '100'), '$100')
        self.assertIn('$', get_converted_amount(
            'ZWL', 'USD', '1'))
        self.assertEqual(get_converted_amount(
            'ZWL', 'ZWL', '3.1415926'), '3.14')

    def test_home_page(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form action="/convert-currency">', html)

    def test_convert_currency_failure(self):
        with app.test_client() as client:
            resp = client.get('/convert-currency?from=USD&to=EUR&amount=0')

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, 'http://localhost/')

    def test_convert_currency_failure_followed(self):
        with app.test_client() as client:
            resp = client.get(
                '/convert-currency?from=USD&to=EUR&amount=0', follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<form action="/convert-currency">', html)
            self.assertIn('Not a valid input.', html)

    def test_convert_currency_success(self):
        with app.test_client() as client:
            resp = client.get('/convert-currency?from=USD&to=USD&amount=100')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('The result is $100.', html)
