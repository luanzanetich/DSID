# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import operations_pb2 as operations__pb2


class LongMessageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendLong = channel.unary_unary(
                '/proto.LongMessageService/SendLong',
                request_serializer=operations__pb2.Long.SerializeToString,
                response_deserializer=operations__pb2.Long.FromString,
                )


class LongMessageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendLong(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LongMessageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendLong': grpc.unary_unary_rpc_method_handler(
                    servicer.SendLong,
                    request_deserializer=operations__pb2.Long.FromString,
                    response_serializer=operations__pb2.Long.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.LongMessageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LongMessageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendLong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.LongMessageService/SendLong',
            operations__pb2.Long.SerializeToString,
            operations__pb2.Long.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class EightLongMessageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendLong = channel.unary_unary(
                '/proto.EightLongMessageService/SendLong',
                request_serializer=operations__pb2.EightLong.SerializeToString,
                response_deserializer=operations__pb2.Long.FromString,
                )


class EightLongMessageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendLong(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EightLongMessageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendLong': grpc.unary_unary_rpc_method_handler(
                    servicer.SendLong,
                    request_deserializer=operations__pb2.EightLong.FromString,
                    response_serializer=operations__pb2.Long.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.EightLongMessageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EightLongMessageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendLong(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.EightLongMessageService/SendLong',
            operations__pb2.EightLong.SerializeToString,
            operations__pb2.Long.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class VoidMessageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendVoid = channel.unary_unary(
                '/proto.VoidMessage/SendVoid',
                request_serializer=operations__pb2.Void.SerializeToString,
                response_deserializer=operations__pb2.Void.FromString,
                )


class VoidMessageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendVoid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VoidMessageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendVoid': grpc.unary_unary_rpc_method_handler(
                    servicer.SendVoid,
                    request_deserializer=operations__pb2.Void.FromString,
                    response_serializer=operations__pb2.Void.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.VoidMessage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VoidMessage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendVoid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.VoidMessage/SendVoid',
            operations__pb2.Void.SerializeToString,
            operations__pb2.Void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class StringMessageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendString = channel.unary_unary(
                '/proto.StringMessageService/SendString',
                request_serializer=operations__pb2.StringMessage.SerializeToString,
                response_deserializer=operations__pb2.StringMessage.FromString,
                )


class StringMessageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StringMessageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendString': grpc.unary_unary_rpc_method_handler(
                    servicer.SendString,
                    request_deserializer=operations__pb2.StringMessage.FromString,
                    response_serializer=operations__pb2.StringMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.StringMessageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StringMessageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.StringMessageService/SendString',
            operations__pb2.StringMessage.SerializeToString,
            operations__pb2.StringMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MovieMessageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMovie = channel.unary_unary(
                '/proto.MovieMessageService/SendMovie',
                request_serializer=operations__pb2.Movie.SerializeToString,
                response_deserializer=operations__pb2.Movie.FromString,
                )


class MovieMessageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMovie(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MovieMessageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMovie': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMovie,
                    request_deserializer=operations__pb2.Movie.FromString,
                    response_serializer=operations__pb2.Movie.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.MovieMessageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MovieMessageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMovie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/proto.MovieMessageService/SendMovie',
            operations__pb2.Movie.SerializeToString,
            operations__pb2.Movie.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
