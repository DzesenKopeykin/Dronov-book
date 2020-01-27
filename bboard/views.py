from django.shortcuts import render

from .models import Ad


def index(request):
    ads = Ad.objects.all()
    return render(request, "bboard/index.html", {"ads": ads})
