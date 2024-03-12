###Manan Arora
###UTA ID: 1002143328
###Muskan Jain 
###UTA ID: 1002033280

# Asynchronous Computation Client-Server System

This project implements a simple client-server system for performing asynchronous computations using gRPC and Python. In asynchronous RPC, the client makes the RPC call to the server and continues its execution.  After completing the computation, the server sends the result of the call back to the client. It consists of two main components: an asynchronous server (`asyncServer.py`) and an asynchronous client (`asyncClient.py`). The server provides two operations: addition and sorting, while the client allows users to interactively request these operations.

## Server (`asyncServer.py`)

The server script implements a gRPC service that provides `Add` and `Sort` methods for performing addition and sorting operations, respectively. 

### Usage
1. Run the server script (`asyncServer.py`).
2. The server will start on port 50055 and wait for client requests.

## Client (`asyncClient.py`)

The client script allows users to interactively select an operation (addition or sorting) and provide input values. It then sends these requests to the server in separate threads to demonstrate asynchronous behavior.

### Usage
1. Run the client script (`asyncClient.py`).
2. Follow the on-screen prompts to select an operation and provide input values.
3. The client will send the requests to the server in separate threads, allowing for concurrent execution.

## Dependencies
- Python 3.x
- gRPC

