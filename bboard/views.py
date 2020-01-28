from django.shortcuts import render

from .models import Ad, Rubric


def index(request):
    ads = Ad.objects.all()
    return render(request, "bboard/index.html", {"ads": ads})


def by_rubric(request, rubric_id):
    ads = Ad.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = rubrics.get(pk=rubric_id)
    context = {"ads": ads, "rubrics": rubrics, "current_rubric": current_rubric}
    return render(request, "bboard/by_rubric.html", context)
