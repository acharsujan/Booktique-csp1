
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from books.views import home, create_post,post_page, signin, signup, signout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('create/', create_post),
    path('signin/',signin),
    path('signout/',signout),
    path('signup/',signup),

    path('post/<int:post_id>/', post_page), 
] 
