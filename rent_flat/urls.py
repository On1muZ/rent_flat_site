from django.contrib import admin
from django.urls import path
from users import views as userviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #Auth
    path('signup/', userviews.signupuser, name = 'signupuser'),
    path('login/', userviews.loginuser, name = 'loginuser'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)