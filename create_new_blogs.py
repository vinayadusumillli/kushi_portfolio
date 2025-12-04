import os
import django
from pathlib import Path
import shutil

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog

# Common author
AUTHOR = 'Khushi Deshmukh'

# Define blogs
blogs_data = [
    {
        'title': "England Triumph Over China in Sold-Out Wembley Clash: A New Era for Women's Football",
        'slug': 'england-triumph-china-wembley',
        'excerpt': "England’s women’s football team secured a commanding 8-0 victory over China in a highly anticipated international friendly at Wembley Stadium.",
        'image_source': 'england_china_cover.png',
        'content': """<p>England’s women’s football team secured a commanding 8-0 victory over China in a highly anticipated international friendly at Wembley Stadium, marking yet another milestone in the growth of women’s football. The match, played in front of a full-capacity crowd, highlighted not only the brilliance on the pitch but also the ever-expanding popularity of the women’s game.</p>

<h2>Dominant Display</h2>
<p>From the first whistle, the Lionesses dominated possession, asserting their superiority with clinical precision. The opening goal came in the 23rd minute, when England's star forward, Beth England, drilled a powerful strike past China’s goalkeeper, Zhu Yu, after a brilliant through ball from midfielder Ella Toone. The early goal set the tone for the match, as England controlled the tempo and created multiple scoring opportunities.</p>
<p>China, under the guidance of their coach Shui Qingxia, struggled to cope with the pace and technicality of the English side. Despite a few promising counter-attacks, they failed to break down the solid defensive partnership of Millie Bright and Alex Greenwood. England doubled their lead just before the break when Lauren Hemp, widely regarded as one of the brightest talents in women’s football, slotted home from close range following a rebound off the post.</p>

<h2>Second Half Domination</h2>
<p>In the second half, the Chinese team showed resilience but could not keep up with the intensity of the hosts. Lucy Bronze, a standout performer for England, delivered a pinpoint cross to Georgia Stanway, whose header in the 72nd minute sealed the win and sent the Wembley crowd into raptures.</p>
<p>The match was a testament to the growing stature of women’s football, underscored by the record-breaking attendance at Wembley. The sold-out crowd of over 90,000 spectators reflected a broader trend of increasing fan engagement and financial investment in women’s sports. This, combined with recent successes in international tournaments, has seen the women's game rise exponentially in terms of both visibility and professionalism.</p>

<h2>A Rising Powerhouse</h2>
<p>England’s victory over China at Wembley is a poignant reminder of how far the sport has come, with many crediting the rise of women’s football to strategic efforts in grassroots development, better media coverage, and corporate sponsorship. The match demonstrated that women’s football is no longer a niche sport but a global powerhouse capable of attracting the world’s attention.</p>

<h2>The Future Looks Bright</h2>
<p>With the 2027 FIFA Women’s World Cup on the horizon, the future of women’s football has never looked brighter. England's comprehensive win and the continued support of fans around the world make it clear: this is just the beginning of a new chapter in the sport’s history.</p>"""
    },
    {
        'title': "Qatar 2025 Race Highlights",
        'slug': 'qatar-2025-race-highlights',
        'excerpt': "The 2025 Qatar Grand Prix dramatically reshaped the title race, transforming what seemed like a comfortable lead for Lando Norris into a tense three-way battle.",
        'image_source': 'qatar_highlights.png',
        'content': """<p>The 2025 Qatar Grand Prix dramatically reshaped the title race, transforming what seemed like a comfortable lead for Lando Norris into a tense three-way battle for the championship. Max Verstappen took victory, finishing ahead of Oscar Piastri and Carlos Sainz, while Norris could only manage fourth. With just 12 points separating Norris and Verstappen, and Piastri still in the hunt, the stage is set for an electrifying Abu Dhabi finale.</p>

<h2>Turning Point</h2>
<p>The race’s turning point came during a Safety Car period on lap seven. Red Bull quickly pitted Verstappen, while McLaren chose to leave both Norris and Piastri out. This decision, intended to preserve track position, backfired when Pirelli's tyre limits forced McLaren into a double pit stop later, while Verstappen and others only needed one. The strategy mistake cost McLaren dearly, and Verstappen took full advantage to regain the momentum in the title fight.</p>

<h2>Strategic Misstep</h2>
<p>McLaren’s decision was widely criticized, with many analysts calling it a rare strategic misstep. Andrea Stella, McLaren’s team principal, admitted it was the wrong call, acknowledging that “hindsight makes it clear we should have pitted with the others.” Despite the setback, Piastri’s strong second-place finish showed McLaren's pace, and Norris remains in the title hunt, though under immense pressure.</p>

<h2>Title Race Wide Open</h2>
<p>Verstappen’s win has revived his championship challenge, and with Piastri also in contention, the title race has been thrown wide open. Norris, once comfortably ahead, must now defend his slim lead in the final race. The 2025 season finale promises to be one of the most dramatic and closely contested in recent memory, with everything on the line.</p>"""
    },
    {
        'title': "McLaren's Pitstop Gamble: A Costly Mistake at the 2025 Qatar Grand Prix",
        'slug': 'mclaren-pitstop-gamble-qatar-2025',
        'excerpt': "The 2025 Qatar Grand Prix was a pivotal moment in the Formula 1 season, not just for its on-track drama, but for a strategic blunder that could haunt McLaren.",
        'image_source': 'mclaren_pitstop.png',
        'content': """<p>The 2025 Qatar Grand Prix was a pivotal moment in the Formula 1 season, not just for its on-track drama, but for a strategic blunder that could haunt McLaren for weeks to come. The team’s decision to keep Lando Norris and Oscar Piastri out during a crucial Safety Car period turned out to be a costly mistake, one that handed Max Verstappen an easy win and completely shifted the momentum in the championship fight.</p>

<h2>A Tactical Howler</h2>
<p>The decision to stay out under the Safety Car was, in hindsight, a tactical error. While it’s easy to understand why McLaren tried to maximize track position, the reality of tyre degradation and pitstop cycles meant that Red Bull’s choice was the safer, smarter one. McLaren's strategy was soon exposed for what it was: a high-risk gamble that didn’t pay off.</p>
<p>In the end, Verstappen cruised to victory, finishing a comfortable eight seconds ahead of Piastri in second, while Norris could only manage fourth. Sky Sports analysts were quick to label McLaren’s decision as a “tactical howler,” noting that the team's hesitation ultimately handed Verstappen the upper hand. “By staying out, McLaren had hoped to make up for what they lost earlier in the season,” Sky’s commentators said. “But in the end, it only gave Verstappen the lead he needed.”</p>

<h2>Team Reaction</h2>
<p>McLaren team principal Andrea Stella was frank in his assessment after the race. He admitted that the strategy didn’t work, acknowledging that they had misjudged the timing and circumstances. “We had a strategy in place, but unfortunately, it didn’t work out,” Stella explained. “We should have pitted with the rest of the field under the Safety Car. In hindsight, that’s clear. We gambled on track position, but it didn’t pay off.”</p>
<p>This pitstop blunder has turned the final race of the season in Abu Dhabi into a must-win for Norris. With Verstappen now so close in the standings, McLaren will have to learn from this mistake and avoid similar errors at Yas Marina. The team’s strategic misstep could have serious consequences, as it handed Verstappen not just a race win, but a psychological advantage going into the final showdown.</p>

<h2>A Lesson in Strategic Caution</h2>
<p>In Formula 1, every decision matters, and McLaren learned that lesson the hard way in Qatar. Their gamble on track position was an ambitious, high-risk strategy, but it ultimately proved to be a costly mistake. Andrea and his team will undoubtedly spend the weeks leading up to the Abu Dhabi Grand Prix reflecting on what went wrong and how to avoid a repeat in the season finale.</p>
<p>As the championship battle now stands, it’s all to play for in Abu Dhabi, with Verstappen only 12 points behind Norris and Piastri also in the hunt. McLaren’s biggest challenge will be to avoid repeating the same strategic error in the high-pressure final race, because in Formula 1, even a small mistake can cost you the title.</p>"""
    }
]

# Process each blog
for data in blogs_data:
    # Handle image
    image_path = None
    if data['image_source']:
        source_path = Path(f"/Users/vinayadusumilli/website/media/blog_images/{data['image_source']}")
        if source_path.exists():
            image_path = f"blog_images/{data['image_source']}"
            print(f"✓ Found existing image for {data['title']}")
        else:
            print(f"! Image not found: {source_path}")

    # Create or update blog
    blog, created = Blog.objects.update_or_create(
        slug=data['slug'],
        defaults={
            'title': data['title'],
            'excerpt': data['excerpt'],
            'content': data['content'],
            'author': AUTHOR,
            'image': image_path
        }
    )
    
    action = "Created" if created else "Updated"
    print(f"✓ {action} blog: {blog.title}")

print("\n🎉 All new blogs have been processed!")
