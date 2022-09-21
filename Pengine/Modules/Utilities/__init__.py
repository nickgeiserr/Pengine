from time import sleep


class Utils:
    # this function suspends the current thread. don't use on main thread unless testing
    def suspend_current_thread(s_time):
        sleep(s_time)
