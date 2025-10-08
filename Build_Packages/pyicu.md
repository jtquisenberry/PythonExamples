# Build `pyicu` for Python 3.12 on Windows for x64 / AMD64

Python package `pyicu` binds to DLLs in the International Components for Unicode (ICU) application `icu4c`. 


# Prerequisites

## Download Visual Studio

This document assumes the use of Visual Studio 2022. VS 2022 was used to compile the DLLs provided in the release of ICU 77.1 found in icu4c-77_1-Win64-MSVC2022.zip. Errors may be minimized by using the same compiler when building `pyicu`. 

Download Visual Studio from https://visualstudio.microsoft.com/.

## Install Visual Studio

Install Visual Studio. The installer displays several tabs, one of which is "Workloads". The "Desktop development with C++" workload is required to build `pyicu`. The workload includes tools for building native (unmanaged) C++ code. 

Following is a partial list of components installed with the workload on my development machine:

* C++ core desktop features
* MSVC v143 - VS 2022 x64/x86 build tools
* C++ CMake tools for Windows
* Windows 11 SDK (10.0.26100.4654)

## Python 3.12

Install Python 3.12 from https://www.python.org/downloads/ . My development machine runs 3.12.4. I installed Python to `D:\Program Files\Python312`.

```cmd
D:\Development>cd D:\Program Files\Python312

D:\Program Files\Python312>python -V
Python 3.12.4
```

Create a Python virtual environment.

```
D:\Program Files\Python312>python -m venv D:\Development\venvs\v3124b
```

Activate the Python virtual environment.

```
D:\Program Files\Python312>cd D:\Development\venvs\v3124b\Scripts
D:\Development\venvs\v3124b\Scripts>activate
```

## Install Python Packages

Upgrade `pip`

```cmd
(v3124b) D:\Development\venvs\v3124b\Scripts>where pip
D:\Development\venvs\v3124b\Scripts\pip.exe

(v3124b) D:\Development\venvs\v3124b\Scripts>python -m pip install --upgrade pip
Requirement already satisfied: pip in d:\development\venvs\v3124b\lib\site-packages (24.0)
Collecting pip
  Downloading pip-25.2-py3-none-any.whl.metadata (4.7 kB)
Downloading pip-25.2-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 4.3 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
Successfully installed pip-25.2
```

Install the following Python packages:
* `setuptools`
* `wheel`
* `build`

```
(v3124b) D:\Development\venvs\v3124b\Scripts>pip install setuptools

(v3124b) D:\Development\venvs\v3124b\Scripts>pip install wheel

(v3124b) D:\Development\venvs\v3124b\Scripts>pip install build
```

Close the command prompt window.


# Build

## Open Command Prompt

Launch the Visual Studio command prompt. It can be found here: 

```
Start -> Visual Studio 2022 -> x64 Native Tools Command Prompt for VS 2022
```

The shortcut launches a .BAT file that sets environment variables that setup building applications in C++ for the x64 architecture.


## Make the Base Directory

```cmd
C:\Program Files (x86)\Microsoft Visual Studio\Installer>D:
D:\>cd D:\
D:\>mkdir Development
D:\>cd Development
```

## Download Sources

Download the `pyicu` source.

```
D:\Development>curl -L -o pyicu-v2.15.3.zip https://gitlab.pyicu.org/main/pyicu/-/archive/v2.15.3/pyicu-v2.15.3.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  331k    0  331k    0     0   191k      0 --:--:--  0:00:01 --:--:--  192k
```

Download the `icu4c` source.

```
D:\Development>curl -L -o icu4c-77_1-Win64-MSVC2022.zip https://github.com/unicode-org/icu/releases/download/release-77-1/icu4c-77_1-Win64-MSVC2022.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 28.0M  100 28.0M    0     0  20.8M      0  0:00:01  0:00:01 --:--:-- 27.1M
```

## Unzip Sources

Unzip `pyicu`

```
D:\Development>tar -xf pyicu-v2.15.3.zip
```

Unzip `icu4c`

```
D:\Development>icu4c-77_1-Win64-MSVC2022 
D:\Development>tar -xf icu4c-77_1-Win64-MSVC2022.zip -C icu4c-77_1-Win64-MSVC2022
```

## Rename ICU .LIB Files

Rename the *.lib files that are in ICU's lib64 directory. The files are renamed by inserting an underscore before the file extension. 

A later step updates the `setup.py` file to refer to the renamed files. I don't know why the renaming steps are required.

```
D:\Development>ren icu4c-77_1-Win64-MSVC2022\lib64\????????.lib ????????_.lib
```

## Copy ICU DLLs to `pyicu`

Copy ICUs *.dll files to `pyicu`'s `py` directory.

```
D:\Development>copy /Y /B icu4c-77_1-Win64-MSVC2022\bin64\icu*.dll pyicu-v2.15.3\py\icu
icu4c-77_1-Win64-MSVC2022\bin64\icudt77.dll
icu4c-77_1-Win64-MSVC2022\bin64\icuin77.dll
icu4c-77_1-Win64-MSVC2022\bin64\icuio77.dll
icu4c-77_1-Win64-MSVC2022\bin64\icutu77.dll
icu4c-77_1-Win64-MSVC2022\bin64\icuuc77.dll
        5 file(s) copied.
```

List the copied files.

```
D:\Development>dir pyicu-v2.15.3\py /B /S
D:\Development\pyicu-v2.15.3\py\icu
D:\Development\pyicu-v2.15.3\py\icu\icudt77.dll
D:\Development\pyicu-v2.15.3\py\icu\icuin77.dll
D:\Development\pyicu-v2.15.3\py\icu\icuio77.dll
D:\Development\pyicu-v2.15.3\py\icu\icutu77.dll
D:\Development\pyicu-v2.15.3\py\icu\icuuc77.dll
D:\Development\pyicu-v2.15.3\py\icu\__init__.py
```

## Edit `pyicu`'s `setup.py` File

Set the `INCLUDES['win32']` element to the path of the `icu4c` `include` directory.

```python
INCLUDES = {
    'darwin': [],
    'linux': [],
    'freebsd': ['/usr/local/include'],
    'win32': [r'D:\Development\icu4c-77_1-Win64-MSVC2022\include'],
    'sunos5': [],
    'cygwin': [],
}
```

Update the `CFLAGS['win32']` element by adding a switch specifying compilation with C++ 17.

```python
CFLAGS = {
    'darwin': ['-std=c++17'],
    'linux': ['-std=c++17'],
    'freebsd': ['-std=c++17'],
    'win32': ['/Zc:wchar_t', '/EHsc', '/std:c++17'],
    'sunos5': ['-std=c++17'],
    'cygwin': ['-D_GNU_SOURCE=1', '-std=c++17'],
}

```

Set the `LFLAGS['win32']` element to the path of the `icu4c` `lib64` directory.

```python
LFLAGS = {
    'darwin': [],
    'linux': [],
    'freebsd': ['-L/usr/local/lib'],
    'win32': [r'/LIBPATH:D:\Development\icu4c-77_1-Win64-MSVC2022\lib64'],
    'sunos5': [],
    'cygwin': [],
}
```

Update the `LIBRARIES['win32]` element by specifying five of the renamed *.lib files: `['icuin_', 'icuuc_', 'icudt_', 'icuio_', 'icutu_']`. 

An earlier step renamed the *.lib files. I don't know why the renaming steps are required.


```python
LIBRARIES = {
    'darwin': [],
    'linux': [],
    'freebsd': ['icui18n', 'icuuc', 'icudata'],
    'win32': ['icuin_', 'icuuc_', 'icudt_', 'icuio_', 'icutu_'],
    'sunos5': ['icui18n', 'icuuc', 'icudata'],
    'cygwin': ['icui18n', 'icuuc', 'icudata'],
}
```

Update the call to `setup()` by adding the `package_data` argument.

```
      package_dir={"": "py"},
      packages=['icu'],
      tests_require=['pytest', 'six'],
      package_data={"icu": ["*.dll",]},)
```

## Activate the Python Virtual Environment

Activate the Python virtual environment. This step will ensure that the packages installed to build the .*whl file will be used.

```
D:\Development>cd D:\Development\venvs\v3124\Scripts

D:\Development\venvs\v3124b\Scripts>activate
```

## Change Directory to the `pyicu` Directory

Change the directory to the `pyicu` directory.

```
(v3124b) D:\Development\venvs\v3124\Scripts>cd D:\Development\pyicu-v2.15.3
```

## Set the ICU_VERSION Environment Variable

Set the ICU_VERSION environment to the major version of ICU. If ICU version 77.1 is used, then set the variable to `77`.

```
(v3124b) D:\Development\pyicu-v2.15.3>set ICU_VERSION=77
```

## Build `pyicu` to .EXP and .LIB

Build `pyicu` with Python. The resulting files are *.exp and *.lib files.

```
(v3124b) D:\Development\pyicu-v2.15.3>python setup.py build

Building pyicu 2.15.3 for ICU 77 (max ICU major version supported: 77)

D:\Development\venvs\v3124b\Lib\site-packages\setuptools\_distutils\dist.py:289: UserWarning: Unknown distribution option: 'test_suite'
  warnings.warn(msg)
...
running build
running build_py
creating build\lib.win-amd64-cpython-312\icu
copying py\icu\__init__.py -> build\lib.win-amd64-cpython-312\icu
copying py\icu\icudt77.dll -> build\lib.win-amd64-cpython-312\icu
copying py\icu\icuin77.dll -> build\lib.win-amd64-cpython-312\icu
copying py\icu\icuio77.dll -> build\lib.win-amd64-cpython-312\icu
copying py\icu\icutu77.dll -> build\lib.win-amd64-cpython-312\icu
copying py\icu\icuuc77.dll -> build\lib.win-amd64-cpython-312\icu
running build_ext
building 'icu._icu_' extension
creating build\temp.win-amd64-cpython-312\Release
...
   Creating library build\temp.win-amd64-cpython-312\Release\_icu_.cp312-win_amd64.lib and object build\temp.win-amd64-cpython-312\Release\_icu_.cp312-win_amd64.exp
Generating code
Finished generating code
```

## Build `pyicu` to .WHL

Build the `pyicu` wheel file with Python. 

```
(v3124b) D:\Development\pyicu-v2.15.3>python setup.py bdist_wheel

Building pyicu 2.15.3 for ICU 77 (max ICU major version supported: 77)
..
creating build\bdist.win-amd64\wheel\pyicu-2.15.3.dist-info\WHEEL
creating 'dist\pyicu-2.15.3-cp312-cp312-win_amd64.whl' and adding 'build\bdist.win-amd64\wheel' to it
adding 'icu/__init__.py'
adding 'icu/_icu_.cp312-win_amd64.pyd'
adding 'icu/icudt77.dll'
adding 'icu/icuin77.dll'
adding 'icu/icuio77.dll'
adding 'icu/icutu77.dll'
adding 'icu/icuuc77.dll'
adding 'pyicu-2.15.3.dist-info/licenses/LICENSE'
adding 'pyicu-2.15.3.dist-info/METADATA'
adding 'pyicu-2.15.3.dist-info/WHEEL'
adding 'pyicu-2.15.3.dist-info/top_level.txt'
adding 'pyicu-2.15.3.dist-info/RECORD'
removing build\bdist.win-amd64\wheel
```

## Show the Wheel File

Show the *.whl file.

```
(v3124b) D:\Development\pyicu-v2.15.3>cd D:\Development\pyicu-v2.15.3\dist

(v3124b) D:\Development\pyicu-v2.15.3\dist>dir /s /b
D:\Development\pyicu-v2.15.3\dist\pyicu-2.15.3-cp312-cp312-win_amd64.whl
```

## Install the Wheel File

Test the wheel file by installing it.

```
(v3124b) D:\Development\pyicu-v2.15.3\dist>pip install pyicu-2.15.3-cp312-cp312-win_amd64.whl
Processing d:\development\pyicu-v2.15.3\dist\pyicu-2.15.3-cp312-cp312-win_amd64.whl
Installing collected packages: pyicu
Successfully installed pyicu-2.15.3
```


