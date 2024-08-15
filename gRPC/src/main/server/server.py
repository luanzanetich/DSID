import grpc
from concurrent import futures
import time
import sys
import threading

import operations_pb2
import operations_pb2_grpc

##para iniciar, basta chamar a função com parâmetro 0 para abrir na porta padrão,
##ou parâmetro 1 para escolher a porta desejada. (python server.py 1 --port 50)

class LongMessageService(operations_pb2_grpc.LongMessageServiceServicer):
    def SendLong(self, request, context):
        # Lógica da operação com argumento e valor de retorno (Long)
        return operations_pb2.Long(value=request.value)

class EightLongMessageService(operations_pb2_grpc.EightLongMessageServiceServicer):
    def SendLong(self, request, context):
        # Lógica da operação com argumento e valor de retorno (Long)
        return operations_pb2.Long(value=request.value_1)
    
class VoidMessageService(operations_pb2_grpc.VoidMessageServicer):
    def SendVoid(self, request, context):
        # Lógica da operação com argumento e valor de retorno (Void)
        return operations_pb2.Void()

class StringMessageService(operations_pb2_grpc.StringMessageServiceServicer):
    def SendString(self, request, context):
        # Lógica da operação com argumento e valor de retorno (StringMessage)
        return request

class MovieMessageService(operations_pb2_grpc.MovieMessageServiceServicer):
    def SendMovie(self, request, context):
        # Lógica da operação com a mensagem de filme recebida e retorno (Movie)
        # Operação que atualiza a variável "foiEnviado" para true
        request.foiEnviado = True

        return request

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    operations_pb2_grpc.add_LongMessageServiceServicer_to_server(LongMessageService(), server)
    operations_pb2_grpc.add_EightLongMessageServiceServicer_to_server(EightLongMessageService(), server)
    operations_pb2_grpc.add_StringMessageServiceServicer_to_server(StringMessageService(), server)
    operations_pb2_grpc.add_VoidMessageServicer_to_server(VoidMessageService(), server)
    operations_pb2_grpc.add_MovieMessageServiceServicer_to_server(MovieMessageService(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"Servidor iniciado na porta {port}")

    # Função para fechar o servidor ao pressionar a tecla "Enter"
    def close_server():
        input("Pressione Enter para fechar o servidor...")
        server.stop(0)

    # Inicia uma thread para aguardar o input do usuário
    threading.Thread(target=close_server, daemon=True).start()

    server.wait_for_termination()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Por favor, especifique o modo de execução (0 ou 1).")
        sys.exit(1)

    mode = int(sys.argv[1])
    if mode == 0:
        serve(50051)
    elif mode == 1:
        if len(sys.argv) < 4 or sys.argv[2] != "--port":
            print("Por favor, especifique a porta após o modo de execução 1.")
            sys.exit(1)
        port = int(sys.argv[3])
        serve(port)
    else:
        print("Modo de execução inválido. Use 0 ou 1.")
        sys.exit(1)
