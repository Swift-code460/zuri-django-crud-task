from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Post

# Create your views here
 
class PostListView(ListView):
 
    # specify the model for list view
    model = Post
    
class PostCreateView(CreateView):
 
    # specify the model for create view
    model = Post
 
    # specify the fields to be displayed
 
    fields = "__all__"

    success_url  = reverse_lazy("blog:all")
    
class PostDetailView(DetailView):
  
    model = Post
    
class PostUpdateView(UpdateView):
  
    model = Post
    
    fields = "__all__"
    
    success_url = reverse_lazy("blog:all")
    
class PostDeleteView(DeleteView):
  
    model = Post

    fields = "__all__"

    success_url  = reverse_lazy("blog:all")
    