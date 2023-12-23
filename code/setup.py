import os

if os.name == 'nt':
    os.system("C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")
if os.name == 'posix':
    os.system("firefox epicgames.com")