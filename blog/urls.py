from django.urls import path
from blog.views import *

urlpatterns = [
    path('', index),
    path("post/<slug>/", post_detail, name="blog-post-detail")
]