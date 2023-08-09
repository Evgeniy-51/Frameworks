from jinja2 import Template

user = "Alex"
age = 34
tm = Template("Hello {{ name }}")
msg = tm.render(name=user)
print(msg)

tm = Template("My name is {{ a.upper() }}. I'm {{ b+2 }}")
msg = tm.render(a=user, b=age)
print(msg)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Ivan', 44)
tm = Template("My name is {{ a.name }}. I'm {{ a.age }}")
msg = tm.render(a=p1)
print(msg)


