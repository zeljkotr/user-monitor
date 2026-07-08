import os
import sys
import tempfile

# Postavi temp folder na mesto gde ima dozvolu
if getattr(sys, 'frozen', False):
    temp = os.path.join(os.environ.get('LOCALAPPDATA', tempfile.gettempdir()), 'UserMonitor')
    os.makedirs(temp, exist_ok=True)
    tempfile.tempdir = temp