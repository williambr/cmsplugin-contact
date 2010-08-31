from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.template.loader import render_to_string
from models import Contact
from forms import AkismetContactForm, RecaptchaContactForm, HoneyPotContactForm
from django.core.mail import EmailMessage

class ContactPlugin(CMSPluginBase):
    model = Contact
    name = _("Contact Form")
    render_template = "cmsplugin_contact/contact.html"

    def create_form(self, instance, request):
        if instance.get_spam_protection_method_display() == 'Akismet':
            AkismetContactForm.aksimet_api_key = instance.aksimet_api_key
            FormClass = AkismetContactForm
        elif instance.get_spam_protection_method_display() == 'ReCAPTCHA':
            RecaptchaContactForm.recaptcha_public_key = instance.recaptcha_public_key
            RecaptchaContactForm.recaptcha_private_key = instance.recaptcha_private_key
            RecaptchaContactForm.recaptcha_theme = instance.recaptcha_theme
            FormClass = RecaptchaContactForm
        else:
            FormClass = HoneyPotContactForm
            
        if request.method == "POST":
            return FormClass(request, data=request.POST)
        else:
            return FormClass(request)


    def send(self, form, site_email):
        subject = form.cleaned_data['subject']
        if not subject:
            subject = _('No subject')
        email_message = EmailMessage(
            subject,
            render_to_string("cmsplugin_contact/email.txt", {
                'data': form.cleaned_data,
            }),
            site_email,
            [site_email],
            headers = {
                'Reply-To': form.cleaned_data['email']
            },)
        email_message.send(fail_silently=True)
    
    def render(self, context, instance, placeholder):
    	request = context['request']

        form = self.create_form(instance, request)
    
    	if request.method == "POST" and form.is_valid():
			self.send(form, instance.site_email)
			context.update( {
				'contact': instance,
			})
    	else:
            context.update({
                'contact': instance,
                'form': form,
            })
            
        return context
    
plugin_pool.register_plugin(ContactPlugin)
