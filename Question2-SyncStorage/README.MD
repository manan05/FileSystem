###Manan Arora
###UTA ID: 1002143328
###Muskan Jain 
###UTA ID: 1002033280

# Server-Client File Synchronization System

This project implements a simple server-client file synchronization system using gRPC and Python. It consists of two main components: a server (`server.py`) and a client (`client.py`). The server handles file synchronization requests from clients, while the client monitors a local folder for changes and syncs these changes with the server.

## Server (`server.py`)

The server script implements a gRPC service that provides a `SyncFileOperation` method for handling file synchronization requests from clients. It creates two folders (`CLIENT_FOLDER` and `SYNC_FOLDER`) to store client files and synchronized files, respectively.

### Usage
1. Run the server script (`server.py`).
2. The server will start on port 50050 and wait for client synchronization requests.

## Client (`client.py`)

The client script monitors a local folder (`CLIENT_FOLDER`) for file changes using the `watchdog` library. When a file is modified, created, deleted, or moved, the client syncs these changes with the server using the `SyncFileOperation` method.

### Usage
1. Run the client script (`client.py`).
2. The client will start monitoring the `CLIENT_FOLDER` for changes and sync them with the server.

## Dependencies
- Python 3
- gRPC
- watchdog

### Installation
You can install the dependencies using pip:
```bash
pip install watchdog
```

