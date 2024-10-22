from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy



class HomePageView(TemplateView):
    model= Post
    template_name = "home.html"
    content_object_name = 'home'

class TADeleteView(DeleteView):
    model = Post
    template_name = "ta_delete.html"
    success_url = reverse_lazy("home")

class TAListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'posts'

class TADetailView(DetailView):
    model = Post
    template_name = "ta_detail.html"

class TACreateView(CreateView):
    model = Post
    template_name = "ta_new.html"
    fields = ["title", "author", "body"]


class TAUpdateView(UpdateView):
    model = Post
    template_name = "ta_edit.html"
    fields = ["title", "body"]