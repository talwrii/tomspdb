import re


def f():
    g()


def g():
    raise re.compile("[")


if __name__ == "__main__":
    f()
