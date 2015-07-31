==============================
Django CMS Contact Form Plugin
==============================

Contact form plugin for `Django CMS <http://www.django-cms.org/>`_ with spam protection and i18n.

The message entered by the web user is turned into an email which is sent to the email address
configured for the specific plugin instance.

Spam protection is provided by either `ReCAPTCHA <http://www.google.com/recaptcha>`_ (free) or
`Akismet <http://akismet.com/>`_ (free for personal use).
Visit the respective website to obtain the keys required to activate the protection method of your
choice.

Dependencies
============

Python Libs
-----------

If you decide to use the ReCAPTCHA spam protection method you need to install the python library ``recaptcha-client`` (package ``python-recaptcha`` in Debian).

If you use Akismet for spam protection ``akismet`` is needed. You also need to set your domain url in django admin in the section "sites".

For Python version <2.7, ``importlib`` has to be installed since ``importlib`` is in the standard library in Python 2.7, but is a third-party package for older versions.

All libraries can be installed by ``pip`` or ``easy_install``.

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

You can download a zip archive of the `latest development version 
<https://github.com/maccesch/cmsplugin-contact/archive/master.zip>`_ from GitHub. 
Unzip the file you downloaded. Then go in your terminal and ``cd`` into the unpacked folder. Then type ``python setup.py install`` in your terminal.

Setup
-----

Put ``'cmsplugin_contact'`` in your ``INSTALLED_APPS`` section in settings.py. Don't forget to syncdb your database or migrate if you're using South.

Put ``'cmsplugin_contact.middleware.ForceResponseMiddleware'`` in your ``MIDDLEWARE_CLASSES`` section in settings.py.


Settings
========

DEFAULT_FROM_EMAIL
------------------

The email address that is used to send the message is picked up from ``DEFAULT_FROM_EMAIL``
`Django setting <https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email>`_.
Additionally, the ``Reply-To:`` header is set to the user-supplied email address.

Sending the message using the user-supplied address to set ``From:`` header of the email is
currently not supported.
This is because many servers will reject emails that use ``From:`` addresses not registered with
that server.
Some servers may also strip the ``Reply-To:`` header. For this, the user-supplied email address
is also added to the body of the message.

.. Note:
.. The info about Reply-To: header is unrelated to the DEFAULT_FROM_EMAIL setting.
.. At some point it should be moved in a more suitable place in the documentation.


RECAPTCHA_PUBLIC_KEY and RECAPTCHA_PRIVATE_KEY
----------------------------------------------

If you don't want to enter the ReCATPCHA keys in the admin interface you can provide them through these settings.

AKISMET_API_KEY
---------------

The same as for ReCAPTCHA goes fo Akismet.

CMSPLUGIN_CONTACT_FORMS
-----------------------

Default::

    (
        ('cmsplugin_contact.forms.ContactForm', _('default')),
    )

You can use your custom ContactForm, just add a new tuple with the class path and name pretty name to show for your user.

If you want to steal using the default ContactForm, do like this in your settings::

    (
        ('cmsplugin_contact.forms.ContactForm', _('default')),
        ('my_app.forms.MyContactForm', _('My form')),
    )

In your custom form, you can set what template you want to use, like this::

    class MyContactForm(Form):
        ...
        template = 'path/to/my_contact_template.html'

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
