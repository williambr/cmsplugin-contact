from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

class Contact(CMSPlugin):
	SPAM_PROTECTION_CHOICES = (
	    (0, 'Honeypot'),
	    (1, 'Akismet'),
	    (2, 'ReCAPTCHA'),
	)
    
	THEME_CHOICES = (
	    ('clean', 'Clean'),
	    ('red', 'Red'),
	    ('white', 'White'),
	    ('blackglass', 'Black Glass'),
        ('custom', 'Custom'),
	)
	
	site_email 	= models.EmailField(_('Email Recipient'))
	email_label 	= models.CharField(_('Email Sender Label'), blank=True, max_length=100)
	subject_label	= models.CharField(_('Subject Label'), blank=True, max_length=200)
	content_label 	= models.CharField(_('Message Content Label'), blank=True, max_length=100)
	thanks 		= models.CharField(verbose_name=_("Thanks Message"), help_text=_('Message displayed on successful submit'), max_length=200)
	submit		= models.CharField(_('Submit Button Value'), blank=True, max_length=30)
	
	spam_protection_method = models.SmallIntegerField(help_text=_('Method to protect your site from spam'), choices=SPAM_PROTECTION_CHOICES)
    
	akismet_api_key = models.CharField(help_text=_('Only if you are using Akismet spam protection.'), verbose_name="Akismet API Key", max_length=255, blank=True)
	
	recaptcha_public_key = models.CharField(help_text=_('Only if you are using ReCAPTCHA spam protection.'), verbose_name="ReCAPTCHA Public Key", max_length=255, blank=True)
	recaptcha_private_key = models.CharField(help_text=_('Only if you are using ReCAPTCHA spam protection.'), verbose_name="ReCAPTCHA Private Key", max_length=255, blank=True)
	recaptcha_theme = models.CharField(max_length=20, choices=THEME_CHOICES, default='clean', help_text=_('Only if you are using ReCAPTCHA spam protection.'))
	
	def __unicode__(self):
		return self.site_email
