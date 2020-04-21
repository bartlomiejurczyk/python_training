
# -*- coding: utf-8 -*-
from typing import List, Any

from model.contact import Contact



#def test_add_empty_entry(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(_first_name="", _middle_name="", _last_name="", _nickname="",
#                    _tittle="", _company="", _address="", _telephone_home="",
#                    _telephone_mobile="", _telephone_work="", _fax="", _email="",
#                    _email_2="", _email_3="", _homepage="", _bday="", _bmonth="-",
#                    _byear="", _aday="", _amonth="-", _ayear="", _secondary_address="",
#                    _secondary_home="", _secondary_notes="")
#    app.contact.fill_new_entry(contact)
#    new_contacts = app.group.get_group_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_untitled_test_case(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(_first_name="Zbigniew", _middle_name="Janusz", _last_name="Brzeczyszczykiewicz", _nickname="nick123",
                          _tittle="tittle123", _company="Company XYZ", _address="adress 3/5", _telephone_home="658123123",
                          _telephone_mobile="654987987", _telephone_work="54121212", _fax="+52 45878787", _email="email123@email.com",
                          _email_2="email2@email2.com", _email_3="email3@email3.com", _homepage="www.bartek123.com", _bday="10", _bmonth="July",
                          _byear="1989", _aday="19", _amonth="December", _ayear="2010", _secondary_address="secondary address",
                          _secondary_home="secondaryHome", _secondary_notes="some additional notes")
    app.contact.fill_new_entry(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




