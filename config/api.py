from bottle import request, template
from utils.main import JsonResponse, get_code_level_function, get_template
from config.settings import STRONG_LEVEL
from importlib import import_module
import inspect
import re
import hashlib
import secrets
import os
import markdown


def logs():
    """"
    Get logs for a specific vulnerability.
    """
    try:
        vuln: str = request.query.get('vuln')
        vuln = re.sub(r'\?.*', '', vuln)
        vuln = vuln.replace('-', '_')
        
        if not vuln:
            return template('_logs', output='🙂', vuln=vuln)
        
        os.makedirs('./logs', exist_ok=True)
        with open(f'./logs/{vuln}.log', 'r') as f:
            logs = f.read()
            return template('_logs', output=logs, vuln=vuln)
    except Exception as e:
        print(e)
        return template('_logs', output=f'No logs for {vuln} yet', vuln=vuln)

def security_level():
    session = request.environ.get('beaker.session')
    level =  session.get('level')
    return JsonResponse({'level': f'?level={level}'}, 200).render()

def level_code():
    """
    End point for code view: fetch module and get required trigger code function
    Returns:
        template: view with source code.
    """
    session = request.environ.get('beaker.session')
    vuln: str = request.query.get('vuln')
    security_level = session['level']
    
    # clear any query
    source_vuln = re.sub(r'\?.*', '', vuln)
    
    # Module and function names might differ, below matches both cases
    vuln_module = source_vuln
    vuln_func = source_vuln
    if source_vuln.find('/') != -1:
        vuln_module, vuln_func = source_vuln.split('/')
    
    try:
        # fetch pure trigger moudle cmd, xss etc...
        module = import_module(f'triggers.{vuln_module}')
        
    except ImportError as e:
        print(f'Module import error: {e}')
        return template('_code', output='🙂', vuln=vuln_module)
        
    # return all trigger functions relying on security level
    func_dict = get_code_level_function(module, security_level)
    source_func = list(func_dict.values()) #e.g. medium_xss, _exec_xss
    
    if source_func:
        func_code = ''
        for function in source_func[::-1]:
            func_code += '\n\n' + inspect.getsource(function)
            
        return template('_code', output=func_code.lstrip(), vuln=vuln_func)
    
    output = f'No source code for {vuln_func} at level {security_level} yet'
    return template('_code', output=output, vuln=vuln_func)
    
    
def generate_csrf_token():
    session = request.environ.get('beaker.session')
    
    csrf_token = hashlib.md5(session['username'].encode()).hexdigest()
    
    if session['level'] == STRONG_LEVEL:
        csrf_token = secrets.token_urlsafe(32)
        session['csrf_token'] = csrf_token
    
    return JsonResponse({'csrf_token': csrf_token}).render()

def get_jwt_token():
    jwt_token = request.environ['beaker.session']['jwt_token']
    
    return JsonResponse({'token': jwt_token}).render()

def help():
    vuln: str = request.query.get('vuln')
    vuln = re.sub(r'\?.*', '', vuln)    
    vuln = vuln.replace('_', '-')
    
    try:
        with open(f'./help/{vuln}.md', 'r') as f:
            html_content = markdown.markdown(f.read())
    except FileNotFoundError as e:
        return str(e)
    
    temp = get_template('_help', instructions=html_content)
    return template(temp)