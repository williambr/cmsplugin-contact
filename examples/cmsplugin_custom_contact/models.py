from django.db import models
from cmsplugin_contact.models import BaseContact
from django.utils.translation import ugettext_lazy as _

class CustomContact(BaseContact):
    custom_label = models.CharField(
        _('Custom sender label'),
        default=_('Your custom value'), max_length=20)
