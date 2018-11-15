docker pull docker.io/leo160886/alert:latest
docker stop my-application
docker rm my-application
docker rmi docker.io/leo160886/alert:latest:current
docker tag docker.io/leo160886/alert:latest docker.example.com/my-application:current
docker run -d --name my-application docker.io/leo160886/alert:latest
