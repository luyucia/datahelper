#!/usr/bin/python
#encoding:utf-8
# author:luyu
import subprocess
import csv

class Presto(object):
    """docstring for Presto"""
    def __init__(self, host ,port ,catalog='hive',schema='default'):
        super(Presto, self).__init__()
        self.host    = host 
        self.schema  = schema 
        self.port    = port
        self.catalog = catalog

    def query(self,sql):
        cmd = 'presto --server {host}:{port} --catalog {catalog} --schema {schema} --execute "{sql}"'.format(
            host=self.host,
            port=self.port,
            catalog=self.catalog,
            schema=self.schema,
            sql=sql,
            )
         
        reader = csv.reader(self._execmd(cmd))
        lines = []
        for l in reader:
            lines.append(l)
        return lines

    def _execmd(self,cmd):
        p = subprocess.Popen(
        cmd, 
        bufsize            = 1024000, 
        executable         = None,
        stdin              = subprocess.PIPE, 
        stdout             = subprocess.PIPE, 
        stderr             = subprocess.PIPE, 
        preexec_fn         = None, 
        close_fds          = False, 
        shell              = True, 
        cwd                = None, 
        env                = None, 
        universal_newlines = False, 
        startupinfo        = None, 
        creationflags      = 0
        )

        print p.stderr.read()
        return p.stdout
