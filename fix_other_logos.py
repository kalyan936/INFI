import os

directories = ['about-us', 'contact-us', 'industries', 'services']
logo_target = """						<a href="../" style="display: flex; align-items: center; gap: 12px; text-decoration: none;">
							<img src="../wp-content/uploads/sites/15/elementor/thumbs/AI-BOT-Assisten-rkr4rs1arkx40bliilvqpcqkq44yo2baa5yhqkcxds.png" alt="Infibytes Systems Logo" style="height: 48px; width: auto; object-fit: contain;">
							<div style="display: flex; flex-direction: column; justify-content: center; text-transform: uppercase;">
								<span style="font-family: 'Outfit', 'Inter Tight', 'Montserrat', sans-serif; font-weight: 900; font-size: 22px; color: #1a1a1a; letter-spacing: 2px; line-height: 1;">INFIBYTE</span>
								<span style="font-family: 'Outfit', 'Inter Tight', 'Montserrat', sans-serif; font-weight: 600; font-size: 10px; color: #666666; letter-spacing: 3px; line-height: 1.2;">SYSTEMS</span>
							</div>
						</a>"""

logo_replacement = """						<a href="../" style="display: flex; align-items: center; text-decoration: none;">
							<img src="../logo.png" alt="Infibytes Systems Logo" style="height: 60px; width: auto; object-fit: contain;">
						</a>"""

for d in directories:
    file_path = os.path.join(d, 'index.html')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if logo_target in content:
            content = content.replace(logo_target, logo_replacement)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file_path}")
        else:
            print(f"Logo target not found in {file_path}")
