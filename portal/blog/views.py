from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from .models import Post, Category

def post_list(request):
	return render_to_response('portal/blog.html', {'posts': Post.objects.all()})

def post_detail(request, slug):
	return render_to_response('portal/post_detail.html', {'post': get_object_or_404(Post, slug=slug)})
