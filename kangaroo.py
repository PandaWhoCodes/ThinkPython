class Kangaroo(object):
    def __init__(self, contents=None):
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        t = [object.__str__(self) + ' with pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)


kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)
print(kanga)
print(roo)
