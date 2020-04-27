
from sys import maxsize


class Contact:

    def __init__(self, _first_name=None, _middle_name=None, _last_name=None, _nickname=None, _tittle=None, _company=None, _address=None,
                 _telephone_home=None, _telephone_mobile=None, _telephone_work=None, _fax=None,
                 _email=None, _email_2=None, _email_3=None, _homepage=None, _bday=None, _bmonth=None, _byear=None, _aday=None, _amonth=None, _ayear=None,
                 _secondary_address=None, _secondary_home=None, _secondary_notes=None, _id=None, _all_phones_from_homepage=None, _all_email_addresses=None):
        self.first_name = _first_name
        self.middle_name = _middle_name
        self.last_name = _last_name
        self.nickname = _nickname
        self.tittle = _tittle
        self.company = _company
        self.address = _address
        self.telephone_home = _telephone_home
        self.telephone_mobile = _telephone_mobile
        self.telephone_work = _telephone_work
        self.fax = _fax
        self.email = _email
        self.email2 = _email_2
        self.email3 = _email_3
        self.homepage = _homepage
        self.bday = _bday
        self.bmonth = _bmonth
        self.byear = _byear
        self.aday = _aday
        self.amonth = _amonth
        self.ayear = _ayear
        self.secondary_address = _secondary_address
        self.secondary_home = _secondary_home
        self.secondary_notes = _secondary_notes
        self.all_email_addresses = _all_email_addresses
        self.all_phones_from_home_page = _all_phones_from_homepage
        self.id = _id


    def __repr__(self):
        return "%s %s %s" % self.id, self.first_name, self.last_name

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize