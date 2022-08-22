# from django.shortcuts import render, redirect, reverse
# from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .forms import NewPostForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-date_time_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreatView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/post_create.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')


# def post_list_view(request):
#     posts_list = Post.objects.filter(
#         status='pub').order_by('-date_time_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})


# def post_create_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post_list')

#     else:
#         form = NewPostForm()
#     return render(request, 'blog/post_create.html', context={'form': form})


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)

#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
#     return render(request, 'blog/post_create.html', context={'form': form})


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     if request.method == 'POST':
#         print("step 2")
#         post.delete()
#         return redirect('post_list')

#     return render(request, 'blog/post_delete.html', context={'post': post})
