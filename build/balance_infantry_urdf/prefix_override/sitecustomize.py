import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lin/PRACTICE-Simulator/install/balance_infantry_urdf'
