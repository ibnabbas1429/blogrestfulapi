from django.shortcuts import render
from .models import Blog
from .forms import BlogForm

# Create your views here.

def create_view(request):
    context = {}
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
    context["form"] = form
    return render(request, "create_view.html", context)