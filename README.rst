==============================
Django CMS Contact Form Plugin
==============================

Contact form plugin for `Django CMS <http://www.django-cms.org/>`_ with spam protection and i18n.

If you want to use ReCAPTCHA you have to get a Public and Private Key from http://www.google.com/recaptcha. You can get them for free.

The Akismet spam protection method requires an Akismet API Key which is obtainable from http://akismet.com/ For private persons this is free, too.

Dependencies
============

Python Libs
-----------

If you decide to use the ReCAPTCHA spam protection method you need to install the python library ``recaptcha-client`` (package ``python-recaptcha`` in Debian).

If you use Akismet for spam protection ``akismet`` is needed. You also need to set your domain url in django admin in the section "sites".

Both libraries can be installed by ``pip`` or ``easy_install``.

It is recommended but not required to use South. Again it can be easily installed by ``pip`` or ``easy_install``.

Installation
============

Download
--------

From PyPI
'''''''''

You can simply type into a terminal ``pip install cmsplugin-contact`` or ``easy_install cmsplugin-contact``.

Manually
''''''''

You can download a zipped archive from http://github.com/maccesch/cmsplugin-contact/downloads.

Unzip the file you downloaded. Then go in your terminal and ``cd`` into the unpacked folder. Then type ``python setup.py install`` in your terminal.

Setup
-----

Put ``'cmsplugin_contact'`` in your ``INSTALLED_APPS`` section in settings.py. Don't forget to syncdb your database or migrate if you're using South.

Settings
========

RECAPTCHA_PUBLIC_KEY and RECAPTCHA_PRIVATE_KEY
----------------------------------------------

If you don't want to enter the ReCATPCHA keys in the admin interface you can provide them through these settings.

AKISMET_API_KEY
---------------

The same as for ReCAPTCHA goes fo Akismet.

DEFAULT_FROM_EMAIL
------------------

This django setting is used to set the ``From`` header of the emails. The value you can enter in django admin only sets the ``Reply-To`` header.
This is because many servers reject mails that claim to be ``From`` different email addresses than registered with the server.

Editors
=======

The default editor is WYMEditor like in Django CMS.
The plugin respects the ``USE_TINYMCE`` setting of Django CMS. Please see Django CMS docs for more information on how to use TinyMCE.
If you have the package ``'djangocms_text_ckeditor'`` in your ``INSTALLES_APPS`` CKEditor is used.


Extending
=========

See ``examples/cmsplugin_custom_contact`` how to subclass
``cmsplugin_contact`` and add custom fields into it. You can override
properties of the subclassed ``ContactPlugin`` and use your own templates
and classes.

Signals
-------

Email sent
''''''''''

After the contact email has been sent a signal is fired. You can use it like
this::

    from django.dispatch import receiver
    from cmsplugin_contact.cms_plugins import email_sent


    @receiver(email_sent)
    def handle_signal(sender, **kwargs):
        print kwargs['data']
