import hashlib
import shelve
import time
import os
from . import helpers, monit, TITLE, DATABASE, monitor

def main():
    helpers.hello(TITLE)

    files = {}

    while True:
        for file in monit.getFiles(monitor):
            hash = hashlib.sha256()

            try:
                with open(file, 'rb') as f:
                    for chunk in iter(lambda: f.read(2048), b""):
                        hash.update(chunk)
                    sha256 = hash.hexdigest()

                if file in files and sha256 != files[file]:
                    print(f'{file} has been changed! {time.strftime("%Y-%m-%d %H:%M:%S")}')

                files[file] = sha256
                with shelve.open(DATABASE) as s:
                    s[file] = files[file]
            except FileNotFoundError:
                continue

        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        helpers.bye(TITLE)