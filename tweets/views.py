from django.shortcuts import render,redirect,reverse
from tweets.models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def all_tweets(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    context = {
        "tweets" : tweets,
    }
    return render(request, 'twitter_official.html', context=context)


def add_tweet(request):
    if not request.user.is_authenticated:
        return redirect(reverse("admin:login"))
    if request.method == "POST":
        content  = request.POST['content']
        data = Tweet(content=content)
        data.author = request.user
        data.save()
        return redirect(reverse("tweets"))
    return render(request, '404_error.html')

def view_author_tweets(request, author_id):
    if not request.user.is_authenticated:
        return redirect(reverse("admin:login"))
    tweets = Tweet.objects.filter(author_id=author_id).order_by('-created_at')
    context = {
        "tweets" : tweets
    }
    return render(request, "author_tweets.html", context=context)

