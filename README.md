Pysplice
========

[![PyPi version](http://img.shields.io/pypi/v/pysplice.svg)](https://pypi.python.org/pypi/pysplice)
[![Build Status](https://travis-ci.org/berdario/pysplice.png)](https://travis-ci.org/berdario/pysplice)

A simple CFFI wrapper around splice(2)


> splice()  moves  data  between  two  file  descriptors  without copying
> between kernel address space and user address space.  It  transfers  up
> to  len  bytes  of  data  from  the  file  descriptor fd_in to the file
> descriptor fd_out, where one of the descriptors must refer to a pipe.


API
===

The interesting thing is just the splice syscall itself:

- ``pysplice.splice(infile, off_in, outfile, off_out, size, flags=0)``

  One of `infile`,`outfile` has to be a pipe. The offset of a pipe has to be None. (this is currently not checked, but it's an obvious improvement).
  The files have to be objects with a `.fileno()` method.

- ``pysplice.mkpipe()``

  A helper function, that will return a `(reader,writer)` pair of objects with a `.fileno()` method (it just wraps `os.pipe()`)

- ``pysplice.lib.SPLICE_F_MOVE``
- ``pysplice.lib.SPLICE_F_NONBLOCK``
- ``pysplice.lib.SPLICE_F_MORE``
- ``pysplice.lib.SPLICE_F_GIFT``
