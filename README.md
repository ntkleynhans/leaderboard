# LeaderBoard 

This application process and set of provided results and generates a leaderboard

## Requires

* Python3

## Execute

### With file
```bash
python3 ranking_table.py data/in.sample.txt
```

### With stdin
```bash
python3 ranking_table.py < data/in.sample.txt
```

### Expected output
````bash
$ python3 ranking_table.py < data/in.sample.txt
Tarantulas, 6 pts
Lions, 5 pts
FC Awesome, 1 pts
Snakes, 1 pts
````

## Docker

Make sure Docker is installed - [Docker Install Guid](https://docs.docker.com/get-docker/)

### Build container
````bash
 docker build -t ranking .
 ````

 ### Run script
```bash
docker run -it ranking ranking_table.py data/in.sample.txt
````
