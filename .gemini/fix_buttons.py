import re

with open('assets/css/elements/button.css', 'r') as f:
    css = f.read()

# Replace .btn--xxx:hover with .btn.btn--xxx:hover to increase specificity to 0,3,0
css = re.sub(r'\.btn--([a-zA-Z0-9-]+):hover', r'.btn.btn--\1:hover, .btn.btn--\1:active', css)
css = re.sub(r'\.btn--([a-zA-Z0-9-]+):active', r'.btn.btn--\1:active', css)

# Wait, if we replace :hover with :hover and :active, then the active state will just be the hover state! That's good enough for most, and for the outline-primary we already defined :active so it will be duplicated but that's fine. Wait, if we duplicate, .btn.btn--outline-primary:active will be defined twice. The second one (the explicit one) will override the hover one! That's perfect.

# Let's run this precisely.
with open('assets/css/elements/button.css', 'w') as f:
    f.write(css)

print("button.css updated!")
