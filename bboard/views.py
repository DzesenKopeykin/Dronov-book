from django.http import HttpResponse

from .models import BillBoard


def index(request):
    response = "Список объявлений\n\n\n"
    for bill_board in BillBoard.objects.order_by("-published"):
        response += f"{bill_board.title}\n{bill_board.content}\n\n"
    return HttpResponse(response, content_type="text/plain; charset=utf-8")
