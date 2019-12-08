#!/usr/bin/env python
from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)
from IPython.core.displaypub import publish_display_data

import sys

@magics_class
class Xdiag(Magics):

    def __init__(self, *args, **kwargs):
        super(Xdiag, self).__init__(*args, **kwargs)
        self.output_format = 'svg'
        self.mime_type = {
            'png': 'image/png',
            'svg': 'image/svg+xml',
        }
        self.delete_tempfiles = True
        if sys.platform in ('win32',):
            # Win32 raises Permission-Error
            self.delete_tempfiles = False

    def diag(self, line, cell, command):
        import tempfile

        with tempfile.NamedTemporaryFile(suffix=".diag", delete=self.delete_tempfiles) as f:
            cell += u"\n"
            f.write(cell.encode('utf-8'))
            f.flush()
            with tempfile.NamedTemporaryFile(suffix="."+self.output_format, delete=self.delete_tempfiles) as p:
                args = [
                    '-T', self.output_format,
                    '-o', p.name,
                    f.name
                ]
                command.main(args=args)
                p.seek(0)
                data = p.read()
                if self.output_format in ['svg']:
                    data = data.decode('utf-8')
                publish_display_data({
                    self.mime_type.get(self.output_format, 'text/plain'): data
                })

        return

    @line_magic
    def xdiag_output_format(self,line):
        if line not in self.mime_type.keys():
            hint = "(available: {})".format(", ".join(self.mime_type.keys()))
            raise Exception("unsupported format " + hint)
        self.output_format = line

    @line_magic
    def xdiag_delete_tempfiles(self,line):
        self.delete_tempfiles = (line.strip().upper() in ('YES', 'TRUE', '1'))
    
    @cell_magic
    def blockdiag(self, line, cell):
        import blockdiag.command
        return self.diag(line, cell, blockdiag.command)

    @cell_magic
    def seqdiag(self, line, cell):
        import seqdiag.command
        return self.diag(line, cell, seqdiag.command)

    @cell_magic
    def actdiag(self, line, cell):
        import actdiag.command
        return self.diag(line, cell, actdiag.command)

    @cell_magic
    def nwdiag(self, line, cell):
        import nwdiag.command
        return self.diag(line, cell, nwdiag.command)

    @cell_magic
    def packetdiag(self, line, cell):
        import packetdiag.command
        return self.diag(line, cell, packetdiag.command)

    @cell_magic
    def rackdiag(self, line, cell):
        import rackdiag.command
        return self.diag(line, cell, rackdiag.command)

def load_ipython_extension(ipython):
    ipython.register_magics(Xdiag)
