import re

with open('assets/css/elements/button.css', 'r') as f:
    css = f.read()

# Replace .btn.btn.btn-- with .btn.btn--
css = css.replace('.btn.btn.btn--', '.btn.btn--')

with open('assets/css/elements/button.css', 'w') as f:
    f.write(css)

print("button.css cleanup updated!")
