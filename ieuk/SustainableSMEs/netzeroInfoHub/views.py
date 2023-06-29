from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Reason

# Create your views here.
def home(request):
    template = loader.get_template("homePage.html")
    reasons = Reason.objects.all()
    context = {
        'reasons': reasons,
    }
    return HttpResponse(template.render(context, request))
