# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(_name="", _header="", _footer="")] + [
    Group(_name=random_string("name", 10), _header=random_string("header", 20), _footer=random_string("footer", 20))
    for i in range(5)
]

testdata2 = [
        Group(_name=name, _header=header, _footer=footer)
        for name in ["", random_string("name", 10)]
        for header in ["", random_string("name", 10)]
        for footer in ["", random_string("footer", 20)]
    ]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_test_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create_group(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    group = Group(_name="", _header="", _footer="")
#    app.group.create_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



