import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/osama/my_tasks/Test/Osama/1st_task_ws/install/write_my_name'
