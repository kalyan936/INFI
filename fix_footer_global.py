import os

css_fix = """
<style>
/* Global Footer Layout Fix */
.elementor-element-f977387 > .e-con-inner {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: wrap !important;
    justify-content: space-between !important;
    align-items: flex-start !important;
    gap: 30px !important;
    width: 100% !important;
}

.elementor-element-f977387 > .e-con-inner > .e-con-child {
    flex: 1 1 0 !important;
    width: auto !important;
    min-width: 150px !important;
}

/* Logo column gets slightly more space */
.elementor-element-f977387 > .e-con-inner > .elementor-element-19c646f {
    flex: 2 1 0 !important;
    min-width: 250px !important;
}

/* Bottom copyright & social row */
.elementor-element-f977387 > .e-con-inner > .elementor-element-2c264a4 {
    flex: 1 1 100% !important;
    width: 100% !important;
    max-width: 100% !important;
    margin-top: 40px !important;
    border-top: 1px solid rgba(255,255,255,0.1) !important;
    padding-top: 20px !important;
}
.elementor-element-2c264a4 > .e-con-inner {
    display: flex !important;
    flex-direction: row !important;
    justify-content: space-between !important;
    align-items: center !important;
    width: 100% !important;
}

@media (max-width: 768px) {
    .elementor-element-f977387 > .e-con-inner {
        flex-direction: column !important;
    }
    .elementor-element-2c264a4 > .e-con-inner {
        flex-direction: column !important;
        gap: 20px !important;
    }
}
</style>
"""

pages = [
    'index.html',
    'about-us/index.html',
    'contact-us/index.html',
    'industries/index.html',
    'services/index.html'
]

for p in pages:
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove old fix if present
        if "/* Footer Layout Fix */" in content:
            # We need to find the style block and remove it. 
            # Easiest way is to just replace the whole file from a clean state or use regex.
            import re
            content = re.sub(r'<style>\s*/\* Footer Layout Fix \*/.*?</style>', '', content, flags=re.DOTALL)
            
        if "/* Global Footer Layout Fix */" not in content:
            # Inject right before the closing </body> tag
            content = content.replace("</body>", css_fix + "\n</body>")
            with open(p, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed footer in {p}")
        else:
            print(f"Footer already fixed in {p}")

