import re
import os

with open('g:/infybytes/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Restore the 4 floating hero images based on their titles
content = content.replace(
    'src="./logo_icon.png"\n\t\t\t\t\t\t\ttitle="AI-BOT-Assisten"', 
    'src="./wp-content/uploads/sites/15/elementor/thumbs/AI-BOT-Assisten-rkr4rs1arkx40bliilvqpcqkq44yo2baa5yhqkcxds.png"\n\t\t\t\t\t\t\ttitle="AI-BOT-Assisten"'
)
content = content.replace(
    'src="./logo_icon.png"\n\t\t\t\t\t\t\ttitle="AI-Text-Translator"', 
    'src="./wp-content/uploads/sites/15/elementor/thumbs/AI-Text-Translator-rkr4rsz4yeyebxk5d4ad9ui1bi0bvrf0malz7ubj7k.png"\n\t\t\t\t\t\t\ttitle="AI-Text-Translator"'
)
content = content.replace(
    'src="./logo_icon.png"\n\t\t\t\t\t\t\ttitle="AI-Website-Builder"', 
    'src="./wp-content/uploads/sites/15/elementor/thumbs/AI-Website-Builder-rkr4rtwz58zonjis7mozuc9hwvvp3giqyf9gp4a51c.png"\n\t\t\t\t\t\t\ttitle="AI-Website-Builder"'
)
content = content.replace(
    'src="./logo_icon.png"\n\t\t\t\t\t\t\ttitle="Ai-Security-Generator"', 
    'src="./wp-content/uploads/sites/15/elementor/thumbs/Ai-Security-Generator-rkr4rsz4yey97s82s3m952jj81ea2af7yx8iplosn4.png"\n\t\t\t\t\t\t\ttitle="Ai-Security-Generator"'
)

# Also handle single-line versions just in case
content = re.sub(r'src="\./logo_icon\.png"(.*?)title="AI-BOT-Assisten"', r'src="./wp-content/uploads/sites/15/elementor/thumbs/AI-BOT-Assisten-rkr4rs1arkx40bliilvqpcqkq44yo2baa5yhqkcxds.png"\1title="AI-BOT-Assisten"', content, flags=re.DOTALL)
content = re.sub(r'src="\./logo_icon\.png"(.*?)title="AI-Text-Translator"', r'src="./wp-content/uploads/sites/15/elementor/thumbs/AI-Text-Translator-rkr4rsz4yeyebxk5d4ad9ui1bi0bvrf0malz7ubj7k.png"\1title="AI-Text-Translator"', content, flags=re.DOTALL)
content = re.sub(r'src="\./logo_icon\.png"(.*?)title="AI-Website-Builder"', r'src="./wp-content/uploads/sites/15/elementor/thumbs/AI-Website-Builder-rkr4rtwz58zonjis7mozuc9hwvvp3giqyf9gp4a51c.png"\1title="AI-Website-Builder"', content, flags=re.DOTALL)
content = re.sub(r'src="\./logo_icon\.png"(.*?)title="Ai-Security-Generator"', r'src="./wp-content/uploads/sites/15/elementor/thumbs/Ai-Security-Generator-rkr4rsz4yey97s82s3m952jj81ea2af7yx8iplosn4.png"\1title="Ai-Security-Generator"', content, flags=re.DOTALL)

# 2. Remove the "Used by leading brands" section completely
# It starts at data-id="5e9db73" and ends before data-id="8d2ba1a"
marquee_pattern = re.compile(r'<div class="elementor-element elementor-element-5e9db73.*?</div>\s*</div>\s*</div>\s*</div>\s*(?=<div class="elementor-element elementor-element-8d2ba1a)', re.DOTALL)
content = marquee_pattern.sub('', content)

# 3. Create SVG icons for Services
icons_dir = "g:/infybytes/icons"
os.makedirs(icons_dir, exist_ok=True)

svg_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100" height="100">
    <rect width="100" height="100" rx="20" fill="rgba(255, 255, 255, 0.05)" stroke="url(#grad)" stroke-width="2"/>
    <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#f05a28;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#7a288a;stop-opacity:1" />
        </linearGradient>
    </defs>
    <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="24" fill="#ffffff" font-weight="bold" dominant-baseline="middle" text-anchor="middle">{text}</text>
</svg>"""

service_icons = {
    "Artificial Intelligence Industry Blue Line-04 1": ("service_ai.svg", "AI"),
    "Artificial Intelligence Industry Blue Line-03 1": ("service_data.svg", "DATA"),
    "Artificial Intelligence Industry Blue Line-21 1": ("service_genai.svg", "LLM"),
    "Artificial Intelligence Industry Blue Line-22 1": ("service_hr.svg", "HR"),
    "Artificial Intelligence Industry Blue Line-20 1": ("service_health.svg", "CARE"),
    "Artificial Intelligence Industry Blue Line-15 1": ("service_finance.svg", "FIN"),
}

for title, (filename, text) in service_icons.items():
    svg_path = os.path.join(icons_dir, filename)
    with open(svg_path, 'w') as sf:
        sf.write(svg_template.replace("{text}", text))
    
    # Replace in HTML
    pattern = r'src="\./logo_icon\.png"(.*?)title="' + re.escape(title) + r'"'
    replacement = r'src="./icons/' + filename + r'"\1title="' + title + r'"'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 4. Create SVG icons for Tech Stack
tech_icons = {
    "GCP Colored Logo2": ("tech_gcp.svg", "GCP"),
    "DO Colored Logo2": ("tech_do.svg", "DO"),
    "Vultr Colored Logo2": ("tech_vultr.svg", "VULTR"),
    "AWS Colored Logo2": ("tech_aws.svg", "AWS"),
}

for title, (filename, text) in tech_icons.items():
    svg_path = os.path.join(icons_dir, filename)
    with open(svg_path, 'w') as sf:
        sf.write(svg_template.replace("{text}", text))
    
    # Replace in HTML
    pattern = r'src="\./logo_icon\.png"(.*?)title="' + re.escape(title) + r'"'
    replacement = r'src="./icons/' + filename + r'"\1title="' + title + r'"'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('g:/infybytes/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored hero images, deleted marquee, and generated/replaced service/tech SVGs!")
