==============================
examples-django-material-admin
==============================

A example for use `Django Admin`_ and `MaterializeCSS`_ support with `material-admin`_.


Features
========

- `Django`_ project 3 version.

- Todo demonstration App.

- `Django Admin`_ with `MaterializeCSS`_ support.


Installation
============

::

  $ git clone https://github.com/macagua/examples-django-material-admin.git
  $ cd material-admin/
  $ virtualenv -p python3 venv
  $ source venv/bin/activate
  $ pip3 install -r requirements.txt
  $ cd djangomaterial
  $ python manage.py migrate
  $ python manage.py createsuperuser --username admin --email admin@mail.com
  $ python manage.py runserver

You can see the Django project default here http://127.0.0.1:8000/

You can see the Django Admin default app default here http://127.0.0.1:8000/admin/


.. image:: https://raw.githubusercontent.com/macagua/examples-django-material-admin/master/docs/_static/screenshot.png
   :height: 485px
   :width: 800px
   :alt: My Django Admin with MaterializeCSS support
   :align: right


Reference
=========

- `Quick start tutorial <https://github.com/MaistrenkoAnton/django-material-admin/blob/master/README.rst>`_.

.. _`material-admin`: https://pypi.org/project/django-material-admin/
.. _`Django`: https://docs.djangoproject.com/en/3.0/
.. _`Django Admin`: https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
.. _`MaterializeCSS`: http://materializecss.com/