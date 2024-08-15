import argparse
import grpc
import sys
import operations_pb2
import operations_pb2_grpc
import time

def run(ip_address, port, size):
    if size <= 0:
        print("O tamanho da string deve ser maior que zero.")
        return

    with grpc.insecure_channel(f'{ip_address}:{port}') as channel:
        stub = operations_pb2_grpc.StringMessageServiceStub(channel)

        string_value = "A" * size  # Cria uma string com o tamanho especificado
        string_message = operations_pb2.StringMessage(value=string_value)

        start_time = time.time()
        response = stub.SendString(string_message)
        end_time = time.time()

        print("Resposta:", end_time - start_time)


## primeiro arguemento é da conexão [0,1] e o segundo é do tamanho da string

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gRPC client')
    parser.add_argument('connection', type=int, choices=[0, 1], help='0 for localhost, 1 for remote server')
    parser.add_argument('size', type=int, help='Size of the string')
    parser.add_argument('--ip', type=str, help='IP address of the remote server')
    parser.add_argument('--port', type=str, help='Port of the remote server')

    args = parser.parse_args()

    if args.connection == 0:
        run('localhost', '50051', args.size)
    else:
        if not args.ip or not args.port:
            parser.error('IP address and port are required for remote server connection.')

        run(args.ip, args.port, args.size)
