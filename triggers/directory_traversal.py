def trigger_path_traversal(file_name):
    with open(f"/var/www/{file_name}", "r") as file:
        return file.read()
