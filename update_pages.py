import re

# 1. Update Industries page with the new bank image
with open('industries/index.html', 'r', encoding='utf-8') as f:
    ind_content = f.read()

# Replace the unsplash URL with the new bank image
unsplash_url = "https://images.unsplash.com/photo-1541354329998-f447a4c92970?auto=format&fit=crop&q=80"
new_bank_img = "./bank.png"

ind_content = ind_content.replace(unsplash_url, new_bank_img)

with open('industries/index.html', 'w', encoding='utf-8') as f:
    f.write(ind_content)
print("Updated industries/index.html")

# 2. Update Contact Us page
with open('contact-us/index.html', 'r', encoding='utf-8') as f:
    contact_content = f.read()

# The content to replace is between </header> and <footer
start_marker = "</header>"
end_marker = '<footer data-elementor-type="footer"'

start_idx = contact_content.find(start_marker)
end_idx = contact_content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    start_idx += len(start_marker)
    
    # We will build the new HTML for the contact page based on the React code.
    new_contact_html = """
<style>
    .new-contact-section {
        background-color: #0d1117;
        color: #fff;
        font-family: 'Inter Tight', sans-serif;
        padding: 80px 20px;
    }
    .new-contact-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    .new-contact-header {
        text-align: center;
        margin-bottom: 80px;
    }
    .new-contact-tag {
        color: #00d084;
        font-family: monospace;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .new-contact-title {
        font-size: 48px;
        font-weight: 700;
        margin: 20px 0;
        letter-spacing: -1px;
    }
    @media(min-width: 768px) {
        .new-contact-title { font-size: 64px; }
    }
    .new-contact-desc {
        max-width: 800px;
        margin: 0 auto;
        font-size: 20px;
        color: #a3a3a3;
        line-height: 1.6;
    }
    .new-contact-grid {
        display: grid;
        grid-template-columns: 1fr;
        gap: 40px;
    }
    @media(min-width: 1024px) {
        .new-contact-grid { grid-template-columns: 1fr 1fr; }
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 40px;
        backdrop-filter: blur(10px);
    }
    .glass-card h2 {
        font-size: 30px;
        font-weight: 700;
        margin-bottom: 24px;
    }
    .glass-card p.subtitle {
        color: #a3a3a3;
        font-size: 16px;
        line-height: 1.6;
        margin-bottom: 32px;
    }
    .contact-info-list {
        display: flex;
        flex-direction: column;
        gap: 24px;
    }
    .contact-info-item {
        display: flex;
        gap: 16px;
    }
    .contact-icon-wrap {
        width: 48px;
        height: 48px;
        flex-shrink: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #00d084;
    }
    .contact-info-item-text h4 {
        font-size: 16px;
        font-weight: 600;
        margin: 0 0 4px 0;
    }
    .contact-info-item-text p {
        margin: 0;
        color: #a3a3a3;
        font-size: 16px;
        line-height: 1.6;
    }
    .focus-areas-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
        margin-top: 24px;
    }
    .focus-area-tag {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 12px 16px;
        color: #d4d4d4;
        font-size: 14px;
    }
    
    .contact-form {
        display: flex;
        flex-direction: column;
        gap: 24px;
    }
    .form-group {
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .form-row {
        display: grid;
        grid-template-columns: 1fr;
        gap: 24px;
    }
    @media(min-width: 640px) {
        .form-row { grid-template-columns: 1fr 1fr; }
    }
    .form-group label {
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 700;
        color: #737373;
    }
    .form-control {
        width: 100%;
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 16px;
        color: #fff;
        font-size: 16px;
        transition: border-color 0.3s;
        box-sizing: border-box;
    }
    .form-control::placeholder {
        color: #525252;
    }
    .form-control:focus {
        outline: none;
        border-color: #00d084;
    }
    select.form-control {
        appearance: none;
    }
    select.form-control option {
        background: #0d1117;
        color: #fff;
    }
    .submit-btn {
        width: 100%;
        padding: 16px;
        background: #00d084;
        color: #0d1117;
        font-weight: 700;
        font-size: 16px;
        border-radius: 12px;
        border: none;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        transition: transform 0.2s;
    }
    .submit-btn:hover {
        transform: scale(1.02);
    }
    .submit-btn:active {
        transform: scale(0.98);
    }
    .mdi-icon {
        font-size: 20px;
    }
</style>

<div class="new-contact-section">
    <div class="new-contact-container">
        <div class="new-contact-header">
            <span class="new-contact-tag">Contact Infibyte</span>
            <h1 class="new-contact-title">Let’s Build Something Intelligent.</h1>
            <p class="new-contact-desc">Connect with us for AI solutions, automation, data engineering, cloud infrastructure, DevOps, or talent resourcing support.</p>
        </div>

        <div class="new-contact-grid">
            
            <div style="display: flex; flex-direction: column; gap: 32px;">
                <div class="glass-card">
                    <h2>Reach Our Team</h2>
                    <p class="subtitle">Share your business requirement, hiring need, or technology challenge. Our team will review it and connect with you.</p>
                    
                    <div class="contact-info-list">
                        <div class="contact-info-item">
                            <div class="contact-icon-wrap"><i class="mdi mdi-map-marker mdi-icon"></i></div>
                            <div class="contact-info-item-text">
                                <h4>Office Address</h4>
                                <p>#52, 3rd Cross, Aswath Nagar, Marathahalli, Bengaluru, Karnataka - 560037</p>
                            </div>
                        </div>
                        <div class="contact-info-item">
                            <div class="contact-icon-wrap"><i class="mdi mdi-email mdi-icon"></i></div>
                            <div class="contact-info-item-text">
                                <h4>HR & Careers</h4>
                                <p>hr@infibytetech.com</p>
                            </div>
                        </div>
                        <div class="contact-info-item">
                            <div class="contact-icon-wrap"><i class="mdi mdi-domain mdi-icon"></i></div>
                            <div class="contact-info-item-text">
                                <h4>Business Inquiries</h4>
                                <p>manjunath@infibytetech.com</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="glass-card">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 24px; margin-top: 0;">What We Can Help With</h3>
                    <div class="focus-areas-grid">
                        <div class="focus-area-tag">HR Consulting</div>
                        <div class="focus-area-tag">AI Solutions</div>
                        <div class="focus-area-tag">Generative AI</div>
                        <div class="focus-area-tag">AI Agents</div>
                        <div class="focus-area-tag">Data Engineering</div>
                        <div class="focus-area-tag">DevOps & Cloud</div>
                    </div>
                </div>
            </div>

            <div class="glass-card">
                <h2>Send An Inquiry</h2>
                <form class="contact-form" onsubmit="event.preventDefault(); alert('Inquiry sent successfully!');">
                    <div class="form-row">
                        <div class="form-group">
                            <label>First Name</label>
                            <input type="text" placeholder="Enter first name" class="form-control" required />
                        </div>
                        <div class="form-group">
                            <label>Last Name</label>
                            <input type="text" placeholder="Enter last name" class="form-control" required />
                        </div>
                    </div>
                    
                    <div class="form-group">
                        <label>Business Email</label>
                        <input type="email" placeholder="name@company.com" class="form-control" required />
                    </div>

                    <div class="form-group">
                        <label>Requirement</label>
                        <select class="form-control" required>
                            <option value="">Select a service</option>
                            <option value="hr">HR Consulting & Talent Resourcing</option>
                            <option value="ai">Data Science, AI & Generative AI Solutions</option>
                            <option value="agents">AI Agents & Intelligent Automation Solutions</option>
                            <option value="data">Data Engineering & Advanced Analytics</option>
                            <option value="cloud">DevOps & Cloud Infrastructure Services</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label>Project Details</label>
                        <textarea rows="5" placeholder="Tell us about your project, hiring need, or business challenge..." class="form-control" style="resize: none;" required></textarea>
                    </div>

                    <button type="submit" class="submit-btn">
                        Submit Inquiry <i class="mdi mdi-send"></i>
                    </button>
                </form>
            </div>
            
        </div>
    </div>
</div>
"""
    
    new_content = contact_content[:start_idx] + new_contact_html + "\n\t\t\t\t" + contact_content[end_idx:]
    with open('contact-us/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated contact-us/index.html")
else:
    print("Could not find boundaries in contact-us/index.html")

