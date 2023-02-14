from django.db.models import Count

from .models import *


class DataMixin():
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
