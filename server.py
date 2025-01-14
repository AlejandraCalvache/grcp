from concurrent import futures
import grpc
import hola_pb2
import hola_pb2_grpc


class HelloWorldService(hola_pb2_grpc.HelloWorldServicer):
    def SayHello(self, request, context):
        return hola_pb2.HelloResponse(message=f"Hola, {request.name}! Bienvenido a gRPC.")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hola_pb2_grpc.add_HelloWorldServicer_to_server(HelloWorldService(), server)
    server.add_insecure_port('[::]:50051')
    print("Servidor gRPC corriendo en el puerto 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
