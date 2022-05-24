#!/urs/bin/python3
""" Low memory cost """


class LockedClass:
    """that prevents the user from dynamically creating new instance attr,
    except if the new instance attribute is called
    first_name"""
    __slots__ = ['first_name']
