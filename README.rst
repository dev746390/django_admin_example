==============================
examples-django-material-admin
==============================

A example for Django 3 with `material-admin`_.

Installation
============

::

  $ git clone https://github.com/macagua/examples-django-material-admin.git
  $ cd material-admin/
  $ virtualenv -p python3 venv
  $ source venv/bin/activate
  $ pip3 install -r requirements.txt
  $ django-admin startproject djangomaterial
  $ cd djangomaterial
  $ python manage.py migrate
  $ python manage.py createsuperuser --username admin --email admin@mail.com
  $ python manage.py runserver

You can see the Django project default here http://127.0.0.1:8000/

You can see the Django Admin default app default here http://127.0.0.1:8000/admin/


Reference
=========

- `Quick start tutorial <https://github.com/MaistrenkoAnton/django-material-admin/blob/master/README.rst>`_.

.. _`material-admin`: https://pypi.org/project/django-material-admin/
