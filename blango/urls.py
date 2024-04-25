from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from django.conf import settings
import blog.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(blog.urls))
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
