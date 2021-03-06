# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(_name="test1", _header="header1", _footer="footer1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(_name="test1_edit")
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




#def test__modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create_group(Group(_name="test1", _header="header1", _footer="footer1"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(_header="header1_edit"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)



#def test__modify_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create_group(Group(_name="test1", _header="header1", _footer="footer1"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(_footer="footer1_edit"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

