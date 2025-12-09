from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Blog, Contact, Service

# Create your views here.

def home(request):
    """Home page view"""
    recent_blogs = Blog.objects.filter(published=True)[:3]
    services = Service.objects.filter(is_active=True).order_by('order')
    context = {
        'recent_blogs': recent_blogs,
        'services': services,
    }
    return render(request, 'main/home.html', context)


def blog_list(request):
    """Blog list view"""
    blogs = Blog.objects.filter(published=True)
    context = {
        'blogs': blogs,
    }
    return render(request, 'main/blog_list.html', context)


def blog_detail(request, slug):
    """Blog detail view"""
    blog = get_object_or_404(Blog, slug=slug, published=True)
    context = {
        'blog': blog,
    }
    return render(request, 'main/blog_detail.html', context)


def contact(request):
    """Contact form view"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'main/home.html')


