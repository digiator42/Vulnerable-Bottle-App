import os
from bottle import FileUpload
from typing import Dict

def trigger_file_upload(user_input: Dict[str, FileUpload]):
    
    file = user_input['input']
    file_name = file.filename

    os.makedirs("./media", exist_ok=True)
    file.save(f"./media/", overwrite=True)
    
    return f'Image saved at /media/{file_name}'