import argparse
import grpc
import time

import operations_pb2
import operations_pb2_grpc


def run(ip_address, port):
    # Cria um canal gRPC para se comunicar com o servidor
    with grpc.insecure_channel(f'{ip_address}:{port}') as channel:
        # Cria um stub para chamar o serviço de mensagem de filme
        stub = operations_pb2_grpc.MovieMessageServiceStub(channel)

        # Cria uma mensagem de filme
        movie = operations_pb2.Movie(
            id=123,
            title="Carros 3",
            genre="Desenho",
            director="Brian Fee",
            actors=[
                operations_pb2.Actor(
                    id=1,
                    name="Owen",
                    surname="Wilson",
                    character_name=["Relâmpago Mcqueen"]
                ),
                operations_pb2.Actor(
                    id=2,
                    name="Paul",
                    surname="Newman",
                    character_name=["Doc Hudson"]
                )
            ],
            duration=120,
            foiEnviado=False
        )

        # Chama o serviço de envio de filme e obtém a resposta
        start_time = time.time()
        response = stub.SendMovie(movie)
        end_time = time.time()

        # Exibe a resposta
        print("Tempo:", end_time - start_time)
        if response.foiEnviado:
            print("O filme foi enviado com sucesso!")
        else:
            print("Ocorreu um erro ao enviar o filme.")


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
