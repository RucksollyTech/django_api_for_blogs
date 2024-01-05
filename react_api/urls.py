from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from react_app_api.views import home,blogs,blog_detail,create_blog
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/blogs', blogs),
    path('api/create_blog', create_blog),
    path('api/blog_detail/<str:pk>', blog_detail),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
