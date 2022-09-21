import psutil
import os


class debug_data:

    def get_cpu_usage():
        return psutil.cpu_percent()

    def get_res_set_size():
        process = psutil.Process(os.getpid())
        return process.memory_info().rss
