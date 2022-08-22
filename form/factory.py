import json
import yaml
from typing import List, Dict

from form.qmodel import *
from visitor import *

node_factory = {
    'sheet': Sheet,
    'check': CheckGroup,
    'radio': CheckGroup,
    'option_input': OptionInput,
    'option': Option,
    'text': InputText,
    'digit': InputDigit,
    'float': InputFloat,
    'date': InputDate,
}


def create_tree(item: Dict, parent: InputItem = None):
    dict_type = item.get('_type')
    input_items = []
    if dict_type in ['sheet', 'radio', 'check', 'option_input']:
        child_input_items = item.pop('input_items')
        node = node_factory[dict_type](item)
        for item in child_input_items:
            child = create_tree(item, node)
            if child:
                input_items.append(child)
        node.input_items = input_items
    elif dict_type in ['text', 'digit', 'float', 'date', 'option']:
        node = node_factory[dict_type](item)
    if parent:
        node.parent = parent
    return node


def export_json(s: Sheet):
    print(s.to_json())


def output_text(s: Sheet):
    text_output = TextOutput()
    print(text_output.visit(s))


def read_sheet(yml_file: str):
    questions_dict = {}
    with open(f'{yml_file}', 'r') as stream:
        try:
            questions_dict.update(yaml.safe_load(stream))
        except Exception as e:
            print(e)

    return questions_dict


if __name__ == '__main__':
    sheet_dict = read_sheet('./qsample.yml')
    # print(sheet_dict)
    sheet = create_tree(sheet_dict)
    export_json(sheet)
    output_text(sheet)

