#!/usr/bin/env python3
"""Markdown to PDF converter for AI 트렌드 온보딩 완벽 가이드"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path
import re

BASE_DIR = Path("/Users/robin/Downloads/ai-trend-onboarding")
WORKSPACE = BASE_DIR / "_workspace"
OUTPUT_DIR = BASE_DIR / "output"
IMAGES_DIR = OUTPUT_DIR / "images"
MD_FILE = WORKSPACE / "book-complete.md"
PDF_FILE = OUTPUT_DIR / "AI-트렌드-온보딩-완벽가이드.pdf"

# Read markdown
md_text = MD_FILE.read_text(encoding="utf-8")

# Fix image paths to absolute
md_text = md_text.replace("](images/", f"]({IMAGES_DIR}/")

# Convert markdown to HTML
html_body = markdown.markdown(
    md_text,
    extensions=["tables", "fenced_code", "toc", "attr_list", "md_in_html"],
    output_format="html5",
)

# CSS styling
css_text = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

@page {
    size: A4;
    margin: 2.2cm 2cm 2.5cm 2cm;
    @bottom-center {
        content: counter(page);
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 9pt;
        color: #888;
    }
}

@page :first {
    @bottom-center { content: none; }
    margin-top: 0;
    margin-bottom: 0;
}

body {
    font-family: 'Noto Sans KR', 'Apple SD Gothic Neo', sans-serif;
    font-size: 10.5pt;
    line-height: 1.75;
    color: #2d2d2d;
    text-align: justify;
    word-break: keep-all;
}

/* Cover page - first h1 */
h1:first-of-type {
    page-break-before: avoid;
    font-size: 28pt;
    font-weight: 900;
    color: #1a1a2e;
    text-align: center;
    margin-top: 6cm;
    margin-bottom: 0.3cm;
    border-bottom: none;
    letter-spacing: 2px;
}

/* Subtitle after cover */
h1:first-of-type + h3 {
    text-align: center;
    font-size: 13pt;
    font-weight: 400;
    color: #555;
    margin-top: 0.5cm;
    margin-bottom: 1cm;
}

h1 {
    font-size: 22pt;
    font-weight: 900;
    color: #1a1a2e;
    border-bottom: 3px solid #4361ee;
    padding-bottom: 8px;
    margin-top: 1.5cm;
    margin-bottom: 0.8cm;
    page-break-before: always;
    letter-spacing: 1px;
}

h2 {
    font-size: 15pt;
    font-weight: 700;
    color: #2d3a8c;
    border-left: 4px solid #4361ee;
    padding-left: 12px;
    margin-top: 1.2cm;
    margin-bottom: 0.5cm;
}

h3 {
    font-size: 12.5pt;
    font-weight: 700;
    color: #3d405b;
    margin-top: 0.8cm;
    margin-bottom: 0.4cm;
}

h4 {
    font-size: 11pt;
    font-weight: 700;
    color: #555;
    margin-top: 0.5cm;
    margin-bottom: 0.3cm;
}

/* Blockquote - summary boxes */
blockquote {
    background: #f0f4ff;
    border-left: 4px solid #4361ee;
    padding: 12px 16px;
    margin: 0.5cm 0;
    border-radius: 0 8px 8px 0;
    font-size: 10pt;
    color: #333;
}

blockquote strong {
    color: #2d3a8c;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.5cm 0;
    font-size: 9.5pt;
    page-break-inside: auto;
}

thead {
    background: #4361ee;
    color: white;
}

th {
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
    font-size: 9pt;
}

td {
    padding: 7px 10px;
    border-bottom: 1px solid #e0e0e0;
}

tr:nth-child(even) {
    background: #f8f9ff;
}

tr {
    page-break-inside: avoid;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 0.8cm auto;
    border-radius: 8px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}

/* Code */
code {
    background: #f4f4f8;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 9pt;
    font-family: 'SF Mono', 'Menlo', monospace;
    color: #d63384;
}

pre {
    background: #1e1e2e;
    color: #cdd6f4;
    padding: 14px 18px;
    border-radius: 8px;
    font-size: 8.5pt;
    line-height: 1.5;
    overflow-x: auto;
    page-break-inside: avoid;
    margin: 0.4cm 0;
}

pre code {
    background: none;
    color: inherit;
    padding: 0;
    font-size: 8.5pt;
}

/* Lists */
ul, ol {
    margin: 0.3cm 0;
    padding-left: 1.2cm;
}

li {
    margin-bottom: 4px;
}

/* Horizontal rule */
hr {
    border: none;
    border-top: 1px solid #ddd;
    margin: 0.8cm 0;
}

/* Links */
a {
    color: #4361ee;
    text-decoration: none;
}

/* Bold text */
strong {
    font-weight: 700;
    color: #1a1a2e;
}

/* TOC styling */
.toc ul {
    list-style: none;
    padding-left: 0;
}
.toc li {
    padding: 4px 0;
    border-bottom: 1px dotted #ccc;
}

/* Page break hints */
h1, h2 {
    page-break-after: avoid;
}

p, blockquote, table {
    orphans: 3;
    widows: 3;
}

/* 알아두기 boxes */
blockquote blockquote {
    background: #fff8e1;
    border-left-color: #ffc107;
}

/* Emoji-like markers */
p > strong:first-child {
    color: #2d3a8c;
}
"""

# Wrap in full HTML
full_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI 트렌드 온보딩 완벽 가이드</title>
</head>
<body>
{html_body}
</body>
</html>"""

print("Converting to PDF...")
html_doc = HTML(string=full_html, base_url=str(BASE_DIR))
css = CSS(string=css_text)
html_doc.write_pdf(str(PDF_FILE), stylesheets=[css])

print(f"PDF generated: {PDF_FILE}")
print(f"File size: {PDF_FILE.stat().st_size / 1024 / 1024:.1f} MB")
