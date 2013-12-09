Django Object FAQ
=================

A reusable Django app that allows to attach Q&As to any Django model instance.

Currently the app provides the models for adding translated questions and 
answers as well as a template tag to render them from a default template, you
can of course override and customize according to your needs.

Future updates might include forms, that allow users to send their own
questions, but it is currently not implemented. Contributions are welcome =)


Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-object-faq

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-object-faq.git#egg=object_faq


Add ``object_faq`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'object_faq',
    )

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load object_faq_tags %}

Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate object_faq


Usage
-----

In your django admin, you can create the ``Entry`` objects with questions and
answers to be rendered on the page. ``position`` is the default ordering of the
queryset.

Additionally you can setup a ``GlobalObjectDescription`` object per model
instance. This will render a general title and description, you might want to
use as introductory text for the object's FAQ or just as general object
description.

Then you only need to add the template tag for the object in the context.
.. code-block:: html

	{% load object_faq_tags %}

    {% render_faq_for_object myobject %}

This will automatically render the tempalte located at
``object_faq/partials/object_faq.html``.


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
