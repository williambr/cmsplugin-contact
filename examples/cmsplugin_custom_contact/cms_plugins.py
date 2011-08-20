from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool

from cmsplugin_contact.cms_plugins import ContactPlugin
from cmsplugin_contact.forms import ContactForm
from cmsplugin_contact.model import BaseContact

class CustomContact(BaseContact):
    custom_label = models.CharField(
        _('Custom sender label'),
        default=_('Your custom value'), max_length=20)

class CustomContactForm(ContactForm):
    custom = forms.CharField()

class CustomContactPlugin(ContactPlugin):
    model = CustomContact
    name = _("Custom Contact Form")
    render_template = "cmsplugin_contact/contact.html"
    contact_form = CustomContactForm
    email_template = "cmsplugin_contact/email.txt"
    
    fieldsets = (
        (None, {
                'fields': ('site_email', 'email_label', 'custom_label',
                           'subject_label', 'content_label', 'thanks',
                           'submit'),
        }),
        (_('Spam Protection'), {
                'fields': ('spam_protection_method', 'akismet_api_key',
                           'recaptcha_public_key', 'recaptcha_private_key',
                           'recaptcha_theme')
        })
    )

plugin_pool.register_plugin(CustomContactPlugin)
