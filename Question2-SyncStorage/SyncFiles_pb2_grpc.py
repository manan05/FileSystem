# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import SyncFiles_pb2 as SyncFiles__pb2


class SynchronizedFileSystemStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SyncFileOperation = channel.unary_unary(
                '/SynchronizedFileSystem/SyncFileOperation',
                request_serializer=SyncFiles__pb2.FileOperation.SerializeToString,
                response_deserializer=SyncFiles__pb2.OperationResult.FromString,
                )


class SynchronizedFileSystemServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SyncFileOperation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SynchronizedFileSystemServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SyncFileOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.SyncFileOperation,
                    request_deserializer=SyncFiles__pb2.FileOperation.FromString,
                    response_serializer=SyncFiles__pb2.OperationResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SynchronizedFileSystem', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SynchronizedFileSystem(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SyncFileOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SynchronizedFileSystem/SyncFileOperation',
            SyncFiles__pb2.FileOperation.SerializeToString,
            SyncFiles__pb2.OperationResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
