from django.shortcuts import get_object_or_404, render

from .models import Post


def post_detail(request, pk):
    post = get_object_or_404(Post.objects.select_related("author"), pk=pk)
    return render(request, "discuss/post_detail.html", {"post": post})
