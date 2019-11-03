from django.template.response import TemplateResponse
from django.views.generic import TemplateView

from drag_and_drop.models import Category, Link


class IndexView(TemplateView):
    template_name = 'index.html'


class DndView(TemplateView):
    template_name = 'dnd_files.html'


class DndObjectsView(TemplateView):
    template_name = 'dnd_objects.html'
    extra_context = {'categories': Category.objects.all(), 'links': Link.objects.all()}


def add_link_to_category(request, pk):
    category = Category.objects.get(pk=pk)
    return TemplateResponse(request, "partials/category.html", context={"category": category})
