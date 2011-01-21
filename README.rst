==============================
Django CMS Contact Form Plugin
==============================

Contact form plugin for `Django CMS <http://www.django-cms.org/>`_ with spam protection and i18n.

Spam protection is done through `glamkit-stopspam <http://github.com/maccesch/glamkit-stopspam>`_ which provides three different protection methods.

If you want to use ReCAPTCHA you have to get a Public and Private Key from http://www.google.com/recaptcha. You can get them for free.

The Akismet spam protection method requires an Akismet API Key which is obtainable from http://akismet.com/ For private persons this is free, too.

For more Information on the spam protection methods see the glamkit-stopspam link below.

Dependencies
============

Django Apps
-----------

`glamkit-stopspam <http://github.com/maccesch/glamkit-stopspam>`_ provides nice spam protection support.
You have to use the latest version from https://github.com/glamkit/glamkit-stopspam/ as the version in PyPI is outdated.

Python Libs
-----------

If you decide to use the ReCAPTCHA spam protection method glamkit-stopspam needs "recaptcha-client".

If you use Akismet for spam protection "akismet" is needed. You also need to set your domain url in django admin "sites".

Both libraries can be installed by ``easy_install`` or ``pip``.

Installation
============

From PyPI
---------

You can simply type into a terminal ``pip install cmsplugin-contact`` or ``easy_install cmsplugin-contact``.

Manual Download
---------------

You can download a zipped archive from http://github.com/maccesch/cmsplugin-contact/downloads.

Unzip the file you downloaded. Then go in your terminal and ``cd`` into the unpacked folder. Then type ``python setup.py install`` in your terminal.

Put "cmsplugin_contact" in your ``INSTALLED_APPS`` section in settings.py. Don't forget to syncdb your database.

Settings
========

RECAPTCHA_PUBLIC_KEY and RECAPTCHA_PRIVATE_KEY
----------------------------------------------

If you don't want to enter the ReCATPCHA keys in the admin interface you can provide them through these settings.

AKISMET_API_KEY
---------------

The same as for ReCAPTCHA goes fo Akismet.