Django Object FAQ
============

A reusable Django app that allows to attach Q&As to any Django model instance

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-object-faq

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-object-faq.git#egg=object_faq

TODO: Describe further installation steps (edit / remove the examples below):

Add ``object_faq`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'object_faq',
    )

Add the ``object_faq`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^object-faq/', include('object_faq.urls')),
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load object_faq_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate object_faq


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-object-faq
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch
