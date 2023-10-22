import grpc
import service_pb2
import service_pb2_grpc

def hello_world(request):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.HelloWorldStub(channel)
        response = stub.SayHello(service_pb2.HelloRequest(name="Pyramid"))
    return {"message": response.message}