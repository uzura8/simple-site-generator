import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
tpl = env.get_template('index.html')

with open('config.yml', 'r') as stream:
    confs = yaml.load(stream, Loader=yaml.FullLoader)

rendered = tpl.render(confs)

with open('public/index.html', 'w') as fh:
    fh.write(rendered)

print('Genarated!')

