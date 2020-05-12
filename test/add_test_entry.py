# -*- coding: utf-8 -*-
from typing import List, Any

from model.contact import Contact
import pytest



#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_untitled_test_case(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.fill_new_entry(contact)
    new_contacts = db.get_contact_list()
    # assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



