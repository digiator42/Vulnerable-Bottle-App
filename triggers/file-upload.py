import os

def trigger_file_upload(user_input):
    file_name = user_input['input'].filename
    content = user_input['input'].file.read()

    os.makedirs("/media", exist_ok=True)
    with open(f"./media/{file_name}", "wb") as f:
        f.write(content)
    return f"Image saved at /media/{file_name}"