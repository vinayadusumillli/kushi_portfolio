import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog

slug = 'england-women-football-china-victory'
try:
    blog = Blog.objects.get(slug=slug)
    blog.delete()
    print(f"✓ Successfully deleted duplicate blog: {blog.title}")
except Blog.DoesNotExist:
    print(f"Blog with slug {slug} not found.")
