import os
import django
from django.core.files import File
from django.utils.text import slugify
import requests
from io import BytesIO

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Blog

def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return BytesIO(response.content)
    except Exception as e:
        print(f"Error downloading image: {e}")
    return None

def populate_db():
    print("Starting database population...")
    
    blogs = [
        {
            'title': 'Brand Visibility at F1 Circuit Tracks: A Deep Dive into the Art of Strategic Placement',
            'author': 'Khushi Deshmukh',
            'image_url': 'https://images.unsplash.com/photo-1535132011086-b8818f016104?q=80&w=2070&auto=format&fit=crop',
            'content': """Formula 1 (F1) racing is a spectacle of speed, skill, and strategy, but beneath the tire-burning action lies a powerful marketing engine that brands harness to reach millions of viewers across the globe. The branding at F1 circuit tracks is not just about slapping logos on barriers and cars; it's a meticulously crafted strategy to maximize brand visibility. One of the most dynamic elements of this marketing approach is how broadcasters change logo placements across different frames and regions, creating unique opportunities for sponsors. Let’s delve into this process, how it varies by country, and why it’s a game-changer for brands.

The Dynamic Nature of F1 Brand Placements

The role of broadcasters in F1 races goes beyond simply capturing the action on track; they also control how and when brand logos appear on the global screen. Brands often pay millions for their logos to be featured during these highly televised events. However, what makes this even more interesting is how broadcasters change these logos across various frames, ensuring maximum exposure for the sponsors.

Changing Logos in Different Frames

During an F1 race, broadcasters employ a technique known as dynamic branding.This means that the visibility of a logo is not static. Logos change depending on the angle, proximity, and timing of the shot. For example, a logo on a trackside banner may be shown during a pit stop or a close-up shot of a driver, while another sponsor’s logo may be highlighted when the camera zooms in on the car in the final stretch.

The same brand could be shown multiple times, each time in a different visual context, on barriers, cars, drivers' suits, and even digital displays. Broadcasters may also rotate logos in line with specific shots, taking into account the aesthetic of the race. The switching of logo placements according to the scene ensures that brands are not just seen but are showcased in high-impact moments, such as overtakes, pit stops, or the thrilling final laps.

Variation in Placements Across Countries

F1’s global nature adds an additional layer of complexity to the branding process. Broadcasters in different regions will display various sponsor logos or change the emphasis of logos to reflect regional preferences and audience interests.

For instance, a major European brand may have a larger presence at the Monaco Grand Prix, where the European audience is predominant, while another brand may be emphasized more heavily during a race in Asia or the Middle East. This geo-targeting strategy ensures that brands are marketed more effectively to local consumers, aligning with regional interests and preferences. As a result, the same race can have different branding focuses, with some logos more prominent in one country than in another.

Why This Matters?

The strategic placement of logos during an F1 race provides several key advantages for brands, particularly when considering the global and multifaceted nature of the sport.

1. Maximal Exposure During Key Moments

F1 races are characterized by intense, fast-paced action, often accompanied by thrilling moments that attract viewers' attention. By placing logos in these high-impact moments, brands gain maximum exposure. The ability of broadcasters to switch logos between various shots ensures that sponsors are featured in front of a global audience at the exact moment of peak excitement, making their brand part of the emotional high of the race. This level of visibility is unparalleled in many other sports.

2. Targeted Regional Marketing

With F1 races happening around the world, broadcasters are able to fine-tune their branding strategies according to the location of the event. Sponsors can gain significant local relevance by placing logos on trackside advertising in regions where they are trying to expand their footprint. Whether it’s a regional auto brand during a race in Japan or a luxury watch brand in Monaco, the custom placements allow for geographic targeting in a way traditional global advertising cannot match.

3. Creating a Long-Lasting Brand Presence

The consistency of branding throughout a race, in combination with the broadcast’s ability to show logos in varying contexts, helps brands establish brand recall. Spectators, even those who might not be F1 enthusiasts, are constantly exposed to these logos, whether they are watching a close-up shot of a driver’s helmet or a wide-angle shot of the entire track. This repeated exposure in different settings ensures that the brand remains top-of-mind long after the race ends.


Brand visibility at F1 circuits has become a fine art, one where broadcasters, sponsors, and marketing experts work together to maximize brand presence. Through dynamic logo placements, geo-targeting for different countries, and an understanding of how viewers engage with the broadcast, F1 has created a unique platform where brands can truly shine. It’s not just about slapping a logo on a car anymore. It's about integrating the brand seamlessly into the action. In an ever-competitive marketing world, this kind of visibility is invaluable, and Formula 1 is showing the way forward for strategic brand engagement in live sports broadcasting."""
        },
        {
            'title': "England's women's football team secured a commanding 8-0 victory over China",
            'author': 'Khushi Deshmukh',
            'image_url': 'https://images.unsplash.com/photo-1518091043644-c1d4457512c6?q=80&w=2000&auto=format&fit=crop', # Football image
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
</div>"""
        },
        {
            'title': "Qatar 2025 Race Highlights",
            'author': 'Khushi Deshmukh',
            'image_url': 'https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?q=80&w=2070&auto=format&fit=crop', # Racing car image
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
            'author': 'Khushi Deshmukh',
            'image_url': 'https://images.unsplash.com/photo-1504285526612-254c0d3887b9?q=80&w=2070&auto=format&fit=crop', # Pitstop/Racing image
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

    for blog_data in blogs:
        slug = slugify(blog_data['title'])
        
        # Check if blog already exists
        if Blog.objects.filter(slug=slug).exists():
            print(f"Blog '{blog_data['title']}' already exists. Updating...")
            blog = Blog.objects.get(slug=slug)
            blog.content = blog_data['content']
            blog.author = blog_data['author']
        else:
            print(f"Creating blog: {blog_data['title']}")
            blog = Blog(
                title=blog_data['title'],
                content=blog_data['content'],
                slug=slug,
                author=blog_data['author']
            )

        # Handle Image
        print(f"Downloading image for {blog.title}...")
        img_file = download_image(blog_data['image_url'])
        if img_file:
            # Create a filename from the slug
            filename = f"{slug}.jpg"
            blog.image.save(filename, File(img_file), save=False)
            print("Image downloaded successfully.")
        else:
            print("Failed to download image.")

        blog.save()
        print(f"Successfully saved blog: {blog.title}\n")

if __name__ == '__main__':
    populate_db()
