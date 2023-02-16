from django.db.models import Count
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect

from .models import *
from .forms import SearchBarForm


class DataMixin(FormMixin):
    paginate_by = 8

    def get_user_context(self, **kwargs):
        context = kwargs
        context['types'] = Type.objects.annotate(Count('product')).order_by('name')
        context['brands'] = Brand.objects.annotate(Count('product')).order_by('name')
        if 'type_selected' not in context:
            context['type_selected'] = 0
        if 'brand_selected' not in context:
            context['brand_selected'] = 0
        return context


class SearchMixin(FormMixin):
    form_class = SearchBarForm
    def post(self, request, *, object_list=None, **kwargs):
        return redirect('search', request.POST['search_query'])