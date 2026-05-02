#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = a / b
        print"{}".format(x)
    except (TypeError):
        return None
    finally:
        print"{}".format(x)
