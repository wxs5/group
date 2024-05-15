
import time,os
path = "D:\\group\\file"
gp = "D:\\Git\\bin\\git"
os.chdir(path)
flag = False
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    import os
    os.system("pip install watchdog")
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        flag = True
        print(f'File created: {event.src_path}')
    def on_renamed(self, event):
        flag = True
        print(f'File renamed: {event.src_path}')
    def on_modified(self, event):
        if  not event.is_directory:
            flag = True
            
        print(f"File {event.src_path} has been modified")

observer = Observer()
event_handler = MyHandler()
observer.schedule(event_handler, path=path, recursive=True)
observer.start()
try:
    while True:
        if flag:
            os.system("git pull")
            os.system(f"{gp} add --all")
            os.system(f"{gp} commit -m au")
            os.system(f"{gp} push")
        
        time.sleep(3)
except KeyboardInterrupt:
    observer.stop()

observer.join()
