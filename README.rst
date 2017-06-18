===========
kwargs-only
===========

.. image:: https://img.shields.io/travis/adamchainz/kwargs-only/master.svg
        :target: https://travis-ci.org/adamchainz/kwargs-only

.. image:: https://img.shields.io/pypi/v/kwargs-only.svg
        :target: https://pypi.python.org/pypi/kwargs-only

A decorator to make a function accept keyword arguments only, on both Python 2
and 3.

If you are only using Python 3, you don't need this, you can just do:

.. code-block:: python

    def myfunction(*, foo=1, bar=2):
        pass

Why?
====

If you are making a library (that still supports Python 2), you might want to
make all functions in its API take keyword arguments only, for a couple of
reasons:

* To avoid user confusion, e.g. if you take ``x`` and ``y`` arguments as
  coordinates, it's easy to forget which way round to pass them.
* To make your API easier to extend - you'll know no callers rely on the
  positional argument ordering, so can refactor this to make sense.

Installation
============

Use **pip**:

.. code-block:: sh

    pip install kwargs-only

Tested on Python 2.7 and Python 3.6.

Usage
=====

Import the decorator and apply it to a function:

.. code-block:: python

    from kwargs_only import kwargs_only

    @kwargs_only
    def myfunction(foo=1, bar=2):
        pass

Then calling the function with positional arguments will cause it to fail with
``TypeError``:

.. code-block:: python

    >>> myfunction(1, 2)
    ...
    TypeError: myfunction should only be called with keyword args

The decorator detects methods and classmethods, by allowing for the first
argument to be a positional one if its name is ``self`` or ``cls``.
``kwargs_only`` should be applied to the function before ``classmethod`` is.
For example:

.. code-block:: python

    class MyClass:

        @classmethod
        @kwargs_only
        def my_class_method(cls, foo=1):
            pass

        @kwargs_only
        def my_instance_method(self, bar=1):
            pass

That's about all there is to it! Enjoy!
