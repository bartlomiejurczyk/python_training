# -*- coding: utf-8 -*-
from model.group import Group


def test__modify_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(_name="test1", _header="header1", _footer="footer1"))
    old_groups = app.group.get_group_list()
    group = Group(_name="test1_edit")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



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