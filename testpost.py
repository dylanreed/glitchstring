#!/usr/bin/env python3
import os
import random
from datetime import datetime, timedelta

# Configuration
OUTPUT_DIR = "content/posts"
NUM_POSTS = 10
NUM_MICROPOSTS = 5
NUM_PHOTO_POSTS = 3

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Sample content
titles = [
    "Creating Puppet Animations with FFmpeg",
    "Python Script for Automated Visemes",
    "Vintage Animation Techniques in Modern Code",
    "Audio Reactivity for Digital Puppets",
    "Building a Cartoon Pipeline from Scratch",
    "Pygame for Creative Coding Projects",
    "Machine Learning for Character Animation",
    "Procedural Eyebrow Movement Algorithms",
    "Muppet-Style Digital Performance Art",
    "Real-time Speech-to-Animation Conversion",
    "Blockchain Jokes for Puppet Comedy",
    "The Art of Digital Puppetry",
    "Animation State Machines in Python"
]

tags = ["python", "animation", "puppets", "creative-coding", "pygame", 
       "ffmpeg", "machine-learning", "procedural", "audio", "visemes", 
       "vintage", "cartoon", "comedy", "blockchain"]

paragraphs = [
    "When I first started merging 1940s animation techniques with modern code, I didn't expect to fall down a rabbit hole of viseme mapping and real-time audio reactivity. Yet here we are, with puppets that respond to speech patterns and emote based on frequency analysis.",
    
    "The foundation of any good puppet system is a skeleton with proper hierarchical joints. In my framework, I use a simple structure that allows for both programmatic and manual control.",
    
    "To recreate that classic rubber-hose animation style, I add intentional overshooting and anticipation to all movements. This creates that bouncy, stretchy feel characteristic of early cartoons.",
    
    "Audio processing is where things get interesting. By analyzing incoming audio in real-time, we can map specific phonemes to mouth shapes (visemes) to create the illusion of speech.",
    
    "I've been experimenting with procedural eyebrow movements based on sentiment analysis of the spoken text. It's uncanny how much emotion a simple pair of eyebrows can convey.",
    
    "My latest project combines Python, Pygame, and FFmpeg to create a full animation pipeline that goes from audio input to rendered output without any manual keyframing.",
    
    "The vintage aesthetic isn't just for show - there's something about the constraints of early animation that forces creativity in problem-solving. Sometimes limitations breed innovation.",
    
    "I'm currently working on adding procedural performance patterns - basically teaching the puppets how to 'act' with rhythmic movement patterns that feel natural and entertaining.",
    
    "One challenge with puppet animation is avoiding the uncanny valley. Too realistic and it becomes creepy; too simple and it loses expression. Finding that sweet spot is an art form.",
    
    "Blockchain jokes have never been funnier than when delivered by a fuzzy digital puppet with exaggerated eyebrow movements. Something about the contrast just works.",
    
    "The glitchy aesthetic of my animations isn't a bug, it's a feature. I intentionally introduce frame skips and visual artifacts to create a unique digital puppetry style.",
    
    "My goal is to create digital characters with enough personality that they feel alive, even though they're clearly not trying to be realistic. It's puppetry, not simulation."
]

micropost_content = [
    "Just fixed the eyebrow algorithm. Now my puppets can look properly skeptical.",
    "Three hours debugging a viseme issue only to find I misspelled 'mouth'. Classic.",
    "New cartoon shader is coming along nicely. Very rubber-hose, much bounce.",
    "Audio-reactive pupils really add so much character to these puppet eyes.",
    "Testing a new procedural arm-flailing routine. Hilarity ensues.",
    "Thinking about adding vintage film grain and projection artifacts to the renderer.",
    "Sometimes I think my puppets are judging my code. Those eyebrows don't lie.",
    "Just implemented real-time audio processing with negligible latency. The puppets speak!",
    "Blockchain joke of the day: Why don't NFTs ever get lost? Because they're always on the chain. (I'll see myself out)",
    "Animation timing is everything. A 50ms pause before a reaction makes it 10x funnier."
]

# Generate regular posts
for i in range(NUM_POSTS):
    title = random.choice(titles)
    titles.remove(title)  # Ensure unique titles
    
    # Create date (random in the last 30 days)
    days_ago = random.randint(0, 30)
    post_date = datetime.now() - timedelta(days=days_ago)
    date_str = post_date.strftime("%Y-%m-%dT%H:%M:%S-04:00")
    
    # Random selection of tags (2-4)
    post_tags = random.sample(tags, random.randint(2, 4))
    tags_str = ", ".join([f'"{tag}"' for tag in post_tags])
    
    # Random selection of paragraphs (3-6)
    post_paragraphs = random.sample(paragraphs, random.randint(3, 6))
    content = "\n\n".join(post_paragraphs)
    
    # Create filename (slugified title)
    slug = title.lower().replace(" ", "-").replace(",", "").replace(".", "")
    filename = f"{OUTPUT_DIR}/{slug}.md"
    
    # Write to file
    with open(filename, "w") as f:
        f.write(f"""---
title: "{title}"
date: {date_str}
tags: [{tags_str}]
---

# {title}

{content}
""")
    print(f"Created post: {filename}")

# Generate microposts
for i in range(NUM_MICROPOSTS):
    content = random.choice(micropost_content)
    micropost_content.remove(content)  # Ensure unique content
    
    # Create date (random in the last 30 days)
    days_ago = random.randint(0, 30)
    post_date = datetime.now() - timedelta(days=days_ago)
    date_str = post_date.strftime("%Y-%m-%dT%H:%M:%S-04:00")
    
    # Create filename
    filename = f"{OUTPUT_DIR}/micropost-{i+1}.md"
    
    # Write to file
    with open(filename, "w") as f:
        f.write(f"""---
date: {date_str}
---

{content}
""")
    print(f"Created micropost: {filename}")

# Generate photo posts
for i in range(NUM_PHOTO_POSTS):
    title = f"Photo Update {i+1}"
    
    # Create date (random in the last 30 days)
    days_ago = random.randint(0, 30)
    post_date = datetime.now() - timedelta(days=days_ago)
    date_str = post_date.strftime("%Y-%m-%dT%H:%M:%S-04:00")
    
    # Random selection of tags (1-3)
    post_tags = random.sample(tags, random.randint(1, 3))
    tags_str = ", ".join([f'"{tag}"' for tag in post_tags])
    
    # Create fake photo paths
    num_photos = random.randint(1, 3)
    photos = [f'"/images/sample-{i+1}-{j+1}.jpg"' for j in range(num_photos)]
    photos_str = ", ".join(photos)
    
    # Short content
    content = random.choice(paragraphs)
    
    # Create filename
    filename = f"{OUTPUT_DIR}/photo-post-{i+1}.md"
    
    # Write to file
    with open(filename, "w") as f:
        f.write(f"""---
title: "{title}"
date: {date_str}
tags: [{tags_str}]
photos: [{photos_str}]
---

{content}
""")
    print(f"Created photo post: {filename}")

print(f"\nGenerated {NUM_POSTS} regular posts, {NUM_MICROPOSTS} microposts, and {NUM_PHOTO_POSTS} photo posts in {OUTPUT_DIR}/")
print("Note: Photo posts reference images that don't exist. Create sample images in /static/images/ with corresponding names.")