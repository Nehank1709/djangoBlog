from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    all_posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(all_posts)
    return render(request, 'post_list.html', {'all_posts': all_posts})
