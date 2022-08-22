from abc import ABC
from typing import List
import json


class LoadDictMixin:
    def __init__(self, input_dict):
        for i in dir(self):
            if i[:2] == '__':
                pass  # 排除class的def
            elif i == '_abc_impl':
                pass
            elif i in input_dict.keys():
                setattr(self, i, input_dict[i])  # 更新傳入參數
            else:
                setattr(self, i, self.__getattribute__(i))  # 無傳入參數用預設值


class JsonMixin:
    def to_dict(self):
        result_dict = {}
        for key, value in vars(self).items():
            # convert without function
            if not (callable(value) or key == 'parent'):
                # result_dict[key] = copy(value)
                if key == 'input_items':
                    item_list = []
                    for item in value:
                        item_dict = item.to_dict()
                        item_list.append(item_dict)
                    result_dict[key] = item_list
                else:
                    result_dict[key] = value
        return result_dict

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)


class InputItem(ABC, LoadDictMixin, JsonMixin):
    id: str = ''
    _type: str = ''
    label: str = ''
    value: str = ''
    required: bool = False
    parent = None


class InputText(InputItem):
    _type: str = 'text'
    unit: str = ''
    length: int = 0
    placeholder: str = ''


class InputDigit(InputItem):
    _type: str = 'digit'
    unit: str = ''
    length: int = 0


class InputFloat(InputItem):
    _type: str = 'float'
    unit: str = ''
    length: int = 0


class InputDate(InputItem):
    _type: str = 'date'


class Option(InputItem):
    _type: str = 'option'


class OptionInput(InputItem):
    _type: str = 'option_input'
    input_items: List['InputItem'] = []
    new_line: bool = False


class InputDate(InputItem):
    _type: str = 'date'


class CheckGroup(InputItem):
    _type: str = ''  # "radio" or "check"
    input_items: List['InputItem'] = []
    value: List[str] = []
    new_line: bool = False


class Sheet(LoadDictMixin, JsonMixin):
    id: str = ''
    _type: str = 'sheet'
    label: str = ''
    input_items: List['InputItem'] = []
    new_line: bool = True
