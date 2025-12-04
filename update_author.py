import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog

# Update all blogs to have the new author
updated_count = Blog.objects.update(author='Khushi Deshmukh')

print(f"✓ Successfully updated author to 'Khushi Deshmukh' for {updated_count} blog posts.")

# Verify
for blog in Blog.objects.all():
    print(f"- {blog.title}: {blog.author}")
