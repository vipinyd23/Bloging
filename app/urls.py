from django.contrib import admin
from django.urls import path
from. import views
from .views import home, post,category
urlpatterns = [
    # path("admin/", admin.site.urls),
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('post/',views.post,name="postitem"),
    path('category/<slug:url>',category),
    path('blog/<slug:url>', post)
]
