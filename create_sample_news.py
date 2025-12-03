#!/usr/bin/env python
"""
Script to create sample news articles for the portfolio website.
Run this with: python create_sample_news.py
"""

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import News
from django.utils.text import slugify

# Sample news data
news_data = [
    {
        'title': 'IPL 2025: Record-Breaking Broadcasting Deal Announced',
        'slug': 'ipl-2025-broadcasting-deal',
        'excerpt': 'The Indian Premier League announces a groundbreaking broadcasting partnership that sets new records in sports media.',
        'content': '''The Indian Premier League (IPL) has announced a historic broadcasting deal that marks a new era in sports media partnerships. This landmark agreement is set to revolutionize how cricket fans experience the game.

The multi-year deal encompasses digital streaming rights, television broadcasting, and international distribution, making it one of the most comprehensive sports media agreements in history.

Industry experts predict this partnership will significantly enhance fan engagement through innovative viewing experiences and exclusive content offerings.

This development underscores the growing commercial value of cricket as a global sport and the IPL's position as one of the world's premier sporting leagues.'''
    },
    {
        'title': 'Women\'s Sports Marketing Sees Unprecedented Growth',
        'slug': 'womens-sports-marketing-growth',
        'excerpt': 'New research reveals exponential growth in women\'s sports marketing investments and fan engagement across multiple platforms.',
        'content': '''A comprehensive industry report has revealed unprecedented growth in women\'s sports marketing, with investments increasing by over 300% in the past three years.

Major brands are recognizing the immense potential of women\'s sports, leading to historic sponsorship deals and media partnerships. The Women\'s Premier League (WPL) has played a pivotal role in this transformation.

Fan engagement metrics show remarkable increases across social media platforms, with younger demographics showing particular interest in women\'s cricket and other sports.

This shift represents not just a trend but a fundamental change in how the sports industry approaches marketing and audience development.

Experts predict continued exponential growth as more brands recognize the authentic connection that women athletes create with diverse audiences.'''
    },
    {
        'title': 'Digital Innovation Transforms Sports Communication',
        'slug': 'digital-innovation-sports-communication',
        'excerpt': 'Emerging technologies are reshaping how sports organizations communicate with fans and stakeholders in real-time.',
        'content': '''The sports communication landscape is undergoing a dramatic transformation driven by digital innovation and emerging technologies.

Virtual reality experiences, augmented reality features, and interactive platforms are creating unprecedented levels of fan engagement. Sports organizations are leveraging these technologies to build deeper connections with their audiences.

Social media strategies have evolved beyond simple posting to include live streaming, behind-the-scenes content, and direct athlete-fan interactions. This evolution has made sports communication more immediate and personal than ever before.

Data analytics are playing an increasingly important role in crafting targeted communication strategies that resonate with specific fan segments.

The integration of artificial intelligence in content creation and distribution is opening new possibilities for personalized fan experiences at scale.'''
    },
]

def create_news():
    """Create sample news articles"""
    print("Creating sample news articles...")
    
    for news_item in news_data:
        news, created = News.objects.get_or_create(
            slug=news_item['slug'],
            defaults={
                'title': news_item['title'],
                'content': news_item['content'],
                'excerpt': news_item['excerpt'],
                'author': 'Khushi Deshmukh',
                'published': True,
            }
        )
        
        if created:
            print(f"✓ Created: {news.title}")
        else:
            print(f"→ Already exists: {news.title}")
    
    print(f"\nTotal news articles in database: {News.objects.count()}")
    print("\nDone! Visit http://127.0.0.1:8001/news/ to see your news articles.")

if __name__ == '__main__':
    create_news()
