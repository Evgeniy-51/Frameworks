from jinja2 import Template

html = """
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}"
{%- endmacro -%}

<p>{{ input('username', size=55) }}<p>
<p>{{ input('email', value='adress@mail.com') }}<p>
<p>{{ input('password') }}<p>
"""
tm = Template(html)
msg = tm.render()
print(msg)


