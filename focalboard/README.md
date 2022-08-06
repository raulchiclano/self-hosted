# Deploy Focalboard with Docker


## Docker-Compose

Docker-Compose provides the option to automate the build and run step, or even include some of the steps from the [personal server setup](https://www.focalboard.com/download/personal-edition/ubuntu/).

To start the server run

```
docker-compose up -d
```

docker exec -ti --user root focalboard-postgres chown -R postgres:postgres var/lib/postgresql/data

This will automatically build the focalboard image and start it with the http port mapping.

```
