from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Homepage"),
    path('aboutus',views.aboutus_view,name="aboutus"),
    path('accounts/',include('accounts.urls')),
    path('blog/',include('blog.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

