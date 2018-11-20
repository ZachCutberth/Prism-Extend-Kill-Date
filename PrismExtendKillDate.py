#!python3
# Prism Extend Kill Date
# Written by Zach Cutberth

import sys
import shutil
import subprocess
import os
#import win32serviceutil

def resource_path():
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return base_path

subprocess.run(["net", "stop", "PrismLicSvr"])

path = 'C:\ProgramData\RetailPro\Server\Licensing\\'
subprocess.run([path + 'LicenseServer.exe', '/uninstall'])

try:
    os.rename(path + 'LicenseServer.exe', path + 'LicenseServer.exe.orig')
except FileExistsError:
    pass

path = resource_path()
shutil.copyfile(path + '\LicenseServer.exe', 'C:\ProgramData\RetailPro\Server\Licensing\LicenseServer.exe')

path = 'C:\ProgramData\RetailPro\Server\Licensing\\'
subprocess.run([path + 'LicenseServer.exe', '/install'])

subprocess.run(["net", "start", "PrismLicSvr"])

print('\nThe Prism license server kill date has been extended successfully.')

input('\nPress any key to exit.')

