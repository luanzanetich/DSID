package main

import (
	"fmt"
	"log"
	"net/rpc"
	"os"
	"strconv"
	"strings"
	"time"
)

type Long struct {
	Value int64
}

type Void struct{}

type EightLong struct {
	Value1 int64
	Value2 int64
	Value3 int64
	Value4 int64
	Value5 int64
	Value6 int64
	Value7 int64
	Value8 int64
}

type String struct {
	Value string
}

type Movie struct {
	ID         int64
	Title      string
	Genre      string
	Director   string
	Actors     []Actor
	Duration   int32
	FoiEnviado bool
}

type Actor struct {
	ID            int64
	Name          string
	Surname       string
	CharacterName []string
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Por favor, passe algum tipo (void/long/eightlong/string (lenght)/movie) como argumento.")
		return
	}

	operation := os.Args[1]
	useCustomIP := false
	customIP := ""
	customPort := ""

	if len(os.Args) > 2 {
		useCustomIPStr := os.Args[2]
		useCustomIPInt, err := strconv.Atoi(useCustomIPStr)
		if err != nil {
			log.Fatal("argumento de useCustomIP inválido: ", err)
		}
		useCustomIP = useCustomIPInt == 1
		if useCustomIP {
			if len(os.Args) < 5 {
				fmt.Println("Por favor, forneça o endereço IP e a porta customizados.")
				return
			}
			customIP = os.Args[3]
			customPort = os.Args[4]
		}
	}

	var reply Long
	var voidReply Void
	var movieReply Movie
	var stringReply String

	var client *rpc.Client
	var err error

	if useCustomIP {
		client, err = rpc.DialHTTP("tcp", customIP+":"+customPort)
	} else {
		client, err = rpc.DialHTTP("tcp", "localhost:8080")
	}

	if err != nil {
		log.Fatal("Erro de conexão: ", err)
	}

	switch operation {
	case "long":
		long := Long{Value: 1234567890123456789}

		startTime := time.Now()
		err = client.Call("LongMessageService.MultiplyByTwo", long, &reply)
		endTime := time.Now()

		if err != nil {
			log.Fatal("RPC call error: ", err)
		}
		fmt.Println("Resposta (Long):", reply.Value)

		duration := endTime.Sub(startTime)
		fmt.Println("Tempo:", duration)

	case "void":
		void := Void{}

		startTime := time.Now()
		err = client.Call("VoidMessageService.SendVoid", void, &voidReply)
		endTime := time.Now()

		if err != nil {
			log.Fatal("RPC call error: ", err)
		}

		duration := endTime.Sub(startTime)
		fmt.Println("Tempo:", duration)

	case "eightlong":
		eightLong := EightLong{
			Value1: 1234567890123456789,
			Value2: 2234567890123456789,
			Value3: 3234567890123456789,
			Value4: 4234567890123456789,
			Value5: 5234567890123456789,
			Value6: 6234567890123456789,
			Value7: 7234567890123456789,
			Value8: 8234567890123456789,
		}

		startTime := time.Now()
		err = client.Call("EightLongMessageService.GetFirstLong", eightLong, &reply)
		endTime := time.Now()

		if err != nil {
			log.Fatal("RPC call error: ", err)
		}

		duration := endTime.Sub(startTime)
		fmt.Println("Tempo", duration)

	case "string":
		if len(os.Args) < 3 {
			fmt.Println("Por favor, forneça o comprimento da string")
			return
		}

		lengthStr := os.Args[2]
		length, err := strconv.Atoi(lengthStr)
		if err != nil {
			log.Fatal("argumento de comprimento inválido: ", err)
		}

		stringMessage := String{
			Value: strings.Repeat("X", length),
		}

		startTime := time.Now()
		err = client.Call("StringMessageService.SendString", stringMessage, &stringReply)
		endTime := time.Now()

		if err != nil {
			log.Fatal("RPC call error: ", err)
		}

		duration := endTime.Sub(startTime)
		fmt.Println("Tempo:", duration)

	case "movie":
		movie := Movie{
			ID:       123,
			Title:    "Carros 3",
			Genre:    "Desenho",
			Director: "Brian fee",
			Actors: []Actor{
				{
					ID:            1,
					Name:          "Owen",
					Surname:       "Wilson",
					CharacterName: []string{"Relâmpago Mcqueen"},
				},
				{
					ID:            2,
					Name:          "Paul",
					Surname:       "Newman",
					CharacterName: []string{"Doc Hudson"},
				},
			},
			Duration:   120,
			FoiEnviado: false,
		}

		startTime := time.Now()
		err = client.Call("MovieMessageService.SendMovie", movie, &movieReply)
		endTime := time.Now()

		if err != nil {
			log.Fatal("RPC call error: ", err)
		}

		duration := endTime.Sub(startTime)
		fmt.Println("Tempo", duration)

	default:
		fmt.Println("Tipo de operação inválido. Por favor, utilize 'long', 'void', 'eightlong', 'string', ou 'movie'.")
	}
}
