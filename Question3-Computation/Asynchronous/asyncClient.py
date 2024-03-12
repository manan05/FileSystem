import grpc
import asyncComputation_pb2
import asyncComputation_pb2_grpc
import threading

def add(stub, a, b):
    print(f"Request sent to add: {a} and {b}")
    response = stub.Add(asyncComputation_pb2.AddRequest(a=a, b=b))
    print(f"\nResult: {a} + {b} = ", response.result)

def sort(stub, inputList):
    print(f"Request sent to sort: {inputList}")
    response = stub.Sort(asyncComputation_pb2.SortRequest(inputList=inputList))
    print(f"\nGiven List: {inputList} and Sorted List: ", response.sortedList)

def asyncFun():
    channel = grpc.insecure_channel("localhost:50055")
    stub = asyncComputation_pb2_grpc.asyncComputationStub(channel)
    while True:
        print("1. Add Operation")
        print("2. Sort Operation")
        print("3. Exit")
        oper = input("Enter the number of the operation: ")
        if oper == "1":
            a = int(input("Enter the 1st number: "))
            b = int(input("Enter the 2nd number: "))
            threading.Thread(target=add, args=(stub, a, b)).start()
        elif oper == "2":
            n = int(input("Enter the number of elements in the list: "))
            inputList = []
            for i in range(n):
                inputList.append(int(input(f"Enter element, {i+1}: ")))
            threading.Thread(target=sort, args=(stub, inputList)).start()
        elif oper == "3":
            print("Exiting!!!")
            break
        else:
            print("Invalid operation")

if __name__ == "__main__":
    print("---------------------------------------")
    print("Asynchronous Computation Client!!!")
    asyncFun()