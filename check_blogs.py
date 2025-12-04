import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog

blogs = Blog.objects.all()
for blog in blogs:
    print(f"Title: {blog.title}")
    print(f"Slug: {blog.slug}")
    print(f"Content Start: {blog.content[:100]}...")
    print("-" * 20)
