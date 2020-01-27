from django.http import HttpResponse
from django.template import loader

from .models import BillBoard


def index(request):
    template = loader.get_template("bboard/index.html")
    billboards = BillBoard.objects.order_by("-published")
    context = {"billboards": billboards}
    return HttpResponse(template.render(context, request))
