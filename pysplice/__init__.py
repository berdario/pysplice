from pysplice._splice import ffi, lib
import os
import errno

from collections import namedtuple
Pipe = namedtuple('Pipe', 'fileno')

def mkpipe():
    readfd, writefd = os.pipe()
    return Pipe(lambda: readfd), Pipe(lambda: writefd)

def splice(infile, off_in, outfile, off_out, size, flags=0):
    off_in = ffi.NULL if off_in is None else ffi.new('loff_t *', off_in)
    off_out = ffi.NULL if off_out is None else ffi.new('loff_t *', off_out)
    while True:
        res = lib.splice(infile.fileno(), off_in,
                         outfile.fileno(), off_out,
                         size, flags)
        if res != -1:
            return res
        elif ffi.errno != errno.EINTR:
            raise OSError(ffi.errno, os.strerror(ffi.errno))


def testit():
    #argv = ['cat', 'a']
    #proc = subprocess.Popen(argv, close_fds=True, stdout=subprocess.PIPE)
    #pipe_fd = proc.stdout
    r, w = mkpipe()
    from urllib.request import urlopen
    u = urlopen('http://arstechnica.com')
    # import socket
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect(('arstechnica.co.uk', 80))
    # sock.sendall(b'GET / HTTP/1.1\r\nHost: arstechnica.co.uk\r\n\r\n')


    with open('/home/dario/.pythonz/dists/jython-installer-2.7.0.jar', 'rb') as f1, open('ars', 'wb') as f2:
        #l = f1.seek(0, 2)
        #f1.seek(0)
        splice(u, None, w, None, 93296)
        splice(u, None, w, None, 93296)
        splice(r, None, f2, 0, 93296)

if __name__ == '__main__':
    testit()
