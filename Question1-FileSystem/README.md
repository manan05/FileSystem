### Manan Arora
### UTA ID: 1002143328

# File System Server and Client

## Description
Implement a multi-threaded file server that supports UPLOAD, DOWNLOAD, DELETE, and RENAME file operations. Use different folders to hold files downloaded to the client or uploaded to the server. It includes a server-side script (`fileSystemServer.py`) and a client-side script (`fileSystemClient.py`).

## Server (`fileSystemServer.py`)
The server script implements the following gRPC service methods:
- `UploadFunction`: Uploads a file to the upload directory.
- `DownloadFunction`: Downloads a file from the upload directory.
- `DeleteFunction`: Deletes a file from the upload directory.
- `RenameFunction`: Renames a file in the upload directory.

### Usage
1. Run the server script (`fileSystemServer.py`).
2. The server will start on port 5000 and wait for client requests.

## Client (`fileSystemClient.py`)
The client script provides a command-line interface for interacting with the file system server. It allows the user to perform the following operations:
- Upload a file to the server.
- Download a file from the server.
- Delete a file from the server.
- Rename a file on the server.

### Usage
1. Run the client script (`fileSystemClient.py`).
2. Follow the on-screen prompts to select an operation and provide the necessary inputs.

