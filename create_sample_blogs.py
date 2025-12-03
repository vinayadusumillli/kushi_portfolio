import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog

# Create sample blog posts
blogs = [
    {
        'title': 'The Rise of Women in Sports Communications',
        'slug': 'rise-of-women-sports-communications',
        'excerpt': 'Exploring the growing opportunities and challenges for women in the sports communications industry.',
        'content': '''
The sports communications landscape is evolving rapidly, and women are at the forefront of this transformation. From IPL franchises to international motorsport events, women professionals are breaking barriers and redefining what it means to work in sports media and communications.

In my journey from working with the Gujarat Titans during their championship season to managing communications for motorsport events, I've witnessed firsthand how the industry is becoming more inclusive and diverse. This shift isn't just about representation—it's about bringing fresh perspectives and innovative approaches to sports storytelling.

The key to success in this field lies in understanding both the technical aspects of communications and the passionate culture of sports. It's about crafting narratives that resonate with fans while maintaining the integrity and authenticity that sports audiences demand.

As more women enter this field, we're seeing a richer, more nuanced approach to sports communications that benefits everyone—from teams and athletes to fans and sponsors.
        ''',
        'author': 'Khushi Deshmukh',
    },
    {
        'title': 'Behind the Scenes: IPL Social Media Strategy',
        'slug': 'behind-scenes-ipl-social-media-strategy',
        'excerpt': 'An insider\'s look at how IPL teams create engaging content that connects with millions of fans.',
        'content': '''
Working with the Gujarat Titans during their inaugural season gave me a unique perspective on IPL social media strategies. The key to success in this fast-paced environment is understanding that you're not just promoting a team—you're building a community.

Every piece of content needs to serve multiple purposes: engaging existing fans, attracting new supporters, and creating shareable moments that extend the team's reach. During match days, we operated on tight schedules, creating real-time content that captured the excitement of the game while maintaining the team's brand voice.

The most successful campaigns always had one thing in common: authenticity. Fans can tell when content is genuine versus when it's manufactured. Behind-the-scenes moments, player personalities, and real emotions always performed better than polished marketing materials.

Social media in sports isn't just about numbers—it's about creating memorable experiences that fans want to be part of. That's what makes this work so rewarding.
        ''',
        'author': 'Khushi Deshmukh',
    },
    {
        'title': 'Why Sports Management Education Matters',
        'slug': 'why-sports-management-education-matters',
        'excerpt': 'Reflecting on my academic journey and how formal education shaped my career in sports.',
        'content': '''
When I started my undergraduate degree in Sport Management, I wasn't entirely sure where it would lead. Now, pursuing my Masters in Sport Business and Innovation at Loughborough University London, I can confidently say that structured education in this field is invaluable.

Sports management education provides more than just theoretical knowledge—it offers frameworks for understanding the complex ecosystem of modern sports. From business analytics to marketing strategies, from event management to athlete representation, the field is incredibly diverse.

My academic background gave me the confidence to approach opportunities with organizations like Decathlon, the Gujarat Titans, and various motorsport entities. It taught me to think critically about industry trends and to bring data-driven insights to creative challenges.

The connections I made during my studies—with professors, industry professionals, and fellow students—continue to open doors and create opportunities. In an industry that's all about networking and relationships, that educational foundation has proven invaluable.

For anyone considering a career in sports, I highly recommend investing in proper education. The industry is becoming increasingly sophisticated, and having that academic grounding will set you apart.
        ''',
        'author': 'Khushi Deshmukh',
    },
]

for blog_data in blogs:
    blog, created = Blog.objects.get_or_create(
        slug=blog_data['slug'],
        defaults=blog_data
    )
    if created:
        print(f"Created blog: {blog.title}")
    else:
        print(f"Blog already exists: {blog.title}")

print("\nSample blogs created successfully!")
