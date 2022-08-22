# --- The visitor base class

class NodeVisitor:
    def visit(self, node, indent_tabs=0):
        method_name = 'visit_' + type(node).__name__
        method = getattr(self, method_name, None)
        if method is None:
            method = self.generic_visit
        return method(node, indent_tabs)

    def generic_visit(self, node, indent_tabs=0):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class TextOutput(NodeVisitor):
    option_header = {'check': "【 】", 'radio': "（ ）"}

    def visit_InputText(self, node, indent_tabs=0):
        new_line = "\n" if (indent_tabs == 0) else ""
        label = f"{node.label}：" if node.label else ""
        return f"{new_line}{label} _______"

    def visit_InputDate(self, node, indent_tabs=0):
        new_line = "\n" if (indent_tabs == 0) else ""
        label = f"{node.label}：" if node.label else ""
        return f"{new_line}{label}___年___月___日"

    def visit_Option(self, node, indent_tabs=0):
        option_label, add_tab = self.option_label(node, indent_tabs)
        return option_label

    def visit_OptionInput(self, node, indent_tabs=0):
        option_label, add_tab = self.option_label(node, indent_tabs)
        result = option_label
        for child in node.input_items:
            result += f"{self.visit(child, indent_tabs + add_tab)}"
        return result

    def visit_CheckGroup(self, node, indent_tabs=0):
        check_group_label, add_tab = self.check_group_label(node, indent_tabs)
        result = check_group_label
        for child in node.input_items:
            result += f"{self.visit(child, indent_tabs + add_tab)}"
        return result

    def visit_Sheet(self, node, indent_tabs=0):
        result = f"{node.label}"
        for child in node.input_items:
            result += f"{self.visit(child, indent_tabs)}"
        return result

    @staticmethod
    def option_label(node, indent_tabs):
        line_header, add_tab = TextOutput.my_line_header(node.parent.new_line, indent_tabs)
        header = TextOutput.option_header.get(node.parent._type, "??")
        return f"{line_header}{header}{node.label}", add_tab

    @staticmethod
    def check_group_label(node, indent_tabs):
        check_type = "多選" if node._type == "check" else "單選"
        line_header, add_tab = TextOutput.my_line_header(node.parent.new_line, indent_tabs)
        if node.label:
            result = f"{line_header}{node.label}[{check_type}]："
        else:
            result = f"{line_header}[{check_type}]："
        return result, add_tab

    @staticmethod
    def my_line_header(new_line: bool, indent_tabs=0):
        return ("\n" + "\t" * indent_tabs, 1 + indent_tabs) if (new_line or indent_tabs == 0) else ("", indent_tabs)
