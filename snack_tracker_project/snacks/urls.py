from django.urls.resolvers import URLPattern
from .views import HomePageView , BlogDetailsView
from django.urls import path 



urlpatterns=[
    path('' , HomePageView.as_view() , name='home'),
    path('blog/<int:pk>' , BlogDetailsView.as_view() , name='post_detail')
]