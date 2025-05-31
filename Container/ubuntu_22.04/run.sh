docker build --platform linux/amd64 -t pwnlab-22.04 .
docker-compose up -d
docker exec -it pwnlab-22.04 bash
# o para root:
#docker exec -it --user root pwnlab-22.04 bash
