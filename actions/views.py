from datetime import datetime

from django.http import HttpResponseRedirect
from django.views import generic

from .forms import ActionForm
from .models import Action


class ActionListView(generic.ListView):
    model = Action
    context_object_name = 'actions'

    def get_queryset(self):
        return Action.objects.filter(deleted=False)


class ActionDetailView(generic.DetailView):
    model = Action
    context_object_name = 'action'


class ActionEditView(generic.UpdateView):
    model = Action
    form_class = ActionForm
    context_object_name = 'action'
    template_name = 'actions/action_create.html'


class ActionCreateView(generic.CreateView):
    form_class = ActionForm
    context_object_name = 'action'
    template_name = 'actions/action_create.html'


class ActionDoneView(generic.DetailView):
    model = Action

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.completed is None:
            obj.completed = None
        else:
            obj.completed = datetime.now()
        obj.save()
        redirect_url = request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(redirect_url)


class ActionDeleteView(generic.DetailView):
    model = Action

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.deleted = not obj.deleted
        obj.save()
        redirect_url = request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(redirect_url)
