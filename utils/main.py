


def get_template(template_name, **kwargs):
    with open(f"templates/{template_name}") as f:
        template = f.read()
    return template.format(**kwargs)