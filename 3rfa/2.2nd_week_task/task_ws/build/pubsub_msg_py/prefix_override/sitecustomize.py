import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/arafa/Desktop/Autonomous/MMS/Test/3rfa/2.2nd_week_task/task_ws/install/pubsub_msg_py'
