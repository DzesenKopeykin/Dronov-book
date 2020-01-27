from django.shortcuts import render

from .models import BillBoard


def index(request):
    billboards = BillBoard.objects.order_by("-published")
    return render(request, "bboard/index.html", {"billboards": billboards})
