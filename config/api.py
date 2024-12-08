from bottle import request, template
from utils.main import JsonResponse, get_code_level_function
import inspect
from config.settings import DEFAULT_LEVEL
from importlib import import_module
import re


def logs():
    """"
    Get logs for a specific vulnerability.
    """
    try:
        session = request.environ.get('beaker.session')
        vuln: str = request.query.get('vuln')
        vuln = vuln.replace(f'?level={session["level"]}', '')
        vuln = vuln.replace('-', '_')
        
        if not vuln:
            return template('_logs', output='🙂', vuln=vuln)
        
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

    source_vuln = vuln.replace(f'?level={security_level}', '')
    
    # for instanc cmd/cmd or only cmd
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
        
    try:
        # return all trigger functions relying on security level
        func_dict = get_code_level_function(module, security_level)
        
        # need for root route if it has hython
        vuln_func = vuln_func.replace('-', '_')
        
        if security_level == DEFAULT_LEVEL:
            pattern = f'trigger_{vuln_func}'
            trigger_pattern = re.compile(rf"{pattern}")

            # gets one function starts with trigger_
            func = [value for key, value in func_dict.items() if trigger_pattern.match(key)][0]
        else:
            func = func_dict[f'{security_level}_{vuln_func}'] #e.g. medium_xss
        
        func_source = inspect.getsource(func)
        
        return template('_code', output=func_source, vuln=vuln_func)
    
    except Exception as e:
        print(f'Unexpected error {e}')
        output = f'No source code for {vuln_func} at level {security_level} yet'
        return template('_code', output=output, vuln=vuln_func)