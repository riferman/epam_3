from collections import Counter

n = 25

string = """The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


def count_each_letter():  # Find how many times each letter is met in the text, print the findings as described below
    a = Counter(string)
    print("count_each_letter", a)
    return a


def sort_the_table():  # Sort the table by alphabet and print it out
    def record():
        # Allow adjusting the limits for table output, i.e. getting only certain amount of entries from the top (the limit number may be set as a global variable)
        e = list(reversed(b))[:n]
        print("Getting only certain amount of entries from the top", e)
        return e

    def list_revers():  # Flip this list horizontally and print it out
        d = list(reversed(b))
        print("List revers", b)
        return d

    def sort_symbols():  # Sort the table by the symbols’ frequency count and print it out
        c = sorted(b, key=lambda x: x[1])
        print("Sort the table by the symbols", c)
        return c

    b = sorted(list(Counter(string).items()), key=lambda x: x[0])
    print("Sort_the_table", b)
    record()
    list_revers()
    sort_symbols()
    return b


count_each_letter()
sort_the_table()
