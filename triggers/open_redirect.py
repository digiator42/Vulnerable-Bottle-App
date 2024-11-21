from bottle import redirect

def trigger_open_redirect(redirect_url):
    return redirect(redirect_url)
