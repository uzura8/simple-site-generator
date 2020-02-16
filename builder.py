import yaml
from jinja2 import Environment, FileSystemLoader
from common.filters import nl2br
from common.file import makedirs

def build_pages(tmpl_env, lang, lang_confs, is_default_lang=False):
    code = lang['code']
    conf_file = 'content/{}.yml'.format(code)
    with open(conf_file, 'r', encoding='utf8') as stream:
        confs = yaml.load(stream, Loader=yaml.FullLoader)

    comon = confs['common']
    for page, vals in confs.items():
        if page == 'common':
            continue
        file_name = page + '.html'
        tpl = tmpl_env.get_template(file_name)
        vals['common'] = comon
        vals['lang_code'] = code
        vals['lang_confs'] = lang_confs
        rendered = tpl.render(vals)

        if is_default_lang:
            output_path = 'public/'
        else:
            output_path = 'public/{}'.format(code)
            makedirs(output_path)

        output_file = '{}/{}'.format(output_path, file_name)
        with open(output_file, 'w', encoding='utf8') as fh:
            fh.write(rendered)


def find_from_dicts(dicts, key, val):
    for item in dicts:
        if key in item and item[key] == val:
            return item

    return None


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

langs = confs['lang']['langs']
for lang in langs:
    build_pages(env, lang, confs['lang'])

def_lang = confs['lang']['default']
lang = find_from_dicts(langs, 'code', def_lang)
build_pages(env, lang, confs['lang'], True)

print('Genarated!')

