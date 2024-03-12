import grpc
import SyncFiles_pb2
import SyncFiles_pb2_grpc
import threading
import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

CLIENT_FOLDER = "clientFolder"
SYNC_FOLDER = "syncFolder"
INTERVAL = 10

last_sync_time = time.time()

def sendFileOperation(fileName, content):
    with grpc.insecure_channel('localhost:50050') as channel:
        stub = SyncFiles_pb2_grpc.SynchronizedFileSystemStub(channel)
        operation = SyncFiles_pb2.FileOperation(fileName=fileName, content=content)
        response = stub.SyncFileOperation(operation)
        print("File operation synced: ", response.success)

def syncFile(filePath):
    fileName = os.path.relpath(filePath, CLIENT_FOLDER)
    with open(filePath, 'rb') as f:
        content = f.read()
    sendFileOperation(fileName, content)

def deleteSyncFile(filePath):
    fileName = os.path.relpath(filePath, CLIENT_FOLDER)
    syncFilePath = os.path.join(SYNC_FOLDER, fileName)
    if os.path.exists(syncFilePath):
        os.remove(syncFilePath)
        print(fileName + " deleted from syncFolder!!")

class EventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global last_sync_time
        if not event.is_directory:
            file_path = event.src_path
            last_modified_time = os.path.getmtime(file_path)
            if last_modified_time > last_sync_time:
                print("File modified", file_path)
                syncFile(file_path)
                last_sync_time = time.time()
    
    def on_created(self, event):
        if not event.is_directory:
            syncFile(event.src_path)
    
    def on_deleted(self, event):
        if not event.is_directory:
            deleteSyncFile(event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            syncFile(event.dest_path)
            deleteSyncFile(event.src_path)

def check_folder_changes():
    observer = Observer()
    observer.schedule(EventHandler(), CLIENT_FOLDER, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

if __name__ == '__main__':
    sync_thread = threading.Thread(target=check_folder_changes, daemon=True)
    sync_thread.start()
    print("Client running!!!")
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Exiting...")