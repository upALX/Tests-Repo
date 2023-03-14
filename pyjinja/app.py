import jinja2


template_jinja = 'Olá {{nome}}, seja bem bindo . Seu endereço de email é {{email}}. Seu estado é {{estado}}'


emails = [
    ['aborabora@gmail.com', 'seu abobora', 'Brasil'],
    ['morango@gmail.com', 'dona morango', 'Brasil'],
    ['melancia@gmail.com', 'dona melancia', 'Brasil']
]


template = jinja2.Template(template_jinja)


for email in emails:
    print(template.render(nome=email[1], email=email[0], estado=email[2]))