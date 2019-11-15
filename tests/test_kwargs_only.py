# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import pytest
import six

from kwargs_only import kwargs_only


def test_kwargs_only_allows_keyword_args():
    @kwargs_only
    def foo(x, y):
        return (x, y)

    assert foo(y=2, x=1) == (1, 2)


def test_kwargs_only_does_not_allow_positional_args():
    @kwargs_only
    def foo(x):
        pass

    with pytest.raises(TypeError) as excinfo:
        foo(1)
    assert "should only be called with keyword args" in six.text_type(excinfo.value)


def test_kwargs_only_method_allows_keyword_args():
    class Foo(object):
        @kwargs_only
        def bar(self, x, y):
            return (x, y)

    assert Foo().bar(y=2, x=1) == (1, 2)


def test_kwargs_only_method_does_not_allow_positional_args():
    class Foo(object):
        @kwargs_only
        def bar(self, x):
            pass

    with pytest.raises(TypeError) as excinfo:
        Foo().bar(1)
    assert "should only be called with keyword args" in six.text_type(excinfo.value)


def test_kwargs_only_classmethod_allows_keyword_args():
    class Foo(object):
        @classmethod
        @kwargs_only
        def bar(cls, x, y):
            return (x, y)

    assert Foo.bar(y=2, x=1) == (1, 2)


def test_kwargs_only_classmethod_does_not_allow_positional_args():
    class Foo(object):
        @classmethod
        @kwargs_only
        def bar(self, x):
            pass

    with pytest.raises(TypeError) as excinfo:
        Foo.bar(1)
    assert "should only be called with keyword args" in six.text_type(excinfo.value)
