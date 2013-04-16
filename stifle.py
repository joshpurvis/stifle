#! /usr/bin/env python
# coding=utf-8
from functools import wraps
from itertools import izip


class InvalidArgumentType(Exception):
    pass


def typed(*types, **kwtypes):
    """ Decorator which allows pseudo typing of a method's args/kwargs. Yes, I'll see you in hell. """

    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            # args
            for arg, t in izip(args, types):
                if not isinstance(arg, t):
                    e = "'%(value)s' is not of %(type)s" % {'value': arg, 'type': t}
                    raise InvalidArgumentType(e)

            # kwargs
            for k, t in kwtypes.iteritems():
                if k in kwargs and not isinstance(kwargs.get(k), t):
                    e = "'%(value)s' is not of %(type)s" % {'value': kwargs.get(k), 'type': t}
                    raise InvalidArgumentType(e)

            return func(*args, **kwargs)
        return decorator
    return wrapper
