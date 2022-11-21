from django.contrib import admin
from django.urls import path
from users import views as userviews
from django.conf import settings
from django.conf.urls.static import static
from rent import views as rentviews

urlpatterns = [
    path('admin/', admin.site.urls),
    #Auth
    path('signup/', userviews.signupuser, name = 'signupuser'),
    path('login/', userviews.loginuser, name = 'loginuser'),
    path('logout/', userviews.logoutuser, name = 'logoutuser'),
    #Main
    path('', rentviews.home, name = 'home'),
    path('createorder/', rentviews.createOrder, name = 'createorder'),
    path('vieworder/<int:order_id>', rentviews.vieworder, name = 'vieworder'),
    path('myorders/<int:user_id>', rentviews.myorders, name = 'myorders'),
    path('isarendated/<int:user_id>/<int:order_id>', rentviews.isarendated, name = 'isarendated'),
    path('isnotarendated/<int:user_id>/<int:order_id>', rentviews.isnotarendated, name = 'isnotarendated'),
    path('deleteorder/<int:user_id>/<int:order_id>', rentviews.deleteorder, name = 'deleteorder'),
    path('deletecomment/<int:comment_id>', rentviews.deletecomment, name = 'delelecomment')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)