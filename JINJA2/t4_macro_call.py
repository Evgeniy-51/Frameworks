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

cars = [
    {'model': 'Audi', 'price': 5_000_000},
    {'model': 'Volvo', 'price': 4_500_000},
    {'model': 'Kia', 'price': 2_200_000},
    {'model': 'Lada', 'price': 600_000},
]

html = """
{% macro list_cars(list_of_cars) -%}
<ul>
{%- for i in list_of_cars %}
    <li>{{i.model.upper()}} {{caller(i)}}<li>
{%- endfor %}
<ul>
{%- endmacro %}

{% call(car) list_cars(cars) %}
    <ul>
        <li>Model: {{car.model}}
        <li>Price: {{car.price}}
    <ul>
{% endcall -%}
"""
tm = Template(html)
msg = tm.render(cars=cars)
print(msg)
