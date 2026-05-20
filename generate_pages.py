import os

def generate():
    # 1. Read the modified index.html
    index_path = "g:/infybytes/index.html"
    if not os.path.exists(index_path):
        print("Error: index.html not found!")
        return
        
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 2. Extract templates
    # Split by </header> to get the head and header
    parts_header = html.split("</header>")
    header_template = parts_header[0] + "</header>"
    
    # Split by <footer to get the footer and scripts
    parts_footer = html.split('<footer data-elementor-type="footer"')
    footer_template = '<footer data-elementor-type="footer"' + parts_footer[1]

    # Let's clean the header template - we'll replace the canonical link if any, and set custom page titles!
    def make_subpage_header(title, folder, depth_prefix="../"):
        sub_h = header_template
        
        # Replace relative paths (single and double quotes)
        sub_h = sub_h.replace("='./", f"='{depth_prefix}")
        sub_h = sub_h.replace('="./', f'="{depth_prefix}')
        
        # Replace escaped relative paths in JS configurations
        sub_h = sub_h.replace(".\\/wp-content", "..\\/wp-content")
        sub_h = sub_h.replace(".\\/wp-includes", "..\\/wp-includes")
        sub_h = sub_h.replace(".\\/wp-json", "..\\/wp-json")
        sub_h = sub_h.replace(".\\/wp-admin", "..\\/wp-admin")
        
        # Inject our custom custom stylesheet right before </head>
        custom_css_link = f'<link rel="stylesheet" href="{depth_prefix}wp-content/uploads/sites/15/elementor/css/infibytes-custom.css" media="all" />\n</head>'
        sub_h = sub_h.replace('</head>', custom_css_link)
        
        # Replace page title
        sub_h = sub_h.replace('<title>INFIBYTES SYSTEMS &#8211; Turning complex data into clear intelligent insights.</title>', 
                              f'<title>{title} &#8211; Infibytes Systems</title>')
        
        # Adjust body class to reflect singular subpage
        sub_h = sub_h.replace('class="home wp-singular', 'class="wp-singular')
        
        # Fix the active menu highlighting
        # First, strip active classes from the "Home" menu item (both desktop and mobile)
        sub_h = sub_h.replace('current-menu-item current_page_item menu-item-home menu-item-5', 'menu-item-home menu-item-5')
        sub_h = sub_h.replace('class="elementor-item elementor-item-active">Home', 'class="elementor-item">Home')
        
        # Then assign active classes to the correct subpage menu item
        if folder == "about-us":
            sub_h = sub_h.replace('menu-item-6', 'menu-item-6 current-menu-item current_page_item')
            sub_h = sub_h.replace('class="elementor-item">About Us', 'class="elementor-item elementor-item-active">About Us')
        elif folder == "services":
            sub_h = sub_h.replace('menu-item-7', 'menu-item-7 current-menu-item current_page_item')
            sub_h = sub_h.replace('class="elementor-item">Services', 'class="elementor-item elementor-item-active">Services')
        elif folder == "industries":
            sub_h = sub_h.replace('menu-item-16', 'menu-item-16 current-menu-item current_page_item')
            sub_h = sub_h.replace('class="elementor-item">Industries', 'class="elementor-item elementor-item-active">Industries')
        elif folder == "contact-us":
            sub_h = sub_h.replace('menu-item-11', 'menu-item-11 current-menu-item current_page_item')
            sub_h = sub_h.replace('class="elementor-item">Contact Us', 'class="elementor-item elementor-item-active">Contact Us')
            
        return sub_h

    def make_subpage_footer(depth_prefix="../"):
        sub_f = footer_template
        
        # Replace relative paths (single and double quotes)
        sub_f = sub_f.replace("='./", f"='{depth_prefix}")
        sub_f = sub_f.replace('="./', f'="{depth_prefix}')
        
        # Replace escaped relative paths in JS configurations
        sub_f = sub_f.replace(".\\/wp-content", "..\\/wp-content")
        sub_f = sub_f.replace(".\\/wp-includes", "..\\/wp-includes")
        sub_f = sub_f.replace(".\\/wp-json", "..\\/wp-json")
        sub_f = sub_f.replace(".\\/wp-admin", "..\\/wp-admin")
        return sub_f

    # Custom contents for the four pages
    about_content = """
<div class="infy-subpage-container">
    <!-- Hero -->
    <div class="infy-hero">
        <div class="infy-container">
            <div class="infy-metric-tag" style="background: rgba(122, 40, 138, 0.1); color: #7a288a; border-color: rgba(122, 40, 138, 0.2);">About Our Systems</div>
            <h1>Empowering Enterprises Through Intelligent Systems</h1>
            <p>At Infibytes Systems, we design, build, and deploy next-generation artificial intelligence and data science platforms that turn complex organizational data into clear, actionable intelligence.</p>
        </div>
    </div>
    
    <!-- Mission & Vision -->
    <div class="infy-container">
        <div class="infy-grid">
            <div class="infy-card">
                <div class="infy-card-content">
                    <div class="infy-card-icon"><i class="mdi mdi-target"></i></div>
                    <h3>Our Mission</h3>
                    <p>To enable enterprises to automate complex workflows, uncover hidden patterns, and achieve unprecedented efficiency by embedding advanced AI systems at the core of their operations.</p>
                </div>
            </div>
            <div class="infy-card">
                <div class="infy-card-content">
                    <div class="infy-card-icon"><i class="mdi mdi-eye-outline"></i></div>
                    <h3>Our Vision</h3>
                    <p>To become the premier global partner for bespoke enterprise intelligence, bridging the gap between cutting-edge scientific research and production-grade software applications.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Core Values -->
    <div class="infy-container" style="margin-top: 100px;">
        <h2 style="text-align: center; font-size: 2.5rem; font-weight: 800; margin-bottom: 20px;">Our Core Philosophy</h2>
        <p style="text-align: center; color: var(--text-muted); max-width: 600px; margin: 0 auto 50px auto;">Four pillars that define how we engineer, collaborate, and deliver value to our clients worldwide.</p>
        <div class="infy-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));">
            <div class="infy-card">
                <div class="infy-card-content">
                    <h3>01. Innovation First</h3>
                    <p>We continuously integrate the latest breakthroughs in Gen AI, deep learning, and NLP into our production models.</p>
                </div>
            </div>
            <div class="infy-card">
                <div class="infy-card-content">
                    <h3>02. Bulletproof Quality</h3>
                    <p>Our solutions undergo rigorous automated validation, bias audits, and scale testing for ultimate corporate reliance.</p>
                </div>
            </div>
            <div class="infy-card">
                <div class="infy-card-content">
                    <h3>03. Human-Centric AI</h3>
                    <p>We build technologies that elevate and empower human workforces rather than replacing them blindly.</p>
                </div>
            </div>
            <div class="infy-card">
                <div class="infy-card-content">
                    <h3>04. Absolute Integrity</h3>
                    <p>We adhere to strict data sovereignty, GDPR compliance, and enterprise-grade privacy protection policies.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Team Section -->
    <div class="infy-container" style="margin-top: 100px;">
        <h2 style="text-align: center; font-size: 2.5rem; font-weight: 800; margin-bottom: 20px;">The Leadership Team</h2>
        <p style="text-align: center; color: var(--text-muted); max-width: 600px; margin: 0 auto 50px auto;">World-class software engineers, AI researchers, and industry specialists driving the Infibytes vision.</p>
        <div class="infy-team-grid">
            <div class="infy-team-card">
                <img class="infy-team-img" src="../wp-content/uploads/sites/15/2026/03/10-1-1.jpg" alt="Emily Chan">
                <h4>Dr. Emily Chan</h4>
                <div class="role">Chief Executive Officer</div>
                <p>Formerly a principal AI research scientist with over 15 years of experience building predictive analytics platforms for global enterprises.</p>
            </div>
            <div class="infy-team-card">
                <img class="infy-team-img" src="../wp-content/uploads/sites/15/2026/03/1-1.jpg" alt="Marcus Vance">
                <h4>Marcus Vance</h4>
                <div class="role">Chief Technology Officer</div>
                <p>An expert in deep learning architectures and distributed high-performance computing systems. Stanford CS Alumnus.</p>
            </div>
            <div class="infy-team-card">
                <img class="infy-team-img" src="../wp-content/uploads/sites/15/2026/03/2-1.jpg" alt="Sarah Jenkins">
                <h4>Sarah Jenkins</h4>
                <div class="role">Head of HR Systems</div>
                <p>Specializes in organizational workforce analytics, recruiting intelligence systems, and talent retention algorithms.</p>
            </div>
        </div>
    </div>
</div>
"""

    services_content = """
<div class="infy-subpage-container">
    <!-- Hero -->
    <div class="infy-hero">
        <div class="infy-container">
            <div class="infy-metric-tag">Enterprise Services</div>
            <h1>Bespoke Technology & AI Solutions</h1>
            <p>We deliver production-grade systems tailored to solve complex technical, logistical, and computational challenges across your enterprise.</p>
        </div>
    </div>
    
    <!-- Services Grid -->
    <div class="infy-container">
        <div class="infy-grid">
            <!-- Service 1 -->
            <div class="infy-card">
                <div class="infy-card-content">
                    <div class="infy-card-icon"><i class="mdi mdi-brain"></i></div>
                    <h3>Artificial Intelligence Solutions</h3>
                    <p>Deploy state-of-the-art machine learning models custom-trained on your proprietary datasets. From computer vision to automated risk prediction, we engineer robust pipelines designed for extreme precision and high execution speed.</p>
                </div>
            </div>
            <!-- Service 2 -->
            <div class="infy-card">
                <div class="infy-card-content">
                    <div class="infy-card-icon"><i class="mdi mdi-chart-timeline-variant"></i></div>
                    <h3>Advanced Data Science</h3>
                    <p>Uncover powerful competitive advantages hidden deep within your database structures. Our data science teams build custom predictive dashboards, semantic processing pipelines, and automated intelligence layers that drive critical executive decisions.</p>
                </div>
            </div>
            <!-- Service 3 -->
            <div class="infy-card">
                <div class="infy-card-content">
                    <div class="infy-card-icon"><i class="mdi mdi-robot"></i></div>
                    <h3>Generative AI & LLM Systems</h3>
                    <p>Integrate conversational models and semantic intelligence agents into your workflows. We specialize in custom Large Language Model (LLM) fine-tuning, Retrieval-Augmented Generation (RAG) setups, and automated digital assistants.</p>
                </div>
            </div>
            <!-- Service 4 -->
            <div class="infy-card">
                <div class="infy-card-content">
                    <div class="infy-card-icon"><i class="mdi mdi-account-group-outline"></i></div>
                    <h3>HR Technology Solutions</h3>
                    <p>Optimize your recruitment, talent acquisition, and workforce retention using advanced analytics. We build talent search indexers, automated skill matching filters, and long-term organizational health forecasting systems.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Extra features -->
    <div class="infy-container" style="margin-top: 100px; text-align: center;">
        <h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 20px;">Why Partner With Us?</h2>
        <p style="color: var(--text-muted); max-width: 600px; margin: 0 auto 50px auto;">We go beyond standard software development to provide full-lifecycle integration and production guarantee.</p>
        <div class="infy-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));">
            <div class="infy-card" style="padding: 30px;">
                <div class="infy-card-content">
                    <h4>Besoke Customization</h4>
                    <p>No generic templates. Every platform is designed specifically for your unique industry logic and operating rules.</p>
                </div>
            </div>
            <div class="infy-card" style="padding: 30px;">
                <div class="infy-card-content">
                    <h4>Extreme Performance</h4>
                    <p>We write highly optimized microservices that handle billions of records with sub-millisecond response rates.</p>
                </div>
            </div>
            <div class="infy-card" style="padding: 30px;">
                <div class="infy-card-content">
                    <h4>Enterprise Sovereignty</h4>
                    <p>You retain 100% ownership of the custom models and databases. No vendor lock-in, ever.</p>
                </div>
            </div>
        </div>
    </div>
</div>
"""

    industries_content = """
<div class="infy-subpage-container" style="padding: 120px 20px 80px 20px;">
    <div style="max-width: 1280px; margin: 0 auto;">
        <h1 class="industry-hero-title">
            Powering the most critical sectors on the planet.
        </h1>
        
        <div class="industry-grid">
            <!-- Card 1 -->
            <div class="industry-card">
                <img src="https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&q=80&w=800" alt="Healthcare" class="industry-img" referrerpolicy="no-referrer" />
                <div class="industry-overlay"></div>
                <div class="industry-content">
                    <span class="industry-icon">🏥</span>
                    <h3 class="industry-title">Healthcare</h3>
                    <p class="industry-desc">Seamless integration of high-performance architecture tailored for healthcare compliance and scale.</p>
                </div>
            </div>
            <!-- Card 2 -->
            <div class="industry-card">
                <img src="https://images.unsplash.com/photo-1557821552-17105176677c?auto=format&fit=crop&q=80&w=800" alt="E-commerce" class="industry-img" referrerpolicy="no-referrer" />
                <div class="industry-overlay"></div>
                <div class="industry-content">
                    <span class="industry-icon">🛒</span>
                    <h3 class="industry-title">E-commerce</h3>
                    <p class="industry-desc">Seamless integration of high-performance architecture tailored for e-commerce compliance and scale.</p>
                </div>
            </div>
            <!-- Card 3 -->
            <div class="industry-card">
                <img src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&q=80&w=800" alt="Finance" class="industry-img" referrerpolicy="no-referrer" />
                <div class="industry-overlay"></div>
                <div class="industry-content">
                    <span class="industry-icon">💼</span>
                    <h3 class="industry-title">Finance</h3>
                    <p class="industry-desc">Seamless integration of high-performance architecture tailored for finance compliance and scale.</p>
                </div>
            </div>
            <!-- Card 4 -->
            <div class="industry-card">
                <img src="https://images.unsplash.com/photo-1541354329998-f447a4c92970?auto=format&fit=crop&q=80&w=800" alt="Banking" class="industry-img" referrerpolicy="no-referrer" />
                <div class="industry-overlay"></div>
                <div class="industry-content">
                    <span class="industry-icon">🏦</span>
                    <h3 class="industry-title">Banking</h3>
                    <p class="industry-desc">Seamless integration of high-performance architecture tailored for banking compliance and scale.</p>
                </div>
            </div>
        </div>
    </div>
</div>
"""

    contact_content = """
<div class="infy-subpage-container">
    <!-- Hero -->
    <div class="infy-hero">
        <div class="infy-container">
            <div class="infy-metric-tag" style="background: rgba(240, 90, 40, 0.1); color: var(--primary-orange); border-color: rgba(240, 90, 40, 0.2);">Connect With Us</div>
            <h1>Let's Build Something Smarter Together</h1>
            <p>Get in touch with our solutions engineering team to explore how bespoke AI and data science platforms can optimize your corporate operations.</p>
        </div>
    </div>
    
    <!-- Contact Info & Form -->
    <div class="infy-container">
        <div class="infy-contact-wrapper">
            <!-- Left Info -->
            <div class="infy-contact-info">
                <h2>Contact Information</h2>
                <p style="color: var(--text-muted); line-height: 1.6;">Our consulting team is available globally for technical workshops, architecture audits, and proof-of-concept reviews.</p>
                
                <div class="infy-contact-item">
                    <div class="infy-contact-icon"><i class="mdi mdi-map-marker"></i></div>
                    <div class="infy-contact-text">
                        <h4>Global Headquarters</h4>
                        <p>12th Floor, Infy Technology Tower, Silicon Valley, CA 94025</p>
                    </div>
                </div>
                
                <div class="infy-contact-item">
                    <div class="infy-contact-icon"><i class="mdi mdi-email-open-outline"></i></div>
                    <div class="infy-contact-text">
                        <h4>General Inquiry</h4>
                        <p>contact@infibytes.com</p>
                    </div>
                </div>
                
                <div class="infy-contact-item">
                    <div class="infy-contact-icon"><i class="mdi mdi-phone"></i></div>
                    <div class="infy-contact-text">
                        <h4>Direct Line</h4>
                        <p>+1 (800) 555-INFY</p>
                    </div>
                </div>
            </div>
            
            <!-- Right Form -->
            <div class="infy-contact-form-container">
                <div class="infy-success-msg" id="contactSuccessMsg">
                    <i class="mdi mdi-check-circle" style="font-size: 20px; vertical-align: middle; margin-right: 8px;"></i>
                    Your message has been sent successfully! Our engineering team will contact you shortly.
                </div>
                
                <form id="infyContactForm" onsubmit="event.preventDefault(); document.getElementById('contactSuccessMsg').style.display = 'block'; document.getElementById('infyContactForm').reset();">
                    <div class="infy-form-group">
                        <label for="contactName">Full Name</label>
                        <input type="text" id="contactName" class="infy-form-input" required placeholder="e.g. John Doe">
                    </div>
                    <div class="infy-form-group">
                        <label for="contactEmail">Work Email</label>
                        <input type="email" id="contactEmail" class="infy-form-input" required placeholder="e.g. john@yourcompany.com">
                    </div>
                    <div class="infy-form-group">
                        <label for="contactCompany">Company Name</label>
                        <input type="text" id="contactCompany" class="infy-form-input" required placeholder="e.g. Acme Corp">
                    </div>
                    <div class="infy-form-group">
                        <label for="contactMessage">How can we assist you?</label>
                        <textarea id="contactMessage" class="infy-form-input" rows="5" required placeholder="Describe your data/AI project requirements..."></textarea>
                    </div>
                    <button type="submit" class="infy-btn">
                        Submit Inquiry <i class="mdi mdi-send"></i>
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>
"""

    pages = {
        "about-us": ("About Us", about_content),
        "services": ("Services", services_content),
        "industries": ("Industries", industries_content),
        "contact-us": ("Contact Us", contact_content)
    }

    for folder, (title, content) in pages.items():
        # Ensure directories exist
        folder_path = f"g:/infybytes/{folder}"
        os.makedirs(folder_path, exist_ok=True)
        
        # Build subpage HTML
        header_p = make_subpage_header(title, folder)
        footer_p = make_subpage_footer()
        
        subpage_html = header_p + content + "\n\t\t\t\t" + footer_p
        
        out_file = os.path.join(folder_path, "index.html")
        with open(out_file, "w", encoding="utf-8") as out_f:
            out_f.write(subpage_html)
            
        print(f"Generated subpage: {out_file}")

if __name__ == "__main__":
    generate()
