# -*- coding: utf-8 -*-
from model.group import Group



def test_add_test_group(app):
    app.group.create_group(Group(_name="test1", _header="header1", _footer="footer1"))


def test_add_empty_group(app):
    app.group.create_group(Group(_name="", _header="", _footer=""))




