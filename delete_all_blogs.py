import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog

# Count before deletion
count = Blog.objects.count()
print(f"Found {count} blog posts.")

# Delete all blogs
Blog.objects.all().delete()

# Verify
remaining = Blog.objects.count()
print(f"Deleted {count} blog posts. Remaining: {remaining}")
