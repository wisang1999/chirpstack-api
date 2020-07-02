# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from chirpstack_api.as_pb.external.api import user_pb2 as chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class UserServiceStub(object):
    """UserService is the service managing the user access.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/api.UserService/List',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.ListUserRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.ListUserResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/api.UserService/Get',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.GetUserRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.GetUserResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/api.UserService/Create',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.CreateUserResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/api.UserService/Update',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Delete = channel.unary_unary(
                '/api.UserService/Delete',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdatePassword = channel.unary_unary(
                '/api.UserService/UpdatePassword',
                request_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.UpdateUserPasswordRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class UserServiceServicer(object):
    """UserService is the service managing the user access.
    """

    def List(self, request, context):
        """Get user list.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get data for a particular user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Create a new user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update an existing user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete a user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePassword(self, request, context):
        """UpdatePassword updates a password.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.ListUserRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.ListUserResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.GetUserRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.GetUserResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.CreateUserRequest.FromString,
                    response_serializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.CreateUserResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.UpdateUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.DeleteUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdatePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePassword,
                    request_deserializer=chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.UpdateUserPasswordRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """UserService is the service managing the user access.
    """

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserService/List',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.ListUserRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.ListUserResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserService/Get',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.GetUserRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.GetUserResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserService/Create',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.CreateUserRequest.SerializeToString,
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserService/Update',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.UpdateUserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserService/Delete',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.DeleteUserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.UserService/UpdatePassword',
            chirpstack__api_dot_as__pb_dot_external_dot_api_dot_user__pb2.UpdateUserPasswordRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
