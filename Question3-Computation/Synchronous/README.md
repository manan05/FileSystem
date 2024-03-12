###Manan Arora
###UTA ID: 1002143328
###Muskan Jain 
###UTA ID: 1002033280

# Synchronous Computation Client-Server System

This project implements a simple client-server system for performing synchronous computations using gRPC and Python. In synchronous RPC, the client makes the RPC call and waits for the result from the server. It consists of two main components: a synchronous server (`syncServer.py`) and a synchronous client (`syncClient.py`). The server provides two operations: addition and sorting, while the client allows users to interactively request these operations.

## Server (`syncServer.py`)

The server script implements a gRPC service that provides `Add` and `Sort` methods for performing addition and sorting operations, respectively.

### Usage
1. Run the server script (`syncServer.py`).
2. The server will start on port 50052 and wait for client requests.

## Client (`syncClient.py`)

The client script allows users to interactively select an operation (addition or sorting) and provide input values. It then sends these requests to the server and prints the results.

### Usage
1. Run the client script (`syncClient.py`).
2. Follow the on-screen prompts to select an operation and provide input values.
3. The client will send the requests to the server and print the results.

## Dependencies
- Python 3.x
- gRPC

