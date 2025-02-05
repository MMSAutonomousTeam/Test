import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ahmedmwafy/Test/Mwafy/ros2_my_ws/install/turtle_control_1'
