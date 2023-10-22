import grpc
from concurrent import futures
import service_pb2
import service_pb2_grpc

class MyServiceServicer(service_pb2_grpc.HelloWorldServicer):
    def SayHello(self, request, context):
        return service_pb2.HelloResponse(greeting=f"Hello, {request.name}!")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
service_pb2_grpc.add_HelloWorldServicer_to_server(MyServiceServicer(), server)
server.add_insecure_port('[::]:50051')
server.start()