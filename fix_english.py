from pathlib import Path
import re

# Common latin/dummy website words
latin_words = [
    "lorem", "ipsum", "dolor", "amet", "consectetuer",
    "adipiscing", "elit", "nullam", "phasellus",
    "dapibus", "litora", "cubilia", "facilisi",
    "hendrerit", "himenaeos", "tristique", "gravida",
    "aptent", "bibendum", "penatibus", "dictumst",
    "mollis", "ultricies", "rutrum", "morbi",
    "laoreet", "sagittis"
]

# English replacement sentences
english_sentences = [
    "We provide innovative AI and cloud solutions for modern businesses.",
    "Our platform helps organizations automate operations and improve productivity.",
    "We build scalable software systems designed for long-term business growth.",
    "Our team delivers reliable technology solutions with strong performance and security.",
    "We help businesses transform complex workflows into simple digital experiences.",
    "Our services improve efficiency, reduce manual effort, and increase operational accuracy.",
    "We create intelligent systems powered by AI, analytics, and automation.",
    "Our solutions are designed to support smarter decisions and faster execution.",
    "We focus on building practical technology that solves real business problems.",
    "Our company combines innovation, strategy, and engineering excellence."
]

latin_pattern = re.compile(
    r'\b(' + '|'.join(latin_words) + r')\b',
    re.IGNORECASE
)

sentence_index = 0

def replace_latin_paragraph(text):
    global sentence_index

    # split into paragraphs
    parts = re.split(r'(\n+)', text)

    for i, part in enumerate(parts):
        word_count = len(part.split())

        # detect latin-heavy paragraph
        latin_matches = latin_pattern.findall(part)

        if len(latin_matches) >= 2 and word_count > 4:
            parts[i] = english_sentences[
                sentence_index % len(english_sentences)
            ]
            sentence_index += 1

    return ''.join(parts)

# scan all website files
for file in Path(".").rglob("*"):
    if file.suffix.lower() not in [
        ".html", ".js", ".jsx",
        ".ts", ".tsx", ".css"
    ]:
        continue

    try:
        content = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        updated = replace_latin_paragraph(content)

        if updated != content:
            file.write_text(updated, encoding="utf-8")
            print("Fixed:", file)

    except Exception as e:
        print("Error:", file, e)

print("Latin text replacement completed.")
