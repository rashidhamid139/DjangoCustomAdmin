from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm


class HomePageView(ListView):
    model = Post
    template_name = 'post_home.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('post_home')

