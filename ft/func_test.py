# -*- coding:utf-8 -*-

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):  # 1

    def setUp(self):  # 2
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  # 3
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  # 4
        # Аліса прочула про новий крутий blog app та вирішила відівіти його головну сторінку. 
        self.browser.get('http://localhost:8000')

        # Отакої! Заголовок сторінки має зовсім не blog назву
        self.assertIn('Blog', self.browser.title)  # 5
        self.fail('Тест скінчився!')  # 6

        # А хотілося б внести отой блог у власні закладки - не склалося
        # далі ненормативна лексіка


if __name__ == '__main__':  # 7
    unittest.main()  # 8
