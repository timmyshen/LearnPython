from apihelper import info
import odbchelper

# li = []

# info(li)

info(odbchelper)
info(odbchelper, 30)
info(odbchelper, 30, 0)

print type(1)
print type([])
print type(odbchelper)

import types
print type(odbchelper) == types.ModuleType

print type(type(1))
print type(type(type(1)))

print str(odbchelper)

print dir()