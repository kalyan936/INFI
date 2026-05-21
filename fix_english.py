from pathlib import Path

fixes = {
"Ligula hendrerit himenaeos maximus amet nulla a nibh integer. Fusce commodo aliquam cubilia eleifend in primis dictumst augue porta. Parturient aenean facilisi letius natoque dapibus metus feugiat ullamcorper fusce consectetuer augue.":
"Infibytes Systems helps businesses use AI, data science, automation, and cloud technologies to solve real problems with simple, scalable, and intelligent digital solutions.",

"Vehicula fermentum congue ligula elit velit nam quis. Nostra hac nibh posuere lorem penatibus praesent sodales ad egestas.":
"Explore our AI, data science, generative AI, HR technology, healthcare, retail, and finance solutions built for smarter business operations.",

"Feugiat ultricies cubilia metus posuere nam enim tortor":
"Trusted by businesses for reliable, intelligent, and scalable technology solutions.",

"Magnis litora aptent quisque consectetuer mollis imperdiet iaculis convallis. Sem aenean mollis aliquet class litora vivamus luctus faucibus suscipit cras laoreet. Quis mi ad eleifend ante risus viverra primis class ultricies consequat.":
"Our team combines AI expertise, business understanding, and practical execution to build reliable solutions that improve operations and support long-term growth.",

"Amet convallis netus dis vitae mus gravida suscipit":
"We help businesses automate work, connect systems, and make faster decisions with clean data and intelligent tools.",

"Laoreet consectetuer sapien finibus libero habitant. Volutpat phasellus bibendum molestie habitasse quis lacus.":
"Choose intelligent solutions that reduce manual effort, improve accuracy, and help your team work faster with modern technology.",

"Sagittis nullam tincidunt lobortis morbi facilisi dapibus":
"Our solutions are secure, scalable, and built around your business needs.",

"Elit nullam rutrum euismod blandit quisque nibh penatibus nostra. Vestibulum ultricies sapien facilisi pede id pellentesque. Turpis dolor magna dictumst congue litora parturient si erat aptent.":
"We build generative AI and LLM systems that help businesses search documents, automate workflows, answer questions, and improve productivity.",

"Nam tristique lobortis nibh leo lacus diam lectus gravida purus":
"We understand the requirement, plan the solution, build it carefully, test it properly, and improve it continuously.",

"Project Done": "Projects Delivered",
"Happy Clients": "Satisfied Clients",
"Top-Rated Expert": "Expert Team",
"Tailored Business Solutions": "Custom Business Solutions",
"INFIBYTE SYSTEMS": "INFIBYTES SYSTEMS",
"@ 2026 Infibytes Systems": "© 2026 Infibytes Systems",
}

for file in Path(".").rglob("*"):
    if file.suffix.lower() not in [".html", ".js", ".jsx", ".ts", ".tsx"]:
        continue

    text = file.read_text(encoding="utf-8", errors="ignore")
    old = text

    for wrong, right in fixes.items():
        text = text.replace(wrong, right)

    text = text.replace(
        "<li>Report an Issue</li>\n<li>Report an Issue</li>",
        "<li>Report an Issue</li>"
    )

    if text != old:
        file.write_text(text, encoding="utf-8")
        print("Fixed:", file)
