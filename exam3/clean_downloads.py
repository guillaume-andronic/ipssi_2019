import os, time, sys
winuser = os.popen('/mnt/c/Windows/System32/cmd.exe /c "echo %USERNAME%"').read()
#print(winuser)
path_to_watch = "/mnt/c/Users/" + winuser[:-1] + "/Downloads/"
