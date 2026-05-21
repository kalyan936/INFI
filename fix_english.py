from pathlib import Path

replacements = {
    "Ligula hendrerit himenaeos maximus amet nulla a nibh integer. Fusce commodo aliquam cubilia eleifend in primis dictumst augue porta. Parturient aenean facilisi letius natoque dapibus metus feugiat ullamcorper fusce consectetuer augue.":
    "Infibytes Systems helps businesses use AI, data science, automation, and cloud technology to improve operations, reduce manual effort, and make smarter decisions.",

    "Vehicula fermentum congue ligula elit velit nam quis. Nostra hac nibh posuere lorem penatibus praesent sodales ad egestas.":
    "We build practical technology solutions that solve real business problems and support long-term growth.",

    "Feugiat ultricies cubilia metus posuere nam enim tortor":
    "Trusted solutions delivered with quality, speed, and measurable business impact.",

    "Magnis litora aptent quisque consectetuer mollis imperdiet iaculis convallis. Sem aenean mollis aliquet class litora vivamus luctus faucibus suscipit cras laoreet. Quis mi ad eleifend ante risus viverra primis class ultricies consequat.":
    "Our team brings together AI engineers, data specialists, cloud experts, and business consultants to deliver reliable digital solutions.",

    "Amet convallis netus dis vitae mus gravida suscipit":
    "Smart, scalable solutions designed for modern business needs.",

    "Laoreet consectetuer sapien finibus libero habitant. Volutpat phasellus bibendum molestie habitasse quis lacus.":
    "Explore our services and discover how Infibytes Systems can help your business work faster, smarter, and more efficiently.",

    "Sagittis nullam tincidunt lobortis morbi facilisi dapibus":
    "Built with secure architecture, scalable design, and business-focused execution.",

    "Elit nullam rutrum euismod blandit quisque nibh penatibus nostra. Vestibulum ultricies sapien facilisi pede id pellentesque. Turpis dolor magna dictumst congue litora parturient si erat aptent.":
    "We design Generative AI and LLM systems that help businesses automate knowledge work, improve customer support, and speed up decision-making.",

    "Nam tristique lobortis nibh leo lacus diam lectus gravida purus":
    "We study your business needs, design the right solution, implement it carefully, and continuously improve performance.",

    "Besoke Customization":
    "Bespoke Customization",

    "Contact Infibyte":
    "Contact Infibytes",

    "Project Done":
    "Projects Delivered",

    "@ 2026 Infibytes Systems, All Rights Reserved.":
    "© 2026 Infibytes Systems. All Rights Reserved."
}

files = [
    Path("index.html"),
    Path("services/index.html"),
    Path("about-us/index.html"),
    Path("industries/index.html"),
    Path("contact-us/index.html"),
]

for file in files:
    if file.exists():
        text = file.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        file.write_text(text, encoding="utf-8")

print("English content fixed.")
