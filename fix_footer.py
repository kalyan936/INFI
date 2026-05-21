footer_text_fixes = {
    "Enterprise\nAI\nSolutions": "Enterprise AI Solutions",
    "Advanced\nData\nScience": "Advanced Data Science",
    "Generative\nAI & LLM\nSystems": "Generative AI & LLM Systems",
    "HR\nTechnology\nSolutions": "HR Technology Solutions",
    "Banking\n&\nFinance\nAI": "Banking & Finance AI",
    "Contact\nUs": "Contact Us",
    "Case\nStudies": "Case Studies",
    "Help\nCenter": "Help Center",
    "AI\nGuides": "AI Guides",
    "Customer\nSupport": "Customer Support",
    "System\nStatus": "System Status",
    "Report\nan\nIssue": "Report an Issue",
}

for wrong, right in footer_text_fixes.items():
    content = content.replace(wrong, right)
