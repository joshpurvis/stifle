Stifle
======

This is probably a bad idea.

Allows "static typing" on python functions using a decorator.

Will raise `InvalidArgumentType` Exception if types don't match.

##### Simple Example:

    from stifle import typed

    @typed(int)
    def must_take_int(n):
        return n + 1

    >>> must_take_int(1)
    2
    >>> must_take_int('nope')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "stifle.py", line 56, in decorator
        raise InvalidArgumentType(e)
    stifle.InvalidArgumentType: 'no' is not of <type 'int'>

##### Keyword arguments work too, but must be explicitly declared.

    @typed(int, multiplier=int)
    def keyword_arguments(n, multiplier=3):
        return n * multiplier

    keyword_arguments(1, multiplier=4)

##### Works with any type or custom class:

    class Foo:
        pass

    @typed(Foo)
    def foo_objects_only(foobar):
        return foobar

    foo_class_only(Foo())

