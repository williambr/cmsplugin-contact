from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool

from cmsplugin_contact.cms_plugins import ContactPlugin
from models import CustomContact

class CustomContactPlugin(ContactPlugin):
    name = _("Custom Contact Form")
    
    model = CustomContact

    # Important: You have to add the following to your settings.py
    # CMSPLUGIN_CONTACT_FORMS =  (
    #     ('cmsplugin_contact.forms.ContactForm', _('default')),
    #     ('cmsplugin_custom_contact.forms.CustomContactForm', _('custom')),
    # )
    # if you're only using your custom plugin you can omit the first line

    # We're using the original cmsplugin_contact render templates here which
    # works fine but requires that the original plugin is in INSTALLED_APPS.
    render_template = "cmsplugin_contact/contact.html"

    # Custom email template to incorporate you custom data
    email_template = "cmsplugin_custom_contact/email.txt"
    
    fieldsets = (
        (None, {
            'fields': ('form_name', 'form_layout', 'site_email', 'submit', 'custom_label'),
        }),
        (_('Redirection'), {
            'fields': ('thanks', 'redirect_url' ),
        } ),
        (_('Spam Protection'), {
            'fields': ('spam_protection_method', 'akismet_api_key',
                       'recaptcha_public_key', 'recaptcha_private_key', 'recaptcha_theme')
        })
    )

plugin_pool.register_plugin(CustomContactPlugin)
