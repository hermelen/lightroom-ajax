# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.http import JsonResponse

from .models import Light
from .forms import LightForm

# Create your views here.

class LightListView(ListView):
    model = Light

    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)

        context['lights'] = []
        for light in self.get_queryset():
            context['lights'].append({
                'light': light,
                'form' : LightForm(instance=light)
                # 'form' : LightForm(prefix="select-%s" % light.id, instance=light)
            })

        return context


class LightSwitchView(UpdateView):
    model = Light
    fields = "__all__"

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({
            'id': self.object.id,
            'status': self.object.status
        })
