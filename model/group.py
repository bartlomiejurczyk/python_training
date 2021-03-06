
from sys import maxsize


class Group:

    def __init__(self, _name=None, _header=None, _footer=None, _id=None):
        self.name = _name
        self.header = _header
        self.footer = _footer
        self.id = _id

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def __lt__(self, other):
        return self.id < other.id

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
