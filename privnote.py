import sys
import json
import os.path
import subprocess
import pyperclip
import pyPrivnote as pn

from os import path

dir_name = os.getcwd()

def exists(file):
  full_path = os.path.join(dir_name, file)
  return path.exists(file) or path.exists(full_path)

def upload(file):
  proc = subprocess.Popen('curl -q -s -F "file=@' + file + '" https://api.anonfiles.com/upload', stdout=subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  obj = json.loads(out)
  url = obj['data']['file']['url']['short']
  return url

def create_note(note):
  note_link = pn.create_note(note)
  pyperclip.copy(note_link)
  spam = pyperclip.paste()
  print(note_link)
  
if len(sys.argv) < 2:
  print('YOU MUST SUPPLY A NOTE')
else:
  if '-u' in sys.argv or '--upload' in sys.argv:
    if '-u' in sys.argv:
      file_path = sys.argv[sys.argv.index('-u') + 1]
    else:
      file_path = sys.argv[sys.argv.index('--upload') + 1]
    if exists(file_path):
      note = upload(file_path)
    else:
      print('CAN NOT FIND FILE @${0}'.format(file_path))
  else:
    note = sys.argv[1]

  create_note(note)