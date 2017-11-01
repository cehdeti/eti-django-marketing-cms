=====
ETI Marketing Landing Pages
=====

This is a custom Django Admin CMS for creating marketing landing pages for ETI related projects.

Installing the Package
-----------------

Download the tar file inside the **dist** folder::

  pip install --user django-eti-marketing-cms-0.1.tar.gz

Quick Start
-----------

1. Add ``'marketing'`` to **INSTALLED_APPS** in ``settings.py``::

	INSTALLED_APPS = [
		...
		'marketing',
	]

2. Include the ``URLconf`` in the project::

	url(r'^', include('marketing.urls')),

3. Run :bash:`python manage.py migrate` to generate the models.

4. Start the server :bash:`python manage.py runserver`

5. Create a superadmin :bash:`python manage.py createsuperuser` then create pages at the admin: `http://localhost:8000/admin`


Notes
------

Obviously the templates are just based stuff. You should always extend those from the actualy project `base` template etc...