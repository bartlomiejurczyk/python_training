import re
from model.contact import Contact


def test_contact_on_home_page(app, db):
    contact_home_page = app.contact.get_contact_list()
    contact_db = db.get_contact_list()
    assert sorted(contact_db, key=Contact.id_or_max) == sorted(contact_home_page, key=Contact.id_or_max)



def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.secondaryphone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))