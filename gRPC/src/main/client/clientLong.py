import argparse
import grpc
import time

import operations_pb2
import operations_pb2_grpc

def run(ip_address, port):
    channel = grpc.insecure_channel(f'{ip_address}:{port}') # Endereço do servidor gRPC
    stub = operations_pb2_grpc.LongMessageServiceStub(channel)

    long_message = operations_pb2.Long(value=1234567890123456789)
    start_time = time.time()
    response = stub.SendLong(long_message, timeout=10)
    end_time = time.time()

    print("Tempo de execução:", end_time - start_time)


if __name__ == '__main__':
    # Crie um objeto ArgumentParser e especifique os argumentos esperados
    parser = argparse.ArgumentParser(description='gRPC client')
    parser.add_argument('connection', type=int, choices=[0, 1], help='0 for localhost, 1 for remote server')
    parser.add_argument('--ip', type=str, help='IP address of the remote server')
    parser.add_argument('--port', type=str, help='Port of the remote server')

    # Analise os argumentos da linha de comando
    args = parser.parse_args()

    # Verifique qual método de conexão foi escolhido
    if args.connection == 0:
        run('localhost', '50051')
    else:
        # Verifique se o endereço IP e a porta foram fornecidos
        if not args.ip or not args.port:
            parser.error('IP address and port are required for remote server connection.')

        run(args.ip, args.port)
