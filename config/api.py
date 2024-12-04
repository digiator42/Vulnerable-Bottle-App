from bottle import request, template
from utils.main import JsonResponse, get_code_level_function
import inspect
from config.settings import DEFAULT_LEVEL
from importlib import import_module


def logs():
    """"
    Get logs for a specific vulnerability.
    """
    try:
        session = request.environ.get('beaker.session')
        vuln: str = request.query.get('vuln')
        vuln = vuln.replace(f'?level={session['level']}', '')
        
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
    # source of vulnerability without level query
    # e.g. subprocess_cmd?level=weak -> subprocess_cmd
    source_vuln = vuln.replace(f'?level={security_level}', '')
    
    # pointing to source_vuln before removing *_ if needed
    vuln = source_vuln
    
    if source_vuln.find('_') != -1:
        vuln = source_vuln.split('_')[-1] #subprocess_cmd -> cmd
    
    
    try:
        # fetch pure trigger moudle cmd, xss etc...
        module = import_module(f'triggers.{vuln}')
        
    except ImportError as e:
        print(f'Module import error: {e}')
        return template('_code', output=f'No module for {vuln}', vuln=vuln)
        
    try:
        # return all trigger functions relying on security level
        func_dict = get_code_level_function(module, security_level)

        if security_level == DEFAULT_LEVEL:
            func = func_dict[f'trigger_{source_vuln}'] #e.g. trigger_xss
        else:
            func = func_dict[f'{security_level}_{source_vuln}'] #e.g. medium_xss
        
        func_source = inspect.getsource(func)
        
        return template('_code', output=func_source, vuln=vuln)
    
    except Exception as e:
        print(f'Unexpected error {e}')
        return template('_code', output=f'No source code for {vuln} yet', vuln=vuln)