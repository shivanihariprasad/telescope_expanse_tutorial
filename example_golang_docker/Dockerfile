FROM golang:1.23

WORKDIR /go/src/ucsdntexample

RUN apt-get update && apt-get install -y parallel
RUN git clone https://github.com/CAIDA/goucsdnt.git

WORKDIR /go/src/ucsdntexample/goucsdnt/cmd/analyzepcaps3/

RUN go mod init

RUN go get github.com/CAIDA/goucsdnt

RUN go mod download all
RUN go mod tidy

RUN go build -o /go/bin/ucsdntexample 

RUN mkdir /output
CMD ["/go/bin/ucsdntexample"]
