import logging
import grpc
from airflower_protobufs import vlr_pb2_grpc, vlr_pb2

def get_vlr_threshold(stub: vlr_pb2_grpc.VLRStrategiaStub):
    threshold = stub.GetVLRThreshold(vlr_pb2.VLRThresholdRequest(strategy="none"))
    return threshold

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = vlr_pb2_grpc.VLRStrategiaStub(channel=channel)
        print(get_vlr_threshold(stub=stub))

if __name__ == '__main__':
    logging.basicConfig()
    run()