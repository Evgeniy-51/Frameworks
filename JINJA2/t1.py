from jinja2 import Template

name = "Alex"

tm = Template("Hello {{ name }}")
msg = tm.render(name=name)

print(msg)