import grpc
from concurrent import futures
import time

import strategia.protos.strategia_pb2 as pb2
import strategia.protos.strategia_pb2_grpc as pb2_grpc
import grpc
from concurrent import futures
import time
# import pika
import logging

logging.basicConfig(level=logging.INFO)

class StrategiaService(pb2_grpc.DecisionServiceServicer):
    def __init__(self):
        # self.rabbitmq_params = pika.ConnectionParameters(host='localhost')
        pass
    
    def MakeDecision(self, request, context):
        logging.info(f"Received data for decision: {request.data}")
        decision = "Approved" if "approve" in request.data else "Denied"
        
        # self.publish_to_rabbitmq(decision)
        
        return pb2.DecisionReply(message=f"Decision: {decision}")

    # def publish_to_rabbitmq(self, decision):
    #     try:
    #         with pika.BlockingConnection(self.rabbitmq_params) as connection:
    #             channel = connection.channel()
    #             channel.queue_declare(queue='decision_queue', durable=True)
    #             channel.basic_publish(
    #                 exchange='',
    #                 routing_key='decision_queue',
    #                 body=decision,
    #                 properties=pika.BasicProperties(
    #                     delivery_mode=2,
    #                 )
    #             )
    #             logging.info(f"Published decision to RabbitMQ: {decision}")
    #     except Exception as e:
    #         logging.error(f"Failed to publish to RabbitMQ: {e}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_DecisionServiceServicer_to_server(StrategiaService(), server)
    server.add_insecure_port('[::]:50052')
    
    logging.info("Starting Strategia gRPC Server on port 50052")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
