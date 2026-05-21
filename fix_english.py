from pathlib import Path

fixes = {
    "Ligula hendrerit himenaeos maximus amet nulla a nibh integer. Fusce commodo aliquam cubilia eleifend in primis dictumst augue porta. Parturient aenean facilisi letius natoque dapibus metus feugiat ullamcorper fusce consectetuer augue.":
    "Infibytes Systems helps businesses transform complex data, AI, and automation challenges into clear, scalable, and intelligent digital solutions.",

    "Vehicula fermentum congue ligula elit velit nam quis. Nostra hac nibh posuere lorem penatibus praesent sodales ad egestas.":
    "Explore AI, data science, automation, HR technology, healthcare, retail, and finance solutions built for smarter business operations.",

    "Feugiat ultricies cubilia metus posuere nam enim tortor":
    "Trusted by businesses for reliable, scalable, and intelligent technology solutions.",

    "Magnis litora aptent quisque consectetuer mollis imperdiet iaculis convallis. Sem aenean mollis aliquet class litora vivamus luctus faucibus suscipit cras laoreet. Quis mi ad eleifend ante risus viverra primis class ultricies consequat.":
    "Our team combines AI expertise, data-driven thinking, and practical execution to build reliable solutions that improve operations and support business growth.",

    "Amet convallis netus dis vitae mus gravida suscipit":
    "We help businesses automate workflows, connect systems, and make faster decisions with intelligent tools.",

    "Laoreet consectetuer sapien finibus libero habitant. Volutpat phasellus bibendum molestie habitasse quis lacus.":
    "Choose smart technology solutions that reduce manual effort, improve accuracy, and help your team work faster.",

    "Sagittis nullam tincidunt lobortis morbi facilisi dapibus":
    "Built to improve efficiency, accuracy, scalability, and long-term business performance.",

    "Elit nullam rutrum euismod blandit quisque nibh penatibus nostra. Vestibulum ultricies sapien facilisi pede id pellentesque. Turpis dolor magna dictumst congue litora parturient si erat aptent.":
    "We build generative AI and LLM systems that help businesses search documents, automate workflows, answer questions, and improve productivity.",

    "Nam tristique lobortis nibh leo lacus diam lectus gravida purus":
    "We analyze your needs, design the solution, implement it carefully, and optimize it for continuous improvement.",

    "Happy Clients": "Satisfied Clients",
    "Project Done": "Projects Delivered",
    "Top-Rated Expert": "Expert Team",
    "Tailored Business Solutions": "Custom Business Solutions",
    "INFIBYTE SYSTEMS": "INFIBYTES SYSTEMS",
    "@ 2026 Infibytes Systems, All Rights Reserved.": "© 2026 Infibytes Systems, All Rights Reserved.",
}

bad_words = [
    "lorem", "ipsum", "litora", "consectetuer", "cubilia", "facilisi",
    "dapibus", "nullam", "tristique", "gravida", "aptent", "phasellus",
    "hendrerit", "himenaeos", "laoreet", "sagittis", "mollis",
    "penatibus", "dictumst", "bibendum", "rutrum"
]

for file in Path(".").rglob("*"):
    if file.suffix.lower() not in [".html", ".js", ".jsx", ".ts", ".tsx"]:
        continue

    text = file.read_text(encoding="utf-8", errors="ignore")
    old = text

    for wrong, right in fixes.items():
        text = text.replace(wrong, right)

    # remove duplicate footer issue
    text = text.replace(
        "<li>Report an Issue</li>\n<li>Report an Issue</li>",
        "<li>Report an Issue</li>"
    )
    text = text.replace(
        "Report an Issue\n\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tReport an Issue",
        "Report an Issue"
    )

    file.write_text(text, encoding="utf-8")

    if text != old:
        print("Fixed:", file)

print("\nChecking remaining dummy Latin words...\n")

failed = False
for file in Path(".").rglob("*"):
    if file.suffix.lower() not in [".html", ".js", ".jsx", ".ts", ".tsx"]:
        continue

    text = file.read_text(encoding="utf-8", errors="ignore").lower()

    for word in bad_words:
        if word in text:
            print(f"Still found '{word}' in {file}")
            failed = True

if failed:
    raise SystemExit("\nSome dummy words still remain. Fix those files before pushing.")
else:
    print("Clean. No dummy Latin words found.")
