
from model.contact import Contact
from random import randrange
import random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.fill_new_entry(
            Contact(_first_name="Zbigniew", _middle_name="Janusz", _last_name="Brzeczyszczykiewicz",
                    _nickname="nick123",
                    _tittle="tittle123", _company="Company XYZ", _address="adress 3/5", _telephone_home="658123123",
                    _telephone_mobile="654987987", _telephone_work="54121212", _fax="+52 45878787",
                    _email="email123@email.com",
                    _email_2="email2@email2.com", _email_3="email3@email3.com", _homepage="www.bartek123.com",
                    _bday="10", _bmonth="July",
                    _byear="1989", _aday="19", _amonth="December", _ayear="2010",
                    _secondary_address="secondary address",
                    _secondary_home="secondaryHome", _secondary_notes="some additional notes"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    #assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    #assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
