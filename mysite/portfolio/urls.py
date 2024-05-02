from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home, name='home'),
    path('academics', views.academics, name='academics'),
    path('professional', views.professional, name='professional'),

    path('blog', views.blog, name='blog'),
    path('my-blog/<int:id>', views.my_blog, name='my-blog'),
    path('blog-detail/<int:id>', views.blog_detail, name='blog-detail'),
    path('portfolio-detail/<int:id>', views.portfolio_detail, name='portfolio-detail'),
    path('web-services', views.web_services, name='web-services'),
    path('mobile-services', views.mobile_services, name='mobile-services'),
    path('desktop-services', views.desktop_services, name='desktop-services'),

    path('feedback', views.feedback, name='feedback'),

]
