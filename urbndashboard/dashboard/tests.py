from django.test import TestCase
from selenium import webdriver
import datetime


class DashboardTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_generate_bar_chart(self):
        # user goes to http://localhost:8000/
        self.browser.get('http://10.55.9.1:8000/')
        # self.browser.get(self.live_server_url)

        # user sees brand dropdown menu
        brands_dropdown_menu = self.browser.find_element_by_id('brandDropdownMenu')
        self.assertTrue(brands_dropdown_menu.is_displayed())

        # user selects brand 'EU EUROPE (EU)'
        brands_dropdown_menu.click()
        self.browser.implicitly_wait(5)
        brand = self.browser.find_element_by_link_text('UO EUROPE (EU)')
        self.assertTrue(brand.is_displayed())
        brand.click()

        # user sees type of sales dropdown menu
        type_of_sales_dropdown_menu = self.browser.find_element_by_id('typeOfSalesDropdownMenu')
        self.assertTrue(type_of_sales_dropdown_menu.is_displayed())

        # user selects type of sales 'RETAIL'
        type_of_sales_dropdown_menu.click()
        self.browser.implicitly_wait(5)
        type_of_sale = self.browser.find_element_by_link_text('RETAIL')
        self.assertTrue(type_of_sale.is_displayed())
        type_of_sale.click()

        # user sees type of stat dropdown menu
        type_of_stat_dropdown_menu = self.browser.find_element_by_id('typeOfStatDropdownMenu')
        self.assertTrue(type_of_stat_dropdown_menu.is_displayed())

        # user selects type of stat 'HOURS'
        type_of_stat_dropdown_menu.click()
        self.browser.implicitly_wait(5)
        type_of_stat = self.browser.find_element_by_link_text('HOURS')
        self.assertTrue(type_of_stat.is_displayed())
        type_of_stat.click()

        # user sees date picker
        date_picker = self.browser.find_element_by_id('datePicker')
        self.assertTrue(date_picker.is_displayed())

        # user sets today date
        date_picker.click()
        self.browser.implicitly_wait(5)
        d = datetime.datetime.today()
        today_date = d.strftime('%Y-%m-%d')
        date_picker.send_keys(today_date)

        # user sees bar chart
        bar_chart = self.browser.find_element_by_id('barChart')
        self.assertTrue(bar_chart.is_displayed())
