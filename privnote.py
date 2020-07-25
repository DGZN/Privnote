import sys
import json
import os.path
import subprocess
import pyperclip
import pyPrivnote as pn

from os import path

dir_name = os.getcwd()
upload_url = "https://api.anonfiles.com/upload"

def exists(file):
  full_path = os.path.join(dir_name, file)
  return path.exists(file) or path.exists(full_path)

def upload(file):
  proc = subprocess.Popen('curl -q -s -F "file=@{0}" {1}'.format(file, upload_url), stdout=subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  obj = json.loads(out)
  url = obj['data']['file']['url']['short']
  return url

def create_note(note):
  note_link = pn.create_note(note)
  pyperclip.copy(note_link)
  spam = pyperclip.paste()
  print('SELF-DESTRUCT URL: {0}'.format(note_link))

if '-h' in sys.argv or '--help' in sys.argv:
  print('Privnote is a tool to create a self-destructing note with an optional anonymous file upload url')
  print('(text) (--upload file_path) (text)')
  print('--upload file_path file name or path to upload anonymously')
else:
  if len(sys.argv) < 2:
    print('YOU MUST SUPPLY A NOTE')
  else:
    if '--upload' in sys.argv:
      upload_flag = sys.argv.index('--upload')
      file_path = sys.argv[upload_flag+1]
      if exists(file_path):
        uploaded_url = upload(file_path)
        del sys.argv[upload_flag]
        sys.argv[upload_flag] = uploaded_url
        note = ' '.join(sys.argv[1:])
      else:
        print('CAN NOT FIND FILE @${0}'.format(file_path))
    else:
      note = sys.argv[1]

    create_note(note)