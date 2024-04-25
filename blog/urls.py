from django.urls import path
from blog.views import *

urlpatterns = [
    path('', index),
    path("post/<slug>/", post_detail, name="blog-post-detail"),
    path("ip/", get_ip)
]

from django.conf import settings
print(f"Time zone: {settings.TIME_ZONE}")