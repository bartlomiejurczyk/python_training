# -*- coding: utf-8 -*-
from model.group import Group


def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(_name="test1_edit", _header="header1_edit", _footer="footer1_edit"))
    app.session.logout()