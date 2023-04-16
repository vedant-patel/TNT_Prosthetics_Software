from ctypes import *
so_file = "C:\Users\cassi\My Stuff\School\1. Triton Neurotech\Neural Prosthetics\tntprostheticsoftware\Python-C-Combo-Test\function-def.so"
function_def = CDLL(so_file)
 
print(type(function_def))
<class 'ctypes.CDLL'>
 
print(function_def.square(10))
100
print(function_def.square(8))
64