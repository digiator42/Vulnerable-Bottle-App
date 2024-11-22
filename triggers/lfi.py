
# Local File Inclusion (LFI)
def trigger_lfi(file_name):
    exec(open(file_name).read())
