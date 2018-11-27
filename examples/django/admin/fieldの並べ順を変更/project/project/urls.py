from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'サンプルアプリケーションだよーん' #もともとは「Django管理サイト」
admin.site.index_title = 'メニューだよーん'#もともとは「管理サイト」
admin.site.site_title="タイトルタグだよーん"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/",include("app.urls")),
    #ajaxは本編に関係ない
    path("ajax/", include("ajax.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

