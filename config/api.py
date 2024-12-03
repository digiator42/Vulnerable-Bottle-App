from bottle import request, template
from utils.main import JsonResponse

def logs():
    try:
        vuln = request.query.get('vuln')
        with open(f'./logs/{vuln}.log', 'r') as f:
            logs = f.read()
            return template('_logs', output=logs, vuln=vuln)
    except Exception as _:
        return template('_logs', output=f'No logs for {vuln} yet', vuln=vuln)
    
def security_level():
    session = request.environ.get('beaker.session')
    level =  session.get('level')
    return JsonResponse({'level': f'?level={level}'}, 200).render()