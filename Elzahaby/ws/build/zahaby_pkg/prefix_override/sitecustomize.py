import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/zahaby/Test/Elzahaby/ws/install/zahaby_pkg'
