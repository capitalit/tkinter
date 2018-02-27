
#from django.template import Context, loader
from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me':"hello hello Im from views.py!"}
    return render(request,'polls/index.html',context=my_dict)





    #return HttpResponse("<center>Hello, world. .</center>")
# Create your views here.
