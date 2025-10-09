## Deployment


### Build Docker image

```
docker build -t abhishekdey001/housing-price-app:latest .

```

### Run Docker container

```

docker run -p 8501:8501 -p 8000:8000 abhishekdey001/housing-price-app:latest

```

### Docker Hub Login

```

docker login

```

### Push the image to docker hub

```

docker push abhishekdey001/housing-price-app:latest

```


### Pull the image from docker hub

```
docker pull abhishekdey001/housing-price-app:latest

```

### List Docker images

```
docker images -a

```

### List Docker containers

```
docker ps

```

### Stop Docker container

```

docker stop <container-id>

```

### Delete Docker image


```
docker rmi -f <image-id>

```

## Follow below links for deployment in Cloud 

1. [AWS EC2 Instance](AWS_EC2/README.md)

2. [AWS Lightsail](AWS_Lightsail/README.md)

3. [Google Cloud Run](Google_Cloud_Run/README.md)

4. [Microsoft Azure Container Apps](Azure_Container_Apps/README.md)

