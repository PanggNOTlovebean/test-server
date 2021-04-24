$ git clone git@github.com:PanggNOTlovebean/test-server.git
$ docker build -t test-server .
```


### Run the container
Create a container from the image.
```
$ docker run --name pangg-server -d -p 11118:8080 test-server
```


