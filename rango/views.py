from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass the template engine to its context
    # Note the key boldmessage is the same as {{ boldmessage }} in the 
    # template.
    context_dic = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    # Return a rendered resonse to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dic)

def about(request):
    return render(request, 'rango/about.html', context=None)
