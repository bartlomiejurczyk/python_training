from model.group import Group
import random
import string
from model.contact import Contact
import jsonpickle
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone_number():
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(9)])


def random_emails(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@gmail.com"


testdata = [Contact(_first_name="", _middle_name="", _last_name="", _nickname="",
                    _tittle="", _company="", _address="", _telephone_home="",
                    _telephone_mobile="", _telephone_work="", _fax="", _email="",
                    _email_2="", _email_3="", _homepage="", _bday="", _bmonth="-",
                    _byear="", _aday="", _amonth="-", _ayear="", _secondary_address="",
                    _secondary_home="", _secondary_notes="")] + [
            Contact(_first_name=random_string("firstname", 15), _middle_name=random_string("middlename", 15), _last_name=random_string("lastname", 15),
                    _nickname=random_string("nickname", 15), _tittle=random_string("tittle", 15), _company=random_string("company", 15),
                    _address=random_string("address", 15), _telephone_home=random_phone_number(),
                   _telephone_mobile=random_phone_number(), _telephone_work=random_phone_number(), _fax=random_phone_number(), _email=random_emails(20),
                   _email_2=random_emails(20), _email_3=random_emails(20), _homepage="www.bartek123.com", _bday="10", _bmonth="July",
                   _byear="1989", _aday="19", _amonth="December", _ayear="2010", _secondary_address=random_string("secondaryaddress", 15),
                   _secondary_home=random_phone_number(), _secondary_notes=random_string("secondarynotes", 15))
            for i in range(5)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))