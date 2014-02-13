#!/usr/bin/env python

import tables
import numpy as np

h5 = tables.openFile('/tmp/test.h5', 'w')
table = h5.createTable(h5.root, 'table',description=np.dtype([('col', 'S16'),('intcol','I')]))
vals = [('abc',3), ('def',4), ('xyz',1), ('x11',2), ('za',8), ('testab', 9), ('testa', 11)]
table.append(vals)
table.flush()

table = h5.root.table

print [x.fetch_all_fields() for x in table.where('contains(col, "ab") & (intcol<10)')]

