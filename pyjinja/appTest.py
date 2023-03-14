from jinja2 import FileSystemLoader, Environment

loader = FileSystemLoader("template")
env = Environment(loader=loader)
template = env.get_template('homepage.html')

file = open('output/index.html', 'w') 

render = template.render(tittle="Jinja test", color_background="#fff", color_letter="#000", name='Alexandre')

file.write(render)
file.close() 