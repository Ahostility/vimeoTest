from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def videoCreate(request):
    name = "https://player.vimeo.com/video/535650264"
    return render(request,'videoVimeo/videoVimeo.html',locals())