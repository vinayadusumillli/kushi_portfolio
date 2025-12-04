import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog

slug = 'england-triumph-over-china-in-sold-out-wembley-clash-a-new-era-for-womens-football'
try:
    blog = Blog.objects.get(slug=slug)
    print(f"Title: {blog.title}")
    print(f"Image: {blog.image}")
    print("Content:")
    print(blog.content[:200]) # Just check the start
except Blog.DoesNotExist:
    print(f"Blog with slug {slug} not found.")
