#! /usr/bin/env python
# coding=utf-8

import unittest
from stifle import typed, InvalidArgumentType


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_matching_int(self):

        @typed(int)
        def matching_int(some_int):
            self.assertIsInstance(some_int, int)

        matching_int(1)

    def test_arg_and_kwarg_mix(self):
        """ Mixing args and kwargs while typing """

        @typed(int, str, named_kw=str)
        def arg_and_kwarg_mix(some_int, some_str, named_kw=''):
            self.assertIsInstance(some_int, int)
            self.assertIsInstance(some_str, str)
            self.assertIsInstance(named_kw, str)

        arg_and_kwarg_mix(1, 'hello there', named_kw='hey')

    def test_mismatched_str(self):

        @typed(str)
        def mismatched_str(some_value):
            pass

        not_a_string = 1

        self.assertRaises(InvalidArgumentType, mismatched_str, not_a_string)

    def test_arg_and_optional_kwarg(self):
        """ Test with and without a typed kw argument """

        @typed(int, named_str_kw=str)
        def arg_and_optional_kwarg(some_int, named_str_kw=''):
            self.assertIsInstance(some_int, int)
            self.assertIsInstance(named_str_kw, str)

        arg_and_optional_kwarg(1)
        arg_and_optional_kwarg(1, named_str_kw='hi')

        self.assertRaises(InvalidArgumentType, arg_and_optional_kwarg, 'hi', 123)

    def test_if_object(self):
        """ Typed as an object of any sort """

        class Foo(object):
            pass

        @typed(object)
        def if_object(some_obj):
            self.assertIsInstance(some_obj, object)

        if_object(Foo())

    def test_custom_type(self):
        """ Typed based on user defined classes """

        class FooType:
            pass

        class NotFooType:
            pass

        @typed(FooType)
        def custom_type(some_object):
            self.assertIsInstance(some_object, FooType)

        custom_type(FooType())

        # test negated
        self.assertRaises(InvalidArgumentType, custom_type, NotFooType())

    def test_too_many_types(self):
        """ Define more types than there are arguments """

        @typed(int, str)
        def too_many_types(some_int):
            pass

        # TODO: this doesn't complain, probably should
        too_many_types(1)

