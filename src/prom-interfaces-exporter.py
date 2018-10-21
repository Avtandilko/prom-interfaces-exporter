import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep
# Update to trigger build

class CustomHttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        write_interface_status()
        file = open(curdir + sep + self.path, 'rb')
        print(file.name)
        if file.name == './/metrics':
            self.send_response(200)
            self.send_header('content-type', 'text')
            self.end_headers()
            self.wfile.write(file.read())
        else:
            self.send_response(503)
        file.close()


def get_interface_names():
    interfaces = {}
    # Check if exporter runs in docker container and /sys from host mounted to /host/sys
    try:
        stdout = subprocess.check_output('ls {}'.format(CONTAINER_DIR), shell=True).decode()
    except subprocess.CalledProcessError:
        try:
            stdout = subprocess.check_output('ls {}'.format(HOST_DIR), shell=True).decode()
        except:
            stdout = 'Something goes wrong'
    for interface in stdout.split('\n'):
        if interface is not '':
            interfaces.update({interface: ''})
    return interfaces


def check_interface_status(sys_location):
    interfaces = get_interface_names()
    for interface in interfaces:
        if subprocess.check_output('cat {}{}/operstate'.format(sys_location, interface),
                                   shell=True).decode().strip() == 'down':
            interfaces[interface] = 0
        elif subprocess.check_output('cat {}{}/operstate'.format(sys_location, interface),
                                     shell=True).decode().strip() == 'up':
            interfaces[interface] = 1
        else:
            interfaces[interface] = 2
    return interfaces


def write_interface_status():
    try:
        interfaces = check_interface_status(CONTAINER_DIR)
    except subprocess.CalledProcessError:
        interfaces = check_interface_status(HOST_DIR)
    with open('metrics', 'w') as metrics:
        metrics.write('# HELP interface_status down = 0, up = 1, any other states (unknown) = 2\n')
        metrics.write('# TYPE interface_status untyped\n')
        for interface in interfaces:
            metrics.write('interface_status{{interface="{}"}} {}\n'.format(interface, interfaces.get(interface)))
    metrics.close()


def run_exporter(server_class=HTTPServer, handler_class=CustomHttpProcessor):
    server_address = ('', 9425)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    CONTAINER_DIR = '/host/sys/class/net/'
    HOST_DIR = '/sys/class/net/'
    run_exporter()
