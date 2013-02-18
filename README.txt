=====================
Eau de Web Highcharts
=====================

Introduction
============

Eau de Web Highcharts provides `Highcharts JS library`_ as zope3 resources.

.. note ::

  This add-on doesn't do anything by itself. It needs to be integrated by a
  developer within your own products.

Installation
============

zc.buildout
-----------
If you are using `zc.buildout`_ and the `plone.recipe.zope2instance`_
recipe to manage your project, you can do this:

* Update your buildout.cfg file:

  * Add ``edw.highcharts`` to the list of eggs to install
  * Tell the `plone.recipe.zope2instance`_ recipe to install a ZCML slug

  ::

    [instance]
    ...
    eggs =
      ...
      edw.highcharts

    zcml =
      ...
      edw.highcharts

* Re-run buildout, e.g. with::

  $ ./bin/buildout

You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.

Source code
===========

- `Eau de Web on Github <https://github.com/eaudeweb/edw.highcharts>`_

.. _`Highcharts JS library`: http://highcharts.com
.. _`plone.recipe.zope2instance`: http://pypi.python.org/pypi/plone.recipe.zope2instance