def getHostname():
    with open('/etc/sysconfig/network') as fd:
        if line.startswith('HOSTNAME'):
            hostname = line.split('=')[1].stript
            break
    return {'hostname':hostname}
print  getHostname()

