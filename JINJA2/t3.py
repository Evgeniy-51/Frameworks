from jinja2 import Template

digs = [2, 33, 17]
ex = "Сумма чисел {{ l | sum }}"
tm = Template(ex)
msg = tm.render(l=digs)
print(msg)

cars = [
    {'model': 'Audi', 'price': 5_000_000},
    {'model': 'Volvo', 'price': 4_500_000},
    {'model': 'Kia', 'price': 2_200_000},
    {'model': 'Lada', 'price': 600_000},
]
tpl = "Суммарная цена автомобилей {{ cars | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cars=cars)
print(msg)

tpl = "Самый дешевый автомобиль: {{ (cs | min(attribute='price')).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

tpl = "Случайный автомобиль: {{ (cs | random) | replace('a', 'A') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

tpl = """
{% for c in cars -%}
{% filter upper %}{{c.model}}{% endfilter %}
{% endfor %}
"""
tm = Template(tpl)
msg = tm.render(cars=cars)
print(msg)


