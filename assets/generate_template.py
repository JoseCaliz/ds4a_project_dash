import os

index_string = './index.html'

with open(index_string, 'r') as f:
    page = f.read()

full_template_vanilla = (
    page
)
