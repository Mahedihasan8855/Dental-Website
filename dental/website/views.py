from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
	 return render(request,'home.html')


def contact(request):
	if request.method == "POST":
		message_name=request.POST['message-name']
		message_email=request.POST['message-email']
		message=request.POST['message']
		send_mail(message_name,
			message,
			message_email,
			['mahedihassan8855@gmail.com'],
			fail_silently=False,

			)
		context = {'message_name': message_name, 'message-email':message_email,'message':message}
		return render(request,'contact.html',context)

	else:
		return render(request,'contact.html',{})