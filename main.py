import time
import ctypes
ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
time.sleep(5)
ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
