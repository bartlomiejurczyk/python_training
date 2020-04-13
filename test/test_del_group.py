

from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(_name="test1", _header="header1", _footer="footer1"))
    app.group.delete_first_group()
