import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog

slug = 'brand-visibility-f1-circuit-tracks'
try:
    blog = Blog.objects.get(slug=slug)
    print(f"Title: {blog.title}")
    print("Content:")
    print(blog.content)
except Blog.DoesNotExist:
    print(f"Blog with slug {slug} not found.")
