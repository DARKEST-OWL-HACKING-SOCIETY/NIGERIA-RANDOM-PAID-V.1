import os, sys

try:os.system('xdg-open https://chat.whatsapp.com/LQGUIDUWK5gFVjJjreQ0vp')

except:pass

try:

    __import__("windows_enc").Main()

except Exception as e:

    exit(str(e))
