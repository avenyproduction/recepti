from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from recepti_app.models import Problem,Trava,Recepti

# Create your views here.
class receptiView(TemplateView):
    template_name = 'recepti_app/index.html'

class problemListView(ListView):
    model = Problem

class traveList(ListView):
    context_object_name = 'trave_list'
#    queryset = Trava.objects.filter(problem__problem="Antiseptik")
    template_name = 'recepti_app/trava_list.html'
    model = Trava

    def get_context_data(self, **kwargs):
        context = super(traveList, self).get_context_data(**kwargs)
        context['problem']=Trava.objects.filter(problem=self.kwargs['pk'])
        return context

class receptDetail(DetailView):
    model = Recepti
