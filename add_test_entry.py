
# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import unittest
from contact import Contact


def is_element_present(self, how, what):
    try:
        self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e:
        return False
    return True


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_empty_entry(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver)
        self.add_new_entry(driver)
        self.fill_new_entry(driver, Contact(_first_name="", _middle_name="", _last_name="", _nickname="",
                          _tittle="", _company="", _address="", _telephone_home="",
                          _telephone_mobile="", _telephone_work="", _fax="", _email="",
                          _email_2="", _email_3="", _homepage="", _bday="", _bmonth="-",
                          _byear="", _aday="", _amonth="-", _ayear="", _secondary_address="",
                          _secondary_home="", _secondary_notes=""))

        self.return_to_homepage(driver)
        self.logout(driver)

    def test_untitled_test_case(self):
        driver = self.driver
        self.open_homepage(driver)
        self.login(driver)
        self.add_new_entry(driver)
        self.fill_new_entry(driver, Contact(_first_name="Zbigniew", _middle_name="Janusz", _last_name="Brzeczyszczykiewicz", _nickname="nick123",
                          _tittle="tittle123", _company="Company XYZ", _address="adress 3/5", _telephone_home="658123123",
                          _telephone_mobile="654987987", _telephone_work="54121212", _fax="+52 45878787", _email="email123@email.com",
                          _email_2="email2@email2.com", _email_3="email3@email3.com", _homepage="www.bartek123.com", _bday="10", _bmonth="July",
                          _byear="1989", _aday="19", _amonth="December", _ayear="2010", _secondary_address="secondary address",
                          _secondary_home="secondaryHome", _secondary_notes="some additional notes"))

        self.return_to_homepage(driver)
        self.logout(driver)

    def fill_new_entry(self, driver, contact):
        # fill contact form
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.first_name)
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middle_name)
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.last_name)
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nickname)
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(contact.tittle)
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(contact.company)
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(contact.telephone_home)
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(contact.telephone_mobile)
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(contact.telephone_work)
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(contact.fax)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(contact.email2)
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(contact.email3)
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(contact.homepage)
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        driver.find_element_by_xpath("//option[@value='" + contact.bday + "']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        driver.find_element_by_xpath("//option[@value='" + contact.bmonth + "']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(contact.byear)
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        driver.find_element_by_xpath("(//option[@value='" + contact.aday + "'])[2]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        driver.find_element_by_xpath("(//option[@value='" + contact.amonth + "'])[2]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(contact.ayear)
        driver.find_element_by_name("theform").click()
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(contact.secondary_address)
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(contact.secondary_home)
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(contact.secondary_notes)
        # add new entry (press to submit button)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_homepage(self, driver):
        driver.find_element_by_link_text("home page").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def add_new_entry(self, driver):
        driver.find_element_by_link_text("add new").click()

    def login(self, driver):
        # fill login and password and click submit button
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_homepage(self, driver):
        driver.get("http://localhost:8080/addressbook/")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
