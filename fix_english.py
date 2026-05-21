from pathlib import Path
import re

bad_words = r"(lorem|ipsum|litora|consectetuer|cubilia|facilisi|dapibus|nullam|tristique|gravida|aptent|phasellus|hendrerit|himenaeos|laoreet|sagittis|morbi|ultricies|mollis|penatibus|dictumst|bibendum|rutrum)"

default_text = {
    "hero": "Infibytes Systems helps businesses use AI, data, cloud, and automation to solve real problems and build smarter digital operations.",
    "about": "We work with businesses to understand their challenges, design the right solution, and deliver reliable technology that improves speed, accuracy, and performance.",
    "services": "Our solutions help teams reduce manual work, improve decision-making, and scale operations with secure and intelligent technology.",
    "ai": "We build AI and generative AI systems that help businesses automate workflows, search documents, answer questions, and improve productivity.",
    "process": "We analyze your requirements, plan the solution, build it carefully, test it properly, and improve it continuously.",
    "short": "Built to improve efficiency, accuracy, and business growth."
}

def pick_text(context):
    c = context.lower()
    if "about" in c or "together" in c:
        return default_text["about"]
    if "solution" in c or "service" in c:
        return default_text["services"]
    if "generative" in c or "ai" in c or "llm" in c:
        return default_text["ai"]
    if "analyze" in c or "process" in c:
        return default_text["process"]
    return default_text["short"]

for file in Path(".").rglob("*"):
    if file.suffix.lower() not in [".html", ".js", ".jsx", ".ts", ".tsx"]:
        continue

    text = file.read_text(encoding="utf-8", errors="ignore")
    old = text

    # Fix text inside HTML tags
    def replace_bad(match):
        content = match.group(2)
        if re.search(bad_words, content, re.I):
            before = text[max(0, match.start()-500):match.start()]
            return match.group(1) + pick_text(before) + match.group(3)
        return match.group(0)

    text = re.sub(r"(>)([^<>]*" + bad_words + r"[^<>]*)(<)", replace_bad, text, flags=re.I)

    # Fix common labels
    text = text.replace("Project Done", "Projects Delivered")
    text = text.replace("Happy Clients", "Satisfied Clients")
    text = text.replace("Top-Rated Expert", "Expert Team")
    text = text.replace("Tailored Business Solutions", "Custom Business Solutions")
    text = text.replace("Besoke Customization", "Bespoke Customization")

    if text != old:
        file.write_text(text, encoding="utf-8")
        print("Fixed:", file)

print("Done. Now run grep to check remaining dummy words.")
