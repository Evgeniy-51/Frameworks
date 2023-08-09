from jinja2 import Template

data = """{% raw %} Модуль Jinja вместо 
определения {{ name }} HE
подставляет соответствующее значение {% endraw %}"""
tm = Template(data)
msg = tm.render(name='Alex')
print(msg)

link = """В HTML-документе ссылки определяются так:
<a href="#">Ссылка <a>"""
tm = Template(link)
tm2 = Template("{{ link | e}}")
msg = tm.render()
msg2 = tm.render(link=link)
print(msg)
print(msg2)

cities = [{'id': 1, 'city': 'Moskow'},
          {'id': 3, 'city': 'Tver'},
          {'id': 23, 'city': 'Riga'},
          {'id': 45, 'city': 'Kiev'}]

link = """
<select name="cities">
{% for c in cities -%}
{% if c.id > 6 -%} 
    <option value="{{c.id}}">{{c.city}}</option>
{% else -%}
    {{c.city}}
{% endif -%}
{% endfor -%}
</select>"""
tm = Template(link)
msg = tm.render(cities=cities)
print(msg)

