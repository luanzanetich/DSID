import argparse
import grpc
import time
import operations_pb2
import operations_pb2_grpc

def run(ip_address, port):
    with grpc.insecure_channel(f'{ip_address}:{port}') as channel:
        stub = operations_pb2_grpc.VoidMessageStub(channel)

        start_time = time.time()
        response = stub.SendVoid(operations_pb2.Void())
        end_time = time.time()

    print("Resposta do servidor:", end_time - start_time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gRPC client')
    parser.add_argument('connection', type=int, choices=[0, 1], help='0 for localhost, 1 for remote server')
    parser.add_argument('--ip', type=str, help='IP address of the remote server')
    parser.add_argument('--port', type=str, help='Port of the remote server')

    args = parser.parse_args()

    if args.connection == 0:
        run('localhost', '50051')
    else:
        if not args.ip or not args.port:
            parser.error('IP address and port are required for remote server connection.')

        run(args.ip, args.port)
