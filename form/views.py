from django.shortcuts import render
from form.forms import *
import requests

# Create your views here.
def message(request):
    message_form=Message_Form()
    if request.method=='POST':
        message_form=Message_Form(request.POST)
        if message_form.is_valid():
            auth_token=""#use your auth_token from aakashsms.com
            to= message_form.cleaned_data.get("to")
            message=message_form.cleaned_data.get("message")
            print(message)
            r=requests.post("https://sms.aakashsms.com/sms/v3/send/",
            data={
                'auth_token':auth_token,
                'to':to,
                'text':message
            })
            status_code = r.status_code
            print(status_code)
            response = r.text
            response_json = r.json()
            
    context={
        'message_form':message_form
    }
    return render(request, 'index.html', context)
