# -*- coding: utf-8 -*-
from model.group import Group



def test_add_test_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(_name="test1", _header="header1", _footer="footer1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(_name="", _header="", _footer=""))
    app.session.logout()




