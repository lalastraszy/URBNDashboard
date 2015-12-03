from django.test import TestCase
from selenium import webdriver


class BrandTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_brands(self):
        # user goes to http://localhost:8000/
        self.browser.get('http://localhost:8000/') #self.live_server_url + '/'
        # user sees brand dropdown menu
        brands_dropdown_menu = self.browser.find_element_by_id('brandsDropdownMenu')

        self.assertEqual('Brand', brands_dropdown_menu.text)

        brands_dropdown_menu.click()

        self.browser.implicitly_wait(5)

        brand_uo_eu_element = self.browser.find_element_by_link_text('UO EUROPE (EU)')
        self.assertTrue(brand_uo_eu_element.is_displayed())

        brand_uo_eu_element.click()


# class DashboardURLsTestCase(TestCase):

# 	def test_root_url_uses_index_view(self):
#         """
#         Test that the root of the site resolves to the
#         correct view function
#         """
#         root = resolve('/')
#         self.assertEqual(root.func, Index.asView)
