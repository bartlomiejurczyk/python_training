
from model.contact import Contact


def test_update_contact(app):
    if app.contact.count() == 0:
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
    old_contacts = app.contact.get_contact_list()
    contact = Contact(_first_name="EDIT", _middle_name="EDIT", _last_name="EDIT", _nickname="EDIT",
                _tittle="EDIT", _company="EDIT", _address="EDIT", _telephone_home="EDIT",
                _telephone_mobile="EDIT", _telephone_work="EDIT", _fax="+52 EDIT",
                _email="EDIT@EDIT.com",
                _email_2="EDIT@EDIT.com", _email_3="EDIT@EDIT.com", _homepage="www.EDIT.com", _bday="12",
                _bmonth="March",
                _byear="1989", _aday="21", _amonth="June", _ayear="3030", _secondary_address="EDIT address",
                _secondary_home="EDIT", _secondary_notes="EDIT notes")
    contact.id = old_contacts[0].id
    app.contact.update_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
