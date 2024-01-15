import json


class Template:
    def __init__(self, template_dict: dict) -> None:
        """
        Initializes an instance of MyClass with a template dictionary.

        Args:
            template_dict (dict): A dictionary representing the template.

        Raises:
            ValueError: If the template format is invalid.
        """
        if self.is_valid(template_dict):
            self.template = template_dict
        else:
            raise ValueError("Invalid template format")

    def is_valid(self, template_dict: dict):
        return True

    def to_dict(self):
        """
        Converts the template object to a dictionary.

        Returns:
            dict: A dictionary representation of the template object.
        """
        return self.template.copy()

    def display(self):
        print(json.dumps(self.to_dict(), indent=4))

    def get_template_by_id(self, id: str) -> 'Template':
        """
        Retrieves a template by its ID.

        Args:
            id (str): The ID of the template.

        Returns:
            Template: The template object corresponding to the given ID, or None if not found.
        """
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

    def add_template(self, new_template, id: str = ""):
        """
        Adds a new template to the existing template.

        Parameters:
        - new_template: The new template to be added.
        - id: The optional ID specifying the location where the new template should be added. If not provided, the new template will be added at the end.

        Returns:
        None
        """
        references = id.split('.')
        template = self.template.copy()
        if id != "":
            for refer in references:
                template = template["functions"][refer - 1]["code"]
        if isinstance(new_template, Template):
            new_template = new_template.to_dict()
        new_id = len(template["functions"]) + 1
        template["functions"].append({
            "id": new_id,
            "type": "code",
            "code": new_template
        })
