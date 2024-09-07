from concurrent import futures
import logging
import grpc
from airflower_protobufs import vlr_pb2, vlr_pb2_grpc

class VLRStrategiaServicer(vlr_pb2_grpc.VLRStrategiaServicer):
    def __init__(self) -> None:
        super().__init__()

    def GetVLRThreshold(self, request, context):
        return vlr_pb2.VLRThresholdResponse(threshold=10)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vlr_pb2_grpc.add_VLRStrategiaServicer_to_server(VLRStrategiaServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
