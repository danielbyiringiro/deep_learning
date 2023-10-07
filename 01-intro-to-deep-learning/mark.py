import markdown

with open('readme.md', 'r') as f:
    md_text = f.read()

html = markdown.markdown(md_text)

with open('readme.html', 'w') as f:
    f.write(html)
    