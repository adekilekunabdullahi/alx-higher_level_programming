#!/usr/bin/python3
"""DOC"""


class MyList(list):
    def append(self, item):
        super().append(str(item))
    def print_sorted(self):
        MyList.lists.append()
        srt = MyList.lists.sort()
        print(srt)
