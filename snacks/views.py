from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, CreateView , ListView, DetailView
from .models import Snack
from django.urls import reverse_lazy

class snack_listView(ListView):
    template_name='snack_list.html'
    model=Snack
    context_object_name = "Snacks"
class snack_detailView(DetailView):
    template_name='snack_detail.html'
    model=Snack

class SnackCreateView(CreateView):
    template_name='snack_create.html'
    model=Snack
    fields= "__all__"

class SnackUpdateView(UpdateView):
    template_name='snack_update.html'
    model=Snack
    fields="__all__"
    success_url=reverse_lazy('snack_list')

    

class SnackDeleteView(DeleteView):
    template_name='snack_delete.html'
    model=Snack
    success_url=reverse_lazy('snack_list')