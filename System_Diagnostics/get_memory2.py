from ctypes import *
print(windll.kernel32)
# <WinDLL 'kernel32', handle ... at ...>
print(cdll.msvcrt)
# <CDLL 'msvcrt', handle ... at ...>
libc = cdll.msvcrt


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
    return z.ullAvailPhys

if __name__ == '__main__':
    physical_free_windows()