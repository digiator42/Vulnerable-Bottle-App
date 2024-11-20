


def get_template(template_name, **kwargs):
    """
    Reads a template file and formats it with the provided keyword arguments.
    Args:
        template_name (str): The name of the template file to read.
        **kwargs: Arbitrary keyword arguments to format the template.
    Returns:
        str: The formatted template string.
    Raises:
        FileNotFoundError: If the template file does not exist.
        KeyError: If a placeholder in the template is not provided in kwargs.
    """
    
    with open(f"templates/{template_name}") as f:
        template = f.read()
    return template.format(**kwargs)