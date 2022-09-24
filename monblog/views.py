from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from monblog.modelsClasses.model_Post import PostClass 
# Create your views here.

def index(request):

    try:
        model=PostClass.listPosts()
        dic={
            'model': model
        }
        # create a response
        response = TemplateResponse(request, 'home.html', dic)
        # Return de response
        return response
    except Exception:
        return HttpResponse("ERROR")
