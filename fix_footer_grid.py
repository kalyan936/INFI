import os
import re

css_fix = """
<style>
/* Global Footer Layout Fix - GRID */
.elementor-element-f977387 > .e-con-inner {
    display: grid !important;
    grid-template-columns: 2fr 1fr 1fr 1fr !important;
    gap: 30px !important;
    width: 100% !important;
    align-items: start !important;
}

.elementor-element-f977387 > .e-con-inner > .e-con-child {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
}

/* Bottom copyright & social row */
.elementor-element-f977387 > .e-con-inner > .elementor-element-2c264a4 {
    grid-column: 1 / -1 !important;
    margin-top: 40px !important;
    border-top: 1px solid rgba(255,255,255,0.1) !important;
    padding-top: 20px !important;
    display: block !important;
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
        grid-template-columns: 1fr !important;
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
        content = re.sub(r'<style>\s*/\* Global Footer Layout Fix \*/.*?</style>', '', content, flags=re.DOTALL)
        content = re.sub(r'<style>\s*/\* Footer Layout Fix \*/.*?</style>', '', content, flags=re.DOTALL)
        
        # Inject right before the closing </body> tag
        content = content.replace("</body>", css_fix + "\n</body>")
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed footer using Grid in {p}")

