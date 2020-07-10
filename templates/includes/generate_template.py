import os


header = './templates/includes/header.html'
sidenav = './templates/includes/sidenav.html'
content = './templates/includes/content.html'
footer = './templates/includes/footer.html'


with open(header, 'r') as f:
    header_html = f.read()

with open(sidenav, 'r') as f:
    sidenav_html = f.read()

with open(content, 'r') as f:
    content_html = f.read()

with open(footer, 'r') as f:
    footer_html = f.read()

full_template_vanilla = (
    header_html
    + sidenav_html
    + content_html
    + footer_html
)
