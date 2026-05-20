import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fix_css = """
<style>
/* Footer Layout Fix */
.elementor-element-f977387 > .e-con-inner {
    display: flex !important;
    flex-wrap: wrap !important;
    justify-content: space-between !important;
    align-items: flex-start !important;
    gap: 20px;
    width: 100%;
}
.elementor-element-f977387 > .e-con-inner > .e-con-child {
    flex: 1 1 200px;
    min-width: 200px;
}
.elementor-element-f977387 > .e-con-inner > .elementor-element-19c646f {
    flex: 2 1 300px;
}
.elementor-element-f977387 > .e-con-inner > .elementor-element-2c264a4 {
    flex: 1 1 100% !important;
    max-width: 100% !important;
    width: 100% !important;
    margin-top: 40px !important;
    border-top: 1px solid rgba(255,255,255,0.1) !important;
    padding-top: 20px !important;
}
.elementor-element-2c264a4 > .e-con-inner {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    width: 100% !important;
    flex-direction: row !important;
}
@media (max-width: 768px) {
    .elementor-element-f977387 > .e-con-inner {
        flex-direction: column !important;
    }
    .elementor-element-2c264a4 > .e-con-inner {
        flex-direction: column !important;
        gap: 20px;
    }
}
</style>
"""

target = '<div class="elementor-element elementor-element-f977387 e-flex e-con-boxed e-con e-parent"'
if target in content and "/* Footer Layout Fix */" not in content:
    content = content.replace(target, fix_css + "\n\t\t" + target)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed footer layout in index.html")
else:
    print("Could not find footer or already fixed.")
