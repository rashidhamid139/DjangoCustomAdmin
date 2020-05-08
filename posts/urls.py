from django.urls import path
from .views import HomePageView, CreatePostView, CityPageView, SearchResultView, StaticPageView, BasicUploadView
app_name='posts'
urlpatterns = [
    path('', HomePageView.as_view(), name='post_home'),
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('cityhome', CityPageView.as_view(), name='cityhome'),
    path('search/', SearchResultView.as_view(), name='search'),
    path('static/', StaticPageView.as_view(), name='static'),
    path('basic_upload/', BasicUploadView.as_view(), name='basic_upload'),
]