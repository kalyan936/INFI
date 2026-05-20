import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Logo
logo_target = """						<a href="./" style="display: flex; align-items: center; gap: 12px; text-decoration: none;">
							<img src="./wp-content/uploads/sites/15/elementor/thumbs/AI-BOT-Assisten-rkr4rs1arkx40bliilvqpcqkq44yo2baa5yhqkcxds.png" alt="Infibytes Systems Logo" style="height: 48px; width: auto; object-fit: contain;">
							<div style="display: flex; flex-direction: column; justify-content: center; text-transform: uppercase;">
								<span style="font-family: 'Outfit', 'Inter Tight', 'Montserrat', sans-serif; font-weight: 900; font-size: 22px; color: #1a1a1a; letter-spacing: 2px; line-height: 1;">INFIBYTE</span>
								<span style="font-family: 'Outfit', 'Inter Tight', 'Montserrat', sans-serif; font-weight: 600; font-size: 10px; color: #666666; letter-spacing: 3px; line-height: 1.2;">SYSTEMS</span>
							</div>
						</a>"""

logo_replacement = """						<a href="./" style="display: flex; align-items: center; text-decoration: none;">
							<img src="./logo.png" alt="Infibytes Systems Logo" style="height: 60px; width: auto; object-fit: contain;">
						</a>"""

content = content.replace(logo_target, logo_replacement)

# Replace Testimonial Section
# The Testimonial section starts at '<div class="elementor-element elementor-element-119e418'
# and ends right before '<div class="elementor-element elementor-element-f977387'

core_values = """		<div class="elementor-element elementor-element-119e418 e-flex e-con-boxed e-con e-parent" data-id="119e418"
			data-element_type="container" data-e-type="container">
			<div class="e-con-inner">
				<div class="elementor-element elementor-element-9b21d90 e-con-full e-flex e-con e-child"
					data-id="9b21d90" data-element_type="container" data-e-type="container">
					<div class="elementor-element elementor-element-f48f536 elementor-widget elementor-widget-heading"
						data-id="f48f536" data-element_type="widget" data-e-type="widget"
						data-widget_type="heading.default">
						<h6 class="elementor-heading-title elementor-size-default">Our Core Values</h6>
					</div>
					<div class="elementor-element elementor-element-b3d8bba elementor-widget elementor-widget-heading"
						data-id="b3d8bba" data-element_type="widget" data-e-type="widget"
						data-widget_type="heading.default">
						<h2 class="elementor-heading-title elementor-size-default">Principles That Drive Our Innovation</h2>
					</div>
				</div>
				<div class="elementor-element elementor-element-4660a50 e-con-full e-grid e-con e-child"
					data-id="4660a50" data-element_type="container" data-e-type="container"
					style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px;">
					
					<div style="background: #111; padding: 40px; border-radius: 12px; border: 1px solid #333;">
						<h3 style="color: #fff; font-size: 24px; margin-bottom: 15px;">Innovation First</h3>
						<p style="color: #aaa; font-size: 16px; line-height: 1.6;">We constantly push the boundaries of AI and technology to deliver cutting-edge solutions that keep our clients ahead of the curve.</p>
					</div>

					<div style="background: #111; padding: 40px; border-radius: 12px; border: 1px solid #333;">
						<h3 style="color: #fff; font-size: 24px; margin-bottom: 15px;">Client Centric</h3>
						<p style="color: #aaa; font-size: 16px; line-height: 1.6;">Your success is our success. We partner closely with organizations to build systems specifically tailored to their unique challenges.</p>
					</div>

					<div style="background: #111; padding: 40px; border-radius: 12px; border: 1px solid #333;">
						<h3 style="color: #fff; font-size: 24px; margin-bottom: 15px;">Reliability</h3>
						<p style="color: #aaa; font-size: 16px; line-height: 1.6;">We build robust, scalable, and secure systems that enterprises can trust for their daily mission-critical operations.</p>
					</div>

				</div>
			</div>
		</div>
"""

start_str = '<div class="elementor-element elementor-element-119e418 e-flex e-con-boxed e-con e-parent"'
end_str = '<div class="elementor-element elementor-element-f977387 e-flex e-con-boxed e-con e-parent"'

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + core_values + "\n\t\t" + content[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated index.html!")
else:
    print(f"Could not find section boundaries. start_idx: {start_idx}, end_idx: {end_idx}")

