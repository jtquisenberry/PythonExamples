# PyICU

## Get the version of `icu.dll`. 

Get the version of `icu.dll`. Only the major and minor version is necessary. In this example, the version is 72.1.


``` powershell
> (Get-Item "C:\Windows\System32\icu.dll").VersionInfo

ProductVersion   FileVersion      FileName
--------------   -----------      --------
72, 1, 0, 4      72, 1, 0, 4 (... C:\Windows\System32\icu.dll
```

# Extract the ICU Source

Extract the ICU source code with 7-zip or the comand line.

``` powershell
> D:
> cd D:\Development
> Expand-Archive -Path "icu4c-72_1-Win32-MSVC2019.zip" -DestinationPath "icu4c"
> cd icu4c\20221013.8_ICU4C_MSVC_x86_Release
> Expand-Archive -Path ".\icu-windows.zip" -DestinationPath ../../icu-windows
```


## Open Command Prompt

Open x64 Native Tools Command Prompt for VS 2022. 

### UI

Start -> Visual Studio 2022 -> x64 Native Tools Command Prompt for VS 2022.

### Command Line

```
"D:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
**********************************************************************
** Visual Studio 2022 Developer Command Prompt v17.11.2
** Copyright (c) 2022 Microsoft Corporation
**********************************************************************
[vcvarsall.bat] Environment initialized for: 'x64'
```


## Set the ICU Environment Variable

```
> set ICU_VERSION=72.1
```






```
> cd icu4c\20221013.8_ICU4C_MSVC_x86_Release

```



```
> set INCLUDE=%INCLUDE%;D:\Development\icu4c-72_1-Win32-MSVC2019\20221013.8_ICU4C_MSVC_x86_Release\icu-windows\include
```








