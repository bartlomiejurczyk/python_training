import mysql.connector
from model.group import Group
from model.contact import Contact

class Dbfixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(_name=name, _header=header, _footer=footer, _id=str(id)))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, mobile, email from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, mobile, email) = row
                list.append(Contact(_id=str(id), _first_name=firstname, _last_name=lastname, _address=address, _telephone_mobile=mobile, _email=email))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()