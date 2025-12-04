import os
import django
import shutil
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog

# England vs China Football Blog Content
football_blog = {
    'title': "England's women's football team secured a commanding 8-0 victory over China",
    'slug': 'england-women-football-china-victory',
    'excerpt': "England's women's football team secured a commanding 8-0 victory over China in a highly anticipated international friendly at Wembley Stadium, marking yet another milestone in the growth of women's football.",
    'content': """<div class="blog-content-3d">
<div class="intro-section">
<p class="lead-paragraph">England's women's football team secured a commanding 8-0 victory over China in a highly anticipated international friendly at Wembley Stadium, marking yet another milestone in the growth of women's football. The match, played in front of a full-capacity crowd, highlighted not only the brilliance on the pitch but also the ever-expanding popularity of the women's game.</p>
</div>

<div class="content-section">
<h2 class="section-heading">Dominant Display from the Start</h2>
<p>From the first whistle, the Lionesses dominated possession, asserting their superiority with clinical precision. The opening goal came in the 23rd minute, when England's star forward, Beth England, drilled a powerful strike past China's goalkeeper, Zhu Yu, after a brilliant through ball from midfielder Ella Toone. The early goal set the tone for the match, as England controlled the tempo and created multiple scoring opportunities.</p>
<p>China, under the guidance of their coach Shui Qingxia, struggled to cope with the pace and technicality of the English side. Despite a few promising counter-attacks, they failed to break down the solid defensive partnership of Millie Bright and Alex Greenwood. England doubled their lead just before the break when Lauren Hemp, widely regarded as one of the brightest talents in women's football, slotted home from close range following a rebound off the post.</p>
</div>

<div class="content-section">
<h2 class="section-heading">Second Half Domination</h2>
<p>In the second half, the Chinese team showed resilience but could not keep up with the intensity of the hosts. Lucy Bronze, a standout performer for England, delivered a pinpoint cross to Georgia Stanway, whose header in the 72nd minute sealed the win and sent the Wembley crowd into raptures.</p>
<p>The match was a testament to the growing stature of women's football, underscored by the record-breaking attendance at Wembley. The sold-out crowd of over 90,000 spectators reflected a broader trend of increasing fan engagement and financial investment in women's sports. This, combined with recent successes in international tournaments, has seen the women's game rise exponentially in terms of both visibility and professionalism.</p>
</div>

<div class="content-section">
<h2 class="section-heading">A Rising Powerhouse</h2>
<p>England's victory over China at Wembley is a poignant reminder of how far the sport has come, with many crediting the rise of women's football to strategic efforts in grassroots development, better media coverage, and corporate sponsorship. The match demonstrated that women's football is no longer a niche sport but a global powerhouse capable of attracting the world's attention.</p>
</div>

<div class="content-section finale-section">
<h2 class="section-heading">The Future Looks Bright</h2>
<p>With the 2027 FIFA Women's World Cup on the horizon, the future of women's football has never looked brighter. England's comprehensive win and the continued support of fans around the world make it clear: this is just the beginning of a new chapter in the sport's history.</p>
</div>
</div>""",
    'author': 'Khushi Deshmukh',
}

# Copy the thumbnail image to media/blog_images/
thumbnail_source = Path('/Users/vinayadusumilli/.gemini/antigravity/brain/53cc66c4-c5ee-46b8-b146-51a7737f6ad2/england_china_football_1764805486181.png')
media_dir = Path('/Users/vinayadusumilli/website/media/blog_images')
media_dir.mkdir(parents=True, exist_ok=True)
thumbnail_dest = media_dir / 'england_china_football.png'

# Copy the image
if thumbnail_source.exists():
    shutil.copy2(thumbnail_source, thumbnail_dest)
    print(f"✓ Thumbnail image copied to {thumbnail_dest}")
    football_blog['image'] = 'blog_images/england_china_football.png'
else:
    print(f"! Thumbnail source not found at {thumbnail_source}, blog will be created without image")

# Create or update the blog post
blog, created = Blog.objects.update_or_create(
    slug=football_blog['slug'],
    defaults=football_blog
)

if created:
    print(f"✓ Successfully created blog: {blog.title}")
else:
    print(f"✓ Successfully updated blog: {blog.title}")

print(f"  - Slug: {blog.slug}")
print(f"  - Author: {blog.author}")
print(f"  - Image: {blog.image}")
print(f"  - Published: {blog.published}")
print(f"\n🎉 England vs China blog is now live on your website!")
