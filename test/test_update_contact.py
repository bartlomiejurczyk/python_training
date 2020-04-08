
from model.contact import Contact


def test_update_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(Contact(_first_name="EDIT", _middle_name="EDIT", _last_name="EDIT", _nickname="EDIT",
                _tittle="EDIT", _company="EDIT", _address="EDIT", _telephone_home="EDIT",
                _telephone_mobile="EDIT", _telephone_work="EDIT", _fax="+52 EDIT",
                _email="EDIT@EDIT.com",
                _email_2="EDIT@EDIT.com", _email_3="EDIT@EDIT.com", _homepage="www.EDIT.com", _bday="12",
                _bmonth="March",
                _byear="1989", _aday="21", _amonth="June", _ayear="3030", _secondary_address="EDIT address",
                _secondary_home="EDIT", _secondary_notes="EDIT notes"))
    app.session.logout()