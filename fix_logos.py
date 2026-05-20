import re

with open('g:/infybytes/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all elementor thumb logos with our logo_icon.png
content = re.sub(r'src="\./wp-content/uploads/sites/15/elementor/thumbs/.*?\.png"', 'src="./logo_icon.png"', content)

with open('g:/infybytes/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Logos replaced successfully!")
