import grpc
import grpc.aio

import syncComputation_pb2
import syncComputation_pb2_grpc

def syncFun():
    channel = grpc.insecure_channel('localhost:50052')
    stub = syncComputation_pb2_grpc.computationStub(channel)
    print("1. Add Operation")
    print("2. Sort Operation")
    print("3. Exit")
    oper = input("Enter the number of the operation: ")
    if oper == '1':
        a = int(input("Enter the 1st number: "))
        b = int(input("Enter the 2nd number: "))
        response = stub.Add(syncComputation_pb2.AddRequest(a=a, b=b))
        print("Result of add operation: ", response.result)
    elif oper == '2':
        n = int(input("Enter the number of elements in the list: "))
        inputList = []
        for i in range(n):
            inputList.append(int(input(f"Enter element, {i+1}: ")))
        response = stub.Sort(syncComputation_pb2.SortRequest(inputList=inputList))
        print("Result of sort operation: ", response.sortedList)
    elif oper == '3':
        print("Exiting...")
        exit()
    else:
        print("Invalid operation")

if __name__ == '__main__':
    while True:
        print("---------------------------------------")
        print("Synchronous Computation Client!!!")
        syncFun()
        