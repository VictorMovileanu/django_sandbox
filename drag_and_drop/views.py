from django.shortcuts import get_object_or_404
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
    data = request.POST
    category = Category.objects.get(pk=pk)
    if request.POST.get("model", None) == "link":
        # TODO: `link` should be held in a global variable, supplied by e.g. context processors in templates
        link = get_object_or_404(Link, pk=data.get('pk', None))
        link.category = category
        link.save()
    return TemplateResponse(request, "partials/category.html", context={"category": category})
