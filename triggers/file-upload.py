import os
from bottle import FileUpload
from typing import Dict
from bottle import request
from config.settings import DEFAULT_LEVEL, MEDIUM_LEVEL, STRONG_LEVEL
from PIL import Image

def trigger_file_upload(user_input: Dict[str, FileUpload]):
    
    session = request.environ.get('beaker.session')
    security_level = session.get('level')
    
    if security_level == DEFAULT_LEVEL:
        return weak_file_upload(user_input)
    
    elif security_level == MEDIUM_LEVEL:
        return medium_file_upload(user_input)
    
    elif security_level == STRONG_LEVEL:
        return strong_file_upload(user_input)

def weak_file_upload(user_input: Dict[str, FileUpload]):
    """
    Weak level of file upload
    """
    return _exec_file_upload(user_input)

def medium_file_upload(user_input: Dict[str, FileUpload]):
    """
    Medium level of file upload
    """
    file = user_input['input']
    file_name = file.filename
    
    # Check the content_type
    if not file.content_type.startswith('image/'):
        return 'File is not an image'

    # allowed image extensions
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    if not any(file_name.lower().endswith(ext) for ext in allowed_extensions):
        return 'File extension is not allowed'
    
    return _exec_file_upload(user_input)

def strong_file_upload(user_input: Dict[str, FileUpload]):
    """
    Strong level of file upload
    """
    file = user_input['input']
    file_name = file.filename
    
    # allowed image extensions
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    if not any(file_name.lower().endswith(ext) for ext in allowed_extensions):
        return 'File extension is not allowed'

    # allowed image size
    if file.content_length > 1024 * 1024:
        return 'File size is too large'
    
    # Verifies that it is, in fact, an image...
    try:
        image = Image.open(file.file)
        image.verify()
    except (IOError, SyntaxError) as e:
        print(e)
        return 'File is not a valid image'

    return _exec_file_upload(user_input)

def _exec_file_upload(user_input: Dict[str, FileUpload]):
    """
    Default level of file upload
    """
    file = user_input['input']
    file_name = file.filename
    
    os.makedirs("./media", exist_ok=True)
    file.save(f"./media/", overwrite=True)
    
    return f'Image saved at /media/{file_name}'