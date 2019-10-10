

class Project:

    def __init__(self, name=None):
        self.name = name


    def __repr__(self):
        return "\n%s" % (self.name)

    def __eq__(self, other):
        return (self.name is None or other.name is None or self.name == other.name)


