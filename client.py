import grpc
import hola_pb2
import hola_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hola_pb2_grpc.HelloWorldStub(channel)
        response = stub.SayHello(hola_pb2.HelloRequest(name="Mundo"))
    print(response.message)


if __name__ == "__main__":
    run()
