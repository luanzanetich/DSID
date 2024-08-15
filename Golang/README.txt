Para executar os testes, primeiro será necessário instalar a linguagem go;
			https://go.dev/doc/install

Em seguida, basta executar o servidor com o seguinte código:

go run main.go (null ou 1). 
//Sendo 1 para especificar logo em seguida a porta em que deseja iniciar o servidor,
//ou null para iniciar na porta padrão (8080)

Com servidor iniciado, basta executar em outro terminal o main.go dentro da pasta Cliente:

go run main.go <op> <useCustomIP> <customIP> <customPort>
    sendo op = 'long', 'void', 'eightlong', 'string (lenght)', ou 'movie'.
    useCustomIP = null ou 1
    customIP = ip desejado
    customPort = porta desejada

Exemplo:
go run main.go movie 1 192.168.1.54 5050