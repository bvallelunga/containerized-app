# rm all docker containers and images
docker rm $(docker ps -a -q) && docker rmi $(docker images -q)
