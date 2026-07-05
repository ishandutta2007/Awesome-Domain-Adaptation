import os
import subprocess
import re

base_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Domain-Adaptation"
readme_path = os.path.join(base_dir, "README.md")
assets_dir = os.path.join(base_dir, "assets")

def run_git(msg):
    cmd = f'git -C "{base_dir}" add . && git -C "{base_dir}" commit -m "{msg}" && git -C "{base_dir}" push'
    subprocess.run(cmd, shell=True, check=True)

# Step 2: Emojis and Banner
os.makedirs(assets_dir, exist_ok=True)
svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200">
    <defs>
        <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#2a0845;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#6441A5;stop-opacity:1" />
        </linearGradient>
    </defs>
    <rect width="100%" height="100%" fill="url(#grad1)" rx="15" />
    <text x="50%" y="50%" font-family="Arial" font-size="40" font-weight="bold" fill="white" alignment-baseline="middle" text-anchor="middle">
        Awesome Domain Adaptation
    </text>
    <circle cx="100" cy="100" r="20" fill="white" opacity="0.5">
        <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.5;0.1;0.5" dur="2s" repeatCount="indefinite" />
    </circle>
    <circle cx="700" cy="100" r="20" fill="white" opacity="0.5">
        <animate attributeName="r" values="20;30;20" dur="2s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.5;0.1;0.5" dur="2s" repeatCount="indefinite" />
    </circle>
</svg>'''
with open(os.path.join(assets_dir, "banner.svg"), 'w') as f:
    f.write(svg_content)

with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

if "![Banner](assets/banner.svg)" not in content and "alt=\"Banner\"" not in content:
    content = content.replace("# Awesome-Domain-Adaptation\n", "# Awesome-Domain-Adaptation\n\n<div align=\"center\">\n  <img src=\"assets/banner.svg\" alt=\"Banner\" />\n</div>\n\n", 1)

content = content.replace("## Domain Adaptation in AI", "## 🧠 Domain Adaptation in AI")
content = content.replace("## 1. The Macro Chronological Evolution", "## 🕰️ 1. The Macro Chronological Evolution")
content = content.replace("## 2. Core Functional & Supervised Variants", "## ⚙️ 2. Core Functional & Supervised Variants")
content = content.replace("## 3. The Adversarial Alignment", "## ⚔️ 3. The Adversarial Alignment")
content = content.replace("## 4. Production Engineering Challenges", "## 🚧 4. Production Engineering Challenges")
content = content.replace("## 5. Frontier Real-World", "## 🚀 5. Frontier Real-World")

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git("added emojis and banner")

# Step 3: SEO and badges left
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'

if '<div align="center">\n  <!-- BADGES -->' not in content:
    banner_div_end = '</div>\n'
    insert_idx = content.find(banner_div_end)
    if insert_idx != -1:
        insert_idx += len(banner_div_end)
        content = content[:insert_idx] + f'\n<div align="center">\n  <!-- BADGES -->\n  {left_badges}\n</div>\n' + content[insert_idx:]
    else:
        content = content.replace("# Awesome-Domain-Adaptation", f"# Awesome-Domain-Adaptation\n\n<div align=\"center\">\n  <!-- BADGES -->\n  {left_badges}\n</div>\n", 1)

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git("seo optimised and badges to left added")

# Step 4: Badges right
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

right_badge = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'
if right_badge not in content:
    content = content.replace(left_badges, f'{left_badges} {right_badge}')

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git("badges to right added")

# Step 5: Star history
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Domain-Adaptation&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Domain-Adaptation&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Domain-Adaptation&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Domain-Adaptation&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

if "Star History Chart" not in content:
    content = content + "\n" + star_history

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(content)
run_git("star history added")

# Step 6: Fix chartrepos
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'chartrepos' in content:
    content = content.replace('chartrepos', 'chart?repos')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    run_git("fixed star plot")
else:
    subprocess.run(f'git -C "{base_dir}" commit --allow-empty -m "fixed star plot" && git -C "{base_dir}" push', shell=True)

# Step 7: Fix awesome link
with open(readme_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'https://github.com/sindresorhus/awesome' in content:
    content = content.replace('https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)
    run_git("invalid awesome link fixed")
else:
    subprocess.run(f'git -C "{base_dir}" commit --allow-empty -m "invalid awesome link fixed" && git -C "{base_dir}" push', shell=True)

print("All tasks completed.")
