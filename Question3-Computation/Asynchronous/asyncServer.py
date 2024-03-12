import grpc
import asyncComputation_pb2
import asyncComputation_pb2_grpc
import time
from concurrent import futures

class ComputationServicer(asyncComputation_pb2_grpc.asyncComputationServicer):
    def Add(self, request, context):
        print(f"Request received! Add {request.a} and {request.b}")
        result = request.a + request.b
        time.sleep(5)
        return asyncComputation_pb2.AddResponse(result=result)

    def Sort(self, request, context):
        print(f"Request recieved! Sort :", request.inputList)
        sortedList = sorted(request.inputList)
        time.sleep(5)
        return asyncComputation_pb2.SortResponse(sortedList=sortedList)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) 
    asyncComputation_pb2_grpc.add_asyncComputationServicer_to_server(ComputationServicer(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    print("Server started at port 50055")
    server.wait_for_termination()

if __name__ == '__main__':
   serve()