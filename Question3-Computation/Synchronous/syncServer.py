import grpc
import syncComputation_pb2
import syncComputation_pb2_grpc

from concurrent import futures

class computationServicer(syncComputation_pb2_grpc.computationServicer):
    def Add(self, request, context):
        print("Add function called")
        result = request.a + request.b
        response = syncComputation_pb2.AddResponse(result = result)
        return response
        
    
    def Sort(self, request, context):
        print("Sort function called")
        sortedList = sorted(request.inputList)
        response = syncComputation_pb2.SortResponse(sortedList = sortedList)
        return response
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    syncComputation_pb2_grpc.add_computationServicer_to_server(computationServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Server started at port 50052")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()