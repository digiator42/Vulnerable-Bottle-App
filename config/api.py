from bottle import request, template
from utils.main import JsonResponse, get_code_level_function
import inspect

def logs():
    try:
        session = request.environ.get('beaker.session')
        vuln: str = request.query.get('vuln')
        vuln = vuln.replace(f'?level={session['level']}', '')
        
        with open(f'./logs/{vuln}.log', 'r') as f:
            logs = f.read()
            return template('_logs', output=logs, vuln=vuln)
    except Exception as _:
        return template('_logs', output=f'No logs for {vuln} yet', vuln=vuln)

def security_level():
    session = request.environ.get('beaker.session')
    level =  session.get('level')
    return JsonResponse({'level': f'?level={level}'}, 200).render()

def level_code():
    try:
        session = request.environ.get('beaker.session')
        security_level = session['level']
        vuln = request.query.get('vuln')
        
        module = __import__(f'triggers.{vuln}', fromlist='triggers')
        
        func_dict = get_code_level_function(module, security_level)
        
        func = func_dict[f'{security_level}_{vuln}'] #e.g. medium_xss
        func_source = inspect.getsource(func)
        print(func_source)
        
        return template('_code', output=func_source, vuln=vuln)
    except Exception as e:
        print(e)
        return template('_code', output=f'No source code for {vuln} yet', vuln=vuln)