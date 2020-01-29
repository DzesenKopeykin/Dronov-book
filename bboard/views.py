from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import AdForm
from .models import Ad, Rubric


def index(request):
    ads = Ad.objects.all()
    rubrics = Rubric.objects.all()
    context = {"ads": ads, "rubrics": rubrics}
    return render(request, "bboard/index.html", context)


def by_rubric(request, rubric_id):
    ads = Ad.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = rubrics.get(pk=rubric_id)
    context = {"ads": ads, "rubrics": rubrics, "current_rubric": current_rubric}
    return render(request, "bboard/by_rubric.html", context)


class AdCreateView(CreateView):
    template_name = "bboard/create.html"
    form_class = AdForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rubrics"] = Rubric.objects.all()
        return context
