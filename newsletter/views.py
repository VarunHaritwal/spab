from src.trydjango18 import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):
	title = "Welcome"
	form = SignUpForm(request.POST or None)
	context = {
		"title" : title,
		"form" : form,
	}
	if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title" : "Thank you",
		
		}
	
	if request.user.is_authenticated() and request.user.is_staff:
		context = {
			"queryset":[123,564],

		}



	return render(request, "home.html", context)


def contact(request):
	title = "Contact Us"
	form = ContactForm(request.POST or None)
	if form.is_valid():
	#	for key, value in form.cleaned_data.items():
	#		print (key, value)
		form_full_name = form.cleaned_data.get('full_name')
		form_message = form.cleaned_data.get('message')
		form_email = form.cleaned_data.get('email')
	
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		contact_message = "%s:%s via %s" %(form_full_name,form_message,form_email)
		to_email = [from_email, 'youotheremail@email.com']

		send_mail(
			subject,
			contact_message,
			from_email,
			to_email,
			fail_silently=True,
			)
		

	context = {
		"form" : form,
		"title" : title,
	}
	return render(request, "forms.html", context)


