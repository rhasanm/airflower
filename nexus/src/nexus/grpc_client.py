import grpc

import nexus.protos.strategia_pb2 as pb2
import nexus.protos.strategia_pb2_grpc as pb2_grpc
import logging

logging.basicConfig(level=logging.INFO)

class NexusClient:
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50052")
        self.stub = pb2_grpc.DecisionServiceStub(self.channel)

    def request_decision(self, data):
        logging.info(f"Sending request to Strategia with data: {data}")
        request = pb2.DecisionRequest(data=data)
        try:
            response = self.stub.MakeDecision(request)
            logging.info(f"Received decision from Strategia: {response.message}")
            return response.message
        except grpc.RpcError as e:
            logging.error(f"RPC Error: {e}")
            return None


if __name__ == "__main__":
    nexus_client = NexusClient()
    decision = nexus_client.request_decision("request_approve")
    if decision:
        logging.info(f"Decision received: {decision}")
    else:
        logging.error("Failed to get a decision.")
