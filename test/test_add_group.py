# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_test_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(_name="test1", _header="header1", _footer="footer1"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(_name="", _header="", _footer=""))
    app.session.logout()


