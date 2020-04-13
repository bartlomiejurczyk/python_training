# -*- coding: utf-8 -*-
from model.group import Group



def test__modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(_name="test1", _header="header1", _footer="footer1"))
    app.group.modify_first_group(Group(_name="test1_edit"))



def test__modify_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(_name="test1", _header="header1", _footer="footer1"))
    app.group.modify_first_group(Group(_header="header1_edit"))


def test__modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create_group(Group(_name="test1", _header="header1", _footer="footer1"))
    app.group.modify_first_group(Group(_footer="footer1_edit"))
