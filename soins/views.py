from django.views import generic
from django.utils import translation
from django.utils.translation import ugettext as _

from .models import Care, Family_Care

class Index(generic.ListView):
    model = Care
    context_object_name = "cares"
    template_name = 'index.html'
    
    def get_queryset(self):
        queryset = Care.objects.order_by('display_order')
        return queryset

    def get_context_data(self, **kwargs):
       
        # user_language = translation.get_language()
        # translation.activate(user_language)
        # self.request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        # family 1
        context = super().get_context_data(**kwargs)
        context['cares_1'] = Care.objects.order_by('display_order').filter(family_id=1)
        context['family_1'] = Family_Care.objects.get(id=1).name
        context['family_1_it'] = Family_Care.objects.get(id=1).name_it
        # family 2
        context['cares_2'] = Care.objects.order_by('display_order').filter(family_id=2)
        context['family_2'] = Family_Care.objects.get(id=2).name
        context['family_2_it'] = Family_Care.objects.get(id=2).name_it
        # family 3
        context['cares_3'] = Care.objects.order_by('display_order').filter(family_id=3)
        context['family_3'] = Family_Care.objects.get(id=3).name
        context['family_3_it'] = Family_Care.objects.get(id=3).name_it
        # family 4
        context['cares_4'] = Care.objects.order_by('display_order').filter(family_id=4)
        context['family_4'] = Family_Care.objects.get(id=4).name
        context['family_4_it'] = Family_Care.objects.get(id=4).name_it
        return context