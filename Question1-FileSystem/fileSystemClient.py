import grpc
import fileSystem_pb2
import fileSystem_pb2_grpc
import os

def uploadFunction(stub):
    fileName = input("Enter the name of the file to upload: ")
    try:
        with open(fileName, "rb") as file:
            content = file.read()
        uploadResponse = stub.UploadFunction(fileSystem_pb2.UploadRequest(fileName=fileName, fileContent=content))
        print(uploadResponse.response)
    except FileNotFoundError:
        print("File not found")
    
def downloadFunction(stub):
    fileName = input("Enter the name of the file to be downloaded: ")
    downloadResponse = stub.DownloadFunction(fileSystem_pb2.DownloadRequest(fileName=fileName))
    if downloadResponse:
        with open(os.path.join('downloads',fileName), "wb") as file:
            file.write(downloadResponse.fileContent)
        print("File downloaded successfully!!!")
    else:
        print("File not found")

def deleteFunction(stub):
    fileName = input("Enter the name of the file to be deleted: ")
    deleteResponse = stub.DeleteFunction(fileSystem_pb2.DeleteRequest(fileName=fileName))
    print("Delete_response: ",deleteResponse.response)

def renameFunction(stub):
    oldFileName = input("Enter the name of the file to be renamed: ")
    newFileName = input("Enter the new name for this file: ")
    renameResponse = stub.RenameFunction(fileSystem_pb2.RenameRequest(oldFileName=oldFileName, newFileName=newFileName))
    print("Rename_response: ",renameResponse.response)

def driver():
    channel = grpc.insecure_channel('localhost:5000')
    stub = fileSystem_pb2_grpc.Q1FileSystemStub(channel)

    while True:
        print("---------------------------------------")
        print("Welcome to File System Client!!!")
        print("Select an operation:")
        print("1. Upload file")
        print("2. Download file")
        print("3. Delete file")
        print("4. Rename file")
        print("5. Exit")
        n = input("Enter your choice: ")

        if n == '1':
            uploadFunction(stub)
        elif n == '2':
            downloadFunction(stub)
        elif n == '3':
            deleteFunction(stub)
        elif n == '4':
            renameFunction(stub)
        elif n == '5':
            break
        else:
            print("Invalid choice. Try again!!!")

if __name__ == "__main__":
    driver()