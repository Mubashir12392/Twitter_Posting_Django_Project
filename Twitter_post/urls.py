"""Twitter_post URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from tweets.views import add_tweet, all_tweets, view_author_tweets


def home_redirect(request):
    from django.shortcuts import redirect, reverse
    return redirect(reverse('tweets'))


urlpatterns = [
    path("", home_redirect),
    path("admin/", admin.site.urls),
    path("dj/tweets/", all_tweets, name="tweets"),
    path("dj/tweets/add", add_tweet, name="add-tweet"),
    path("dj/tweets/view/<int:author_id>",
         view_author_tweets, name="view-author")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)