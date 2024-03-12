import grpc
import SyncFiles_pb2
import SyncFiles_pb2_grpc
from concurrent import futures
import os

CLIENT_FOLDER = "clientFolder"
SYNC_FOLDER = "syncFolder"

class SynchronizedFileSystemServicer(SyncFiles_pb2_grpc.SynchronizedFileSystemServicer):
    def __init__(self):
        if not os.path.exists(SYNC_FOLDER):
            os.makedirs(SYNC_FOLDER, exist_ok=True)
        if not os.path.exists(CLIENT_FOLDER):
            os.makedirs(CLIENT_FOLDER, exist_ok=True)
    
    def SyncFileOperation(self, request, context):

        client_filePath = os.path.join(CLIENT_FOLDER, request.fileName)
        sync_filePath = os.path.join(SYNC_FOLDER, request.fileName)
        if request.content is not None:
            with open(client_filePath, 'wb') as file:
               file.write(request.content)
            with open(sync_filePath, 'wb') as file:
                file.write(request.content)
            print(request.fileName + " create/update success !!!")
        return SyncFiles_pb2.OperationResult(success=True, message="success")
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    SyncFiles_pb2_grpc.add_SynchronizedFileSystemServicer_to_server(SynchronizedFileSystemServicer(), server)
    server.add_insecure_port('[::]:50050')
    server.start()
    print("Server Started at port 50050!!")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()