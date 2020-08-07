from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib.messages import constants as messages

# Create your views here.
def index(request):
    context = {
        'variable':'this is sent'
    }
    return render(request, 'index.html', context)
   # return HttpResponse('this is homepage')

def about(request):
     return render(request, 'about.html', )
   # return HttpResponse('this is about page')

def services(request):
     return render(request, 'services.html', )
   # return HttpResponse('this is services page')


def contact(request):
    
     return render(request, 'contact.html',)
   # return HttpResponse('this is contact page')
   

def submitcontact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Phone = request.POST.get('Phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=Phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent')
    
    return render(request, 'submitcontact.html')