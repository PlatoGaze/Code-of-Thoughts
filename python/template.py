import json
class Template:
    def __init__(self, template_dict: dict) -> None:
        if (self.is_valid(template_dict)):
            self.template = template_dict
        else:
            raise ValueError("Invalid template format")

    def is_valid(self, template_dict: dict):
        return True

    def to_dict(self):
        return self.template.copy()

    def display(self):
        print(json.dumps(self.to_dict(), indent=4))

    def get_template_by_id(self, id: str) -> 'Template':
        references = id.split('.')
        template = self.template.copy()
        path_so_far = []

        try:
            for ix, ref in enumerate(references):
                if ref.isdigit():
                    ref_index = int(ref) - 1
                    path_so_far.append(ref)
                    template = template["functions"][ref_index]["code"]

                    if not template or "functions" not in template:
                        raise TypeError(
                            f"{'.'.join(path_so_far)} is not a template")

        except (KeyError, IndexError, TypeError):
            return None

        return Template(template)

    def add_template(self, new_template, id: str):
        
