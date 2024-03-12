# 🌐 Distributed File and Computation Service

## 📝 Project Description

In this project, I have implemented a simple file upload and download service and a computation service using remote procedure call (RPC) based communication. The project is divided into three parts:

### Part 1

Implement a multi-threaded file server that supports UPLOAD, DOWNLOAD, DELETE, and RENAME file operations. Different folders are used to hold files downloaded to the client or uploaded to the server.

### Part 2

Create a Dropbox-like synchronized storage service where a helper thread handles file transfer between the client and the server transparently. Changes made to the synchronized folder on the client side are automatically sent to the server to update the folder on the server side.

### Part 3

Implement a computation server to support add(i, j) and sort(array A) operations using synchronous and asynchronous RPCs. In synchronous RPC, the client waits for the result from the server, while in asynchronous RPC, the client continues after receiving an acknowledgment from the server.

## 💻 Technologies Used

- **Python**: Programming language used for implementation.
- **gRPC**: Framework used for remote procedure call (RPC) based communication.
- **Multi-threading**: Used in the file server to handle multiple client requests concurrently.
- **Watchdog**: Used to implement a synchronization feature in the file system

## ✨ Features

- **File Operations**: Supports UPLOAD, DOWNLOAD, DELETE, and RENAME file operations.
- **Transparent Synchronization**: Automatically synchronizes changes made to the synchronized folder between client and server.
- **Computation Service**: Provides support for add(i, j) and sort(array A) operations.

## 🚀 Getting Started

To get started with the Distributed File and Computation Service, follow these steps:

1. Clone this repository.
2. Install the required dependencies (Python, gRPC, watchdog).
3. Run the server and the client as per the readme provided in the folder.
4. Start using the provided client application to interact with the services.

