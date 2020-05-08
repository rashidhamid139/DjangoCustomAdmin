from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from .models import Post, City, Photo
from .forms import PostForm, PhotoForm
from django.db.models import Q
from django.http import JsonResponse
from django.views import View



class HomePageView(ListView):
    model = Post
    template_name = 'post_home.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('post_phome')


class CityPageView(TemplateView):
    template_name = 'cityhome.html'


class SearchResultView(ListView):
    model = City
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(name__icontains=query)|Q(state__icontains=query)
        )
        return object_list



class StaticPageView(TemplateView):
    template_name = 'static.html'


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/basic_upload/index.html', {'photos': photos_list})


    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)