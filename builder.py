import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('templates'),
    #block_start_string='[%',
    #block_end_string='%]',
    #variable_start_string='[[',
    #variable_end_string=']]',
    #comment_start_string='[#',
    #comment_end_string='#]'
)


with open('config.yml', 'r') as stream:
    confs = yaml.load(stream)

comon = confs['common']
for page, vals in confs.items():
    if page == 'common':
        continue
    file_name = page + '.html'
    tpl = env.get_template(file_name)
    vals['common'] = comon
    rendered = tpl.render(vals)
    with open('public/' + file_name, 'w') as fh:
        fh.write(rendered)

print('Genarated!')

