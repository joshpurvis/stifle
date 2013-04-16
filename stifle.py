#! /usr/bin/env python
# coding=utf-8

"""
    Copyright (c) 2013, Josh Purvis (http://joshpurvis.com)

    Some rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are
    met:

    * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above
    copyright notice, this list of conditions and the following
    disclaimer in the documentation and/or other materials provided
    with the distribution.

    * The names of the contributors may not be used to endorse or
    promote products derived from this software without specific
    prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
    OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

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
