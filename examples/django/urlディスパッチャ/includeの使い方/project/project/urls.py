from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#同じapp.urlsを指定している場合、警告が出る場合があるが、
#namespaceを別々に設定することで回避できる。
urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/",include("app.urls",namespace="short"),),
    path("app/<int:value2>/", include("app.urls", namespace="long"), {"value":123}, ),
    #ajaxは本編に関係ない
    path("ajax/", include("ajax.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

