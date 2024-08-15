package main

import (
	"log"
	"net"
	"net/http"
	"net/rpc"
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

type LongMessageService int

func (lms *LongMessageService) MultiplyByTwo(message Long, reply *Long) error {
	result := Long{
		Value: message.Value * 2,
	}
	*reply = result
	return nil
}

type VoidMessageService int

func (vms *VoidMessageService) SendVoid(message Void, reply *Void) error {
	return nil
}

type EightLongMessageService int

func (elms *EightLongMessageService) GetFirstLong(message EightLong, reply *Long) error {
	result := Long{
		Value: message.Value1,
	}
	*reply = result
	return nil
}

type StringMessageService int

func (sms *StringMessageService) SendString(message String, reply *String) error {
	reversed := reverseString(message.Value)
	result := String{
		Value: reversed,
	}
	*reply = result
	return nil
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

type MovieMessageService int

func (mms *MovieMessageService) SendMovie(message Movie, reply *Movie) error {
	message.FoiEnviado = true
	*reply = message
	return nil
}

func main() {
	longMessageService := new(LongMessageService)
	err := rpc.Register(longMessageService)
	if err != nil {
		log.Fatal("Erro ao registrar LongMessageService: ", err)
	}

	voidMessageService := new(VoidMessageService)
	err = rpc.Register(voidMessageService)
	if err != nil {
		log.Fatal("Erro ao registrar VoidMessageService: ", err)
	}

	eightLongMessageService := new(EightLongMessageService)
	err = rpc.Register(eightLongMessageService)
	if err != nil {
		log.Fatal("Erro ao registrar EightLongMessageService: ", err)
	}

	stringMessageService := new(StringMessageService)
	err = rpc.Register(stringMessageService)
	if err != nil {
		log.Fatal("Erro ao registrar StringMessageService: ", err)
	}

	movieMessageService := new(MovieMessageService)
	err = rpc.Register(movieMessageService)
	if err != nil {
		log.Fatal("Erro ao registrar MovieMessageService: ", err)
	}

	rpc.HandleHTTP()

	listener, err := net.Listen("tcp", ":8080")
	if err != nil {
		log.Fatal("Listener error: ", err)
	}
	log.Println("Servidor iniciado na porta 8080")
	err = http.Serve(listener, nil)
	if err != nil {
		log.Fatal("Erro ao iniciar servidor: ", err)
	}
}
