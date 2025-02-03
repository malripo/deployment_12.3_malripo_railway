"""a_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from a_posts.views import home_view
from a_posts.views import *
from a_users.views import *
# for media
from django.conf import settings
from django.conf.urls.static import static

# for Sitemaps
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from a_posts.sitemaps import *

sitemaps = {
    'static' : StaticSitemap,
    'categories' : CategorySitemap,
    'postpages' : PostpageSitemap
}

urlpatterns = [
    # for Sitemaps
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),   
    # for theboss
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # path('admin/', admin.site.urls),
    path('theboss/', admin.site.urls),
    # for allauth
    path('accounts/', include('allauth.urls')),
    path('', home_view, name='home'),
    path('category/<tag>/', home_view, name='category'),
    path('post/create/', post_create_view, name='post-create'),
    path('post/delete/<pk>/', post_delete_view, name='post-delete'),
    path('post/edit/<pk>/', post_edit_view, name='post-edit'),
    path('post/<pk>/', post_page_view, name='post'),
    path('post/like/<pk>/', like_post, name="like-post"), 
    path('comment/like/<pk>/', like_comment, name="like-comment"), 
    path('reply/like/<pk>/', like_reply, name="like-reply"),
    # path('category/<tag>/', category_view, name='category'),
    path('profile/', profile_view, name="profile"),
    path('_/', include('a_landingpages.urls')), 
    path('<username>/', profile_view, name="userprofile"),
    path('<username>/', profile_view, name="userprofile"),  
    path('profile/edit/', profile_edit_view, name="profile-edit"),
    path('profile/delete/', profile_delete_view, name="profile-delete"),
    path('profile/onboarding/', profile_edit_view, name="profile-onboarding"),
    path('profile/verify-email/', profile_verify_email, name="profile-verify-email"),
    path('commentsent/<pk>/', comment_sent, name="comment-sent"),
    path('comment/delete/<pk>/', comment_delete_view, name='comment-delete'),  
    path('replysent/<pk>/', reply_sent, name='reply-sent'),
    path('replyform/<pk>/', reply_form, name='reply-form'),  
    path('reply/delete/<pk>/', reply_delete_view, name='reply-delete'),  
]
# for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
