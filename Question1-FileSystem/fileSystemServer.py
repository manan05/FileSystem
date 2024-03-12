import grpc
import os
import fileSystem_pb2
import fileSystem_pb2_grpc
from concurrent import futures

UPLOAD_FILE_PATH = 'uploads'
DOWNLOAD_FILE_PATH = 'downloads'

class FileSystemService(fileSystem_pb2_grpc.Q1FileSystemServicer):

    def __init__(self):
        if not os.path.exists(UPLOAD_FILE_PATH):
            os.makedirs(UPLOAD_FILE_PATH, exist_ok=True)
        if not os.path.exists(DOWNLOAD_FILE_PATH):
           os.makedirs(DOWNLOAD_FILE_PATH, exist_ok=True)

    def UploadFunction(self, request, context):
        fileName = os.path.join(UPLOAD_FILE_PATH, request.fileName)
        #testing filename
        print(fileName)
        with open(fileName, 'wb') as file:
            file.write(request.fileContent)
        print("File uploaded successfully!! ...")
        return fileSystem_pb2.UploadResponse(response="File uploaded successfully!!")
    
    def DownloadFunction(self, request, context):
        print(request.fileName)
        fileName = os.path.join(UPLOAD_FILE_PATH, request.fileName)
        print(fileName)
        try:
            with open(fileName, "rb") as file:
                content = file.read()
            print("File downloaded successfully!!!")
            return fileSystem_pb2.DownloadResponse(fileContent=content)
        except FileNotFoundError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('File not found')
            return fileSystem_pb2.DownloadResponse()

    def DeleteFunction(self, request, context):
        fileName = os.path.join(UPLOAD_FILE_PATH, request.fileName)
        try:
            os.remove(fileName)
            print("File deleted successfully!!!")
            return fileSystem_pb2.DeleteResponse(response="File deleted successfully!!")
        except FileNotFoundError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('File not found')
            return fileSystem_pb2.DeleteResponse()
    
    def RenameFunction(self, request, context):
        oldFileName = os.path.join(UPLOAD_FILE_PATH, request.oldFileName)
        newFileName = os.path.join(UPLOAD_FILE_PATH, request.newFileName)
        try:
            os.rename(oldFileName, newFileName)
            print("File renamed successfully!!!")   
            return fileSystem_pb2.RenameResponse(response="File renamed successfully!!")
        except FileNotFoundError:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('File not found')
            return fileSystem_pb2.RenameResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fileSystem_pb2_grpc.add_Q1FileSystemServicer_to_server(FileSystemService(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    print('File System server started at port 5000 ...')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()