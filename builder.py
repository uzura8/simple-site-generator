import yaml
from jinja2 import Environment, FileSystemLoader
from common.filters import nl2br
from common.file import makedirs

def build_pages(tmpl_env, lang, is_default_lang=False):
    conf_file = 'content/{}.yml'.format(lang)
    with open(conf_file, 'r', encoding='utf8') as stream:
        confs = yaml.load(stream, Loader=yaml.FullLoader)

    comon = confs['common']
    for page, vals in confs.items():
        if page == 'common':
            continue
        file_name = page + '.html'
        tpl = tmpl_env.get_template(file_name)
        vals['common'] = comon
        rendered = tpl.render(vals)

        if is_default_lang:
            output_path = 'public/'
        else:
            output_path = 'public/{}'.format(lang)
            makedirs(output_path)

        output_file = '{}/{}'.format(output_path, file_name)
        with open(output_file, 'w', encoding='utf8') as fh:
            fh.write(rendered)


env = Environment(
    loader=FileSystemLoader('templates'),
    #block_start_string='[%',
    #block_end_string='%]',
    #variable_start_string='[[',
    #variable_end_string=']]',
    #comment_start_string='[#',
    #comment_end_string='#]'
)
env.filters['nl2br'] = nl2br

with open('config.yml', 'r', encoding='utf8') as stream:
    confs = yaml.load(stream, Loader=yaml.FullLoader)

for lang in confs['lang']['items']:
    build_pages(env, lang)

build_pages(env, confs['lang']['default'], True)

print('Genarated!')

