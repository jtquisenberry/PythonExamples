from ctypes import *
print(windll.kernel32)
# <WinDLL 'kernel32', handle ... at ...>
print(cdll.msvcrt)
# <CDLL 'msvcrt', handle ... at ...>
libc = cdll.msvcrt
import numpy as np


def physical_free_windows():
    """Return physical free memory on Windows"""

    from ctypes import c_long, c_ulonglong
    # from ctypes.wintypes import Structure, sizeof, windll, byref

    class MEMORYSTATUSEX(Structure):
        _fields_ = [
            ('dwLength', c_long),
            ('dwMemoryLoad', c_long),
            ('ullTotalPhys', c_ulonglong),
            ('ullAvailPhys', c_ulonglong),
            ('ullTotalPageFile', c_ulonglong),
            ('ullAvailPageFile', c_ulonglong),
            ('ullTotalVirtual', c_ulonglong),
            ('ullAvailVirtual', c_ulonglong),
            ('ullExtendedVirtual', c_ulonglong),
        ]

    def GlobalMemoryStatusEx():
        x = MEMORYSTATUSEX()
        x.dwLength = sizeof(x)
        windll.kernel32.GlobalMemoryStatusEx(byref(x))
        return x

    z = GlobalMemoryStatusEx()
    print(z)
    # return z.ullAvailPhys
    return z

if __name__ == '__main__':
    mem = physical_free_windows()
    print(mem.ullTotalPhys / 1024.0 / 1024.0 / 1024.0)
    print(mem.ullAvailPhys / 1024.0 / 1024.0 / 1024.0)
    print(mem.ullTotalPageFile / 1024.0 / 1024.0 / 1024.0)
    print(mem.ullAvailPageFile / 1024.0 / 1024.0 / 1024.0)
    print(mem.ullTotalVirtual / 1024.0 / 1024.0 / 1024.0)
    print(mem.ullAvailVirtual / 1024.0 / 1024.0 / 1024.0)
    print(mem.ullExtendedVirtual / 1024.0 / 1024.0 / 1024.0)

    size = 1024 * 1024 * 1024 * 14
    print(size * 8 / 1024.0 / 1024 / 1024)
    X = np.random.randn(size)