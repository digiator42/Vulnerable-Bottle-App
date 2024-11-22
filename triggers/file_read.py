from bottle import request, response

def trigger_read_file():
    filename = request.query.filename
    try:
        with open(filename, 'r') as file:
            content = file.read()
        response.content_type = 'text/plain'
        return content
    except Exception as e:
        response.status = 500
        return str(e)