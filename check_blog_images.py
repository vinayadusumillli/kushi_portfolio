import os
import django
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog
from django.conf import settings

print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
print(f"MEDIA_URL: {settings.MEDIA_URL}")
print("-" * 50)

blogs = Blog.objects.all()
for blog in blogs:
    print(f"Title: {blog.title}")
    print(f"Image Field Value: {blog.image}")
    if blog.image:
        full_path = settings.MEDIA_ROOT / str(blog.image)
        exists = full_path.exists()
        print(f"Full Path: {full_path}")
        print(f"Exists: {exists}")
        try:
            print(f"URL: {blog.image.url}")
        except Exception as e:
            print(f"URL Error: {e}")
    else:
        print("No image set")
    print("-" * 50)
