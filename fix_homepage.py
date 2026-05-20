import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the broken avatar images + lorem ipsum + "Trusted by 2,000+" section
# This is the block from "Congue velit nec hac" down to "Trusted by 2,000+ Happy Clients"
# It sits inside elementor-element-9259d99

old_broken_section = '''				<div class="elementor-element elementor-element-9259d99 e-con-full e-flex e-con e-child"
					data-id="9259d99" data-element_type="container" data-e-type="container">'''

# Replace the entire content of that container with meaningful company stats
replacement_section = '''				<div class="elementor-element elementor-element-9259d99 e-con-full e-flex e-con e-child"
					data-id="9259d99" data-element_type="container" data-e-type="container"
					style="display: flex; flex-direction: column; gap: 24px; justify-content: center;">
					<p style="color: #a3a3a3; font-size: 18px; line-height: 1.8; margin: 0;">
						We deliver cutting-edge AI, data engineering, and cloud solutions that drive measurable business outcomes. Our expert team combines deep technical knowledge with industry experience to accelerate your digital transformation journey.
					</p>
					<div style="display: flex; gap: 40px; flex-wrap: wrap; margin-top: 16px;">
						<div style="text-align: center;">
							<div style="font-size: 36px; font-weight: 900; background: linear-gradient(135deg, #4f46e5, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">50+</div>
							<div style="color: #a3a3a3; font-size: 14px; margin-top: 4px;">Projects Delivered</div>
						</div>
						<div style="text-align: center;">
							<div style="font-size: 36px; font-weight: 900; background: linear-gradient(135deg, #4f46e5, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">30+</div>
							<div style="color: #a3a3a3; font-size: 14px; margin-top: 4px;">Happy Clients</div>
						</div>
						<div style="text-align: center;">
							<div style="font-size: 36px; font-weight: 900; background: linear-gradient(135deg, #4f46e5, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">3+</div>
							<div style="color: #a3a3a3; font-size: 14px; margin-top: 4px;">Years Experience</div>
						</div>
						<div style="text-align: center;">
							<div style="font-size: 36px; font-weight: 900; background: linear-gradient(135deg, #4f46e5, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">99%</div>
							<div style="color: #a3a3a3; font-size: 14px; margin-top: 4px;">Client Satisfaction</div>
						</div>
					</div>'''

if old_broken_section in content:
    # Find the start of the broken section
    start = content.find(old_broken_section)
    # Find the closing tags - we need to find the matching closing div
    # The section ends before elementor-element-d52830f
    end_marker = '<div class="elementor-element elementor-element-d52830f'
    end = content.find(end_marker, start)
    
    if end != -1:
        # Extract and count divs to find proper closing
        section = content[start:end]
        content = content[:start] + replacement_section + "\n\t\t\t\t</div>\n\t\t\t\t" + content[end:]
        print("1. Removed broken avatar section and replaced with company stats")
    else:
        print("1. ERROR: Could not find end marker for broken section")
else:
    print("1. Broken section not found (may already be fixed)")

# 2. Replace the broken img_5.png with the new generated image
old_img = './wp-content/uploads/sites/15/2026/03/img_5.png'
new_img = './generative_ai_llm.png'

if old_img in content:
    content = content.replace(old_img, new_img)
    print("2. Replaced broken img_5.png with generative_ai_llm.png")
else:
    print("2. img_5.png not found (may already be fixed)")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Home page updated.")
