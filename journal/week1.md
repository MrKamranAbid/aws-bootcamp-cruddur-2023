# Week 1 - Homework

# Run the dockerfile CMD as an external script

I was having trouble understanding the instruction to run the Dockerfile CMD as an external script. My interpretation was to create a bash script.

Original file

```json
FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
```

```bash
#!/bin/bash

python3 -m flask run --host=0.0.0.0 --port=4567
```

Incoporating the extenral script into the Dockerfile

```bash
FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ddna9eF@dGmEVfbqtTekj4RXUJ4MyQ97cti
COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD [ "./script.sh" ] # Will execute external bash script above
```

**********Note:********** Installing requirements is not needed but I included it to make it simulate what an actual docker file may look like if the python script being executed if it actually had requirements and was not just a default library that came with python. 

# Push and tag a image to DockerHub (they have a free tier)

`docker login` → Command to log into docker 

`docker build -t backend:1.0 .` → Build the docker image based on `Dockerfile` in local directory. 

- `-t` → tag
    - <image-name>:<tags> → `backend:1.0`
- `.` → local directory

```powershell
PS C:\Users\Kamran\Desktop\aws-bootcamp-cruddur-2023-main\backend-flask> docker build -t backend:1.0 .
[+] Building 24.7s (11/11) FINISHED
 => [internal] load build definition from Dockerfile                                                                   0.1s
 => => transferring dockerfile: 294B                                                                                   0.0s
 => [internal] load .dockerignore                                                                                      0.1s
 => => transferring context: 2B                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.10-slim-buster                                            12.7s
 => [auth] library/python:pull token for registry-1.docker.io                                                          0.0s
 => [1/5] FROM docker.io/library/python:3.10-slim-buster@sha256:c059afb019e7aea99777e54b3e0ff8c970ef552b737fb4acbd842  7.0s
 => => resolve docker.io/library/python:3.10-slim-buster@sha256:c059afb019e7aea99777e54b3e0ff8c970ef552b737fb4acbd842  0.0s
 => => sha256:29cd48154c03e9242f1ff4f9895cf886a344fb94c9b71029455e76e11214328f 27.14MB / 27.14MB                       4.9s
 => => sha256:2c59e55cfd719490e5070eb007a3b0ffde33d3e36171a573a3224a050c1e341d 2.78MB / 2.78MB                         2.1s
 => => sha256:3b4b58298de0d8fc8f69c675c463afab2beb87c60a81d13b5620c6b87ee42cbb 11.47MB / 11.47MB                       5.4s
 => => sha256:c059afb019e7aea99777e54b3e0ff8c970ef552b737fb4acbd842916c751fcfd 988B / 988B                             0.0s
 => => sha256:497b91c87ca7d8bf5e0d07d59db1c3e5f29d36ccca1f9878719123e9fbc8f144 1.37kB / 1.37kB                         0.0s
 => => sha256:934047247b20ffd13894ccfd0997208c2e20ec7ba385f40e15d56df2a2912d43 7.79kB / 7.79kB                         0.0s
 => => sha256:6239e464c1ab2cca0154db8e88c6b2eb8969c76dd4cdf8e67e03be54df84ac33 232B / 232B                             2.4s
 => => sha256:609722ad05b6850bc85fa5089312a3294fabfb20978d107d898d4f7804a9269e 3.35MB / 3.35MB                         4.9s
 => => extracting sha256:29cd48154c03e9242f1ff4f9895cf886a344fb94c9b71029455e76e11214328f                              0.9s
 => => extracting sha256:2c59e55cfd719490e5070eb007a3b0ffde33d3e36171a573a3224a050c1e341d                              0.1s
 => => extracting sha256:3b4b58298de0d8fc8f69c675c463afab2beb87c60a81d13b5620c6b87ee42cbb                              0.4s
 => => extracting sha256:6239e464c1ab2cca0154db8e88c6b2eb8969c76dd4cdf8e67e03be54df84ac33                              0.0s
 => => extracting sha256:609722ad05b6850bc85fa5089312a3294fabfb20978d107d898d4f7804a9269e                              0.2s
 => [internal] load build context                                                                                      0.0s
 => => transferring context: 22.28kB                                                                                   0.0s
 => [2/5] WORKDIR /backend-flask                                                                                       0.2s
 => [3/5] COPY requirements.txt requirements.txt                                                                       0.1s
 => [4/5] RUN pip3 install -r requirements.txt                                                                         4.1s
 => [5/5] COPY . .                                                                                                     0.1s
 => exporting to image                                                                                                 0.3s
 => => exporting layers                                                                                                0.2s
 => => writing image sha256:d55d67eeb0e7e8948aed59edbc04398e9077d037185b19c279c9825a6c8e646e                           0.0s
 => => naming to docker.io/library/backend:1.0                                                                         0.0s

PS C:\Users\Kamran\Desktop\aws-bootcamp-cruddur-2023-main\backend-flask> docker images
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
backend      1.0       d55d67eeb0e7   2 minutes ago   129MB
```

```powershell
PS C:\Users\Kamran\Desktop\aws-bootcamp-cruddur-2023-main\backend-flask> docker tag d55d67eeb0e7 kamranabid/backend:1.0

PS C:\Users\Kamran\Desktop\aws-bootcamp-cruddur-2023-main\backend-flask> docker push kamranabid/backend:1.0
The push refers to repository [docker.io/kamranabid/backend]
8b1e69be378a: Pushed
500e763ff584: Pushed
9cc6d510d892: Pushed
4e54b15b37d9: Pushed
4358fe544125: Mounted from library/python
53b2529dfca9: Mounted from library/python
5be8f6899d42: Mounted from library/python
8d60832b730a: Mounted from library/python
63b3cf45ece8: Mounted from library/python
1.0: digest: sha256:bd9bd07c56f7ade14f2f2dd9eef3a9c6d0aaa6d4c8cba389a4d5097d23cc7aa9 size: 2203
PS C:\Users\Kamran\Desktop\aws-bootcamp-cruddur-2023-main\backend-flask>
```

![Untitled](Week%201%20-%20Homework%205f9dd9bb27024001beb920c889866117/Untitled.png)

![Untitled](Week%201%20-%20Homework%205f9dd9bb27024001beb920c889866117/Untitled%201.png)

# Use multi-stage building for a Dockerfile build

```powershell
Directory: C:\Users\Kamran\Desktop\Docker Tests

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---          25/02/2023    15:30            257 Dockerfile
-a---          25/02/2023    15:04              7 requirements.txt

PS C:\Users\Kamran\Desktop\Docker Tests> docker build -t multistage .
[+] Building 16.3s (16/16) FINISHED
 => [internal] load build definition from Dockerfile                                                                   0.0s
 => => transferring dockerfile: 296B                                                                                   0.0s
 => [internal] load .dockerignore                                                                                      0.0s
 => => transferring context: 2B                                                                                        0.0s
 => [internal] load metadata for docker.io/library/alpine:latest                                                       2.0s
 => [internal] load metadata for docker.io/library/python:3.9-alpine                                                   2.0s
 => [auth] library/alpine:pull token for registry-1.docker.io                                                          0.0s
 => [auth] library/python:pull token for registry-1.docker.io                                                          0.0s
 => [internal] load build context                                                                                      0.0s
 => => transferring context: 348B                                                                                      0.0s
 => [builder 1/4] FROM docker.io/library/python:3.9-alpine@sha256:a02fee195c815e1a1038513af6be324a4e401667bb10eb1dfdb  7.0s
 => => resolve docker.io/library/python:3.9-alpine@sha256:a02fee195c815e1a1038513af6be324a4e401667bb10eb1dfdbbeda2d78  0.1s
 => => sha256:781eddb6f34207e2b80d9ac0c81f1edde119e3ed0628aa9d4eeb6f8c01669b14 622.90kB / 622.90kB                     0.3s
 => => sha256:79794a61759890aeafd2857b0dfde9ac1451c96a569c21a1bac00ca37f5c43a0 11.55MB / 11.55MB                       1.6s
 => => sha256:586214a07410b26960d23432ac8929422f9671c27f226b9ec9f36a99f7357c35 229B / 229B                             0.5s
 => => sha256:a02fee195c815e1a1038513af6be324a4e401667bb10eb1dfdbbeda2d780748c 1.65kB / 1.65kB                         0.0s
 => => sha256:3d77aa146a90c04e7435f858a91f3664ad19ed0ebed6c63bb3e6191f08cacf31 1.37kB / 1.37kB                         0.0s
 => => sha256:dabd8d0fa98dfab821aca674ac2b3edf455e66d0d5588562416f2240df4db178 7.31kB / 7.31kB                         0.0s
 => => extracting sha256:781eddb6f34207e2b80d9ac0c81f1edde119e3ed0628aa9d4eeb6f8c01669b14                              0.4s
 => => sha256:44e0fa32783adf54185fcf4f38eba19e0e38693c1d8aff843dc68091a19d6f00 2.88MB / 2.88MB                         6.5s
 => => extracting sha256:79794a61759890aeafd2857b0dfde9ac1451c96a569c21a1bac00ca37f5c43a0                              0.4s
 => => extracting sha256:586214a07410b26960d23432ac8929422f9671c27f226b9ec9f36a99f7357c35                              0.0s
 => => extracting sha256:44e0fa32783adf54185fcf4f38eba19e0e38693c1d8aff843dc68091a19d6f00                              0.3s
 => [stage-1 1/4] FROM docker.io/library/alpine@sha256:69665d02cb32192e52e07644d76bc6f25abeb5410edc1c7a81a10ba3f0efb9  0.1s
 => => resolve docker.io/library/alpine@sha256:69665d02cb32192e52e07644d76bc6f25abeb5410edc1c7a81a10ba3f0efb90a        0.1s
 => => sha256:69665d02cb32192e52e07644d76bc6f25abeb5410edc1c7a81a10ba3f0efb90a 1.64kB / 1.64kB                         0.0s
 => => sha256:e2e16842c9b54d985bf1ef9242a313f36b856181f188de21313820e177002501 528B / 528B                             0.0s
 => => sha256:b2aa39c304c27b96c1fef0c06bee651ac9241d49c4fe34381cab8453f9a89c7d 1.47kB / 1.47kB                         0.0s
 => [builder 2/4] WORKDIR /app                                                                                         0.2s
 => [builder 3/4] COPY requirements.txt .                                                                              0.1s
 => [builder 4/4] RUN pip3 install -r requirements.txt                                                                 6.5s
 => [stage-1 2/4] COPY --from=builder /usr/local/bin/python /usr/local/bin/python                                      0.1s
 => [stage-1 3/4] WORKDIR /app                                                                                         0.1s
 => [stage-1 4/4] COPY . .                                                                                             0.1s
 => exporting to image                                                                                                 0.1s
 => => exporting layers                                                                                                0.1s
 => => writing image sha256:7bd6e6c081a4216862e6a6b2088f8db8c0c7e825364c74ca208d432fb3f72379                           0.0s
 => => naming to docker.io/library/multistage                                                                          0.0s
```

![Untitled](Week%201%20-%20Homework%205f9dd9bb27024001beb920c889866117/Untitled%202.png)

```powershell
PS C:\Users\Kamran\Desktop\Docker Tests> cat .\Dockerfile
# First stage: build python binary and install dependencies
FROM python:3.9-alpine as builder
WORKDIR /test
COPY . .
RUN pip3 install -r requirements.txt

# Second stage: copy virtual environment from first stage
FROM alpine:3.14
COPY --from=builder /usr/local /usr/local
WORKDIR /test
COPY . .
CMD ["python", "-m", "http.server", "--bind", "0.0.0.0", "80"]
PS C:\Users\Kamran\Desktop\Docker Tests> cat .\requirements.txt
flask
PS C:\Users\Kamran\Desktop\Docker Tests> cat .\app.py
print("hello world")
PS C:\Users\Kamran\Desktop\Docker Tests>
```

# Installing docker locally and running the docker images

I have my files on my local machine and have docker already installed 

```powershell
PS C:\Users\Kamran\Desktop\aws-bootcamp-cruddur-2023-main> ls

    Directory: C:\Users\Kamran\Desktop\aws-bootcamp-cruddur-2023-main

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          25/02/2023    14:15                _docs
d----          25/02/2023    14:15                aws
d----          25/02/2023    14:15                backend-flask
d----          25/02/2023    14:15                docker
d----          25/02/2023    14:15                frontend-react-js
d----          25/02/2023    14:15                journal
-a---          25/02/2023    14:15            754 .gitpod.yml
-a---          25/02/2023    14:15           1524 docker-compose.yml
-a---          25/02/2023    14:15            953 README.md
```

I will execute the docker compose command to build the images locally like I would do in GitPod.

```powershell
PS C:\Users\Kamran\Desktop\aws-bootcamp-cruddur-2023-main> docker compose -f ./docker-compose.yml up -d --build
[+] Running 14/14
 - db Pulled                                                                                                                                          40.2s
   - 63b65145d645 Pull complete                                                                                                                       18.6s
   - c441836541d9 Pull complete                                                                                                                       18.7s
   - d49de1a24361 Pull complete                                                                                                                       19.1s
   - 6c609d08dc3c Pull complete                                                                                                                       38.0s
### TRUNCATED
```

```powershell
PS C:\Users\Kamran\Desktop\aws-bootcamp-cruddur-2023-main> docker ps -a
CONTAINER ID   IMAGE                                              COMMAND                  CREATED          STATUS          PORTS                    NAMES
072709dcc29f   aws-bootcamp-cruddur-2023-main-backend-flask       "python3 -m flask ru…"   3 minutes ago    Up 3 minutes    0.0.0.0:4567->4567/tcp   aws-bootcamp-cruddur-2023-main-backend-flask-1
a1b5d54c580d   aws-bootcamp-cruddur-2023-main-frontend-react-js   "docker-entrypoint.s…"   3 minutes ago    Up 3 minutes    0.0.0.0:3000->3000/tcp   aws-bootcamp-cruddur-2023-main-frontend-react-js-1
c534ae89e1ad   amazon/dynamodb-local:latest                       "java -jar DynamoDBL…"   20 minutes ago   Up 20 minutes   0.0.0.0:8000->8000/tcp   dynamodb-local
6171ea60a647   postgres:13-alpine                                 "docker-entrypoint.s…"   20 minutes ago   Up 20 minutes   0.0.0.0:5432->5432/tcp   aws-bootcamp-cruddur-2023-main-db-1

```

![Untitled](Week%201%20-%20Homework%205f9dd9bb27024001beb920c889866117/Untitled%203.png)

# Implementing health check

I added a simple healthcheck to my frontend Docker container to ensure that the image is functioning correctly. This will provide peace of mind knowing that the image is up and running as expected.

Code snippet form docker compose 

```powershell
frontend-react-js:
    environment:
      REACT_APP_BACKEND_URL: "https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
    build: ./frontend-react-js
    ports:
      - "3000:3000"
    volumes:
      - ./frontend-react-js:/frontend-react-js
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 10s
```

`docker ps` → Shows it is healthy

```powershell
CONTAINER ID   IMAGE                                         COMMAND                  CREATED          STATUS                    PORTS                                       NAMES
4ff7054ddf86   aws-bootcamp-cruddur-2023-frontend-react-js   "docker-entrypoint.s…"   36 seconds ago   Up 34 seconds (healthy)   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp   aws-bootcamp-cruddur-2023-frontend-react-js-1
959e6385b728   aws-bootcamp-cruddur-2023-backend-flask       "python3 -m flask ru…"   36 seconds ago   Up 34 seconds             0.0.0.0:4567->4567/tcp, :::4567->4567/tcp   aws-bootcamp-cruddur-2023-backend-flask-1
c6891b972b6e   postgres:13-alpine                            "docker-entrypoint.s…"   36 seconds ago   Up 34 seconds             0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   aws-bootcamp-cruddur-2023-db-1
5bfa22d61812   amazon/dynamodb-local:latest                  "java -jar DynamoDBL…"   36 seconds ago   Up 34 seconds             0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   dynamodb-local
```

`docker inspect <id>` → Shows it is healthy 

```powershell
gitpod /workspace/aws-bootcamp-cruddur-2023/frontend-react-js (main) $ docker inspect 4ff7054ddf86
[
    {
        "Id": "4ff7054ddf869ddac1995b91d1b7eedb04d563d599f28392ca285958c48c2d5c",
        "Created": "2023-02-25T16:12:12.742728322Z",
        "Path": "docker-entrypoint.sh",
        "Args": [
            "npm",
            "start"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 2816,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-02-25T16:12:13.688684838Z",
            "FinishedAt": "0001-01-01T00:00:00Z",
            "Health": {
                "Status": "healthy",
```

# Launch EC2, install docker and pull a container

![Untitled](Week%201%20-%20Homework%205f9dd9bb27024001beb920c889866117/Untitled%204.png)

![Untitled](Week%201%20-%20Homework%205f9dd9bb27024001beb920c889866117/Untitled%205.png)

# Make docker file conform to best practices

Here is a list of some of the best practices I’ve found through my research. 

| Best Practice | Explanation |
| --- | --- |
| Use .dockerignore | Exclude unnecessary files from the Docker image. |
| Multi-stage builds | Build the image in stages to reduce size. |
| Keep images updated | Use the latest security patches and bug fixes. |
| Limit image layers | Fewer layers make the image smaller and faster to transfer. |
| Specify WORKDIR | Organize the file system and run commands easily. |
| Use environment variables | Easily manage different environments without rebuilding the image. |
| Keep packages minimal | Only include necessary packages to reduce image size and manage dependencies. |
| Use non-root user | Improve security by limiting application permissions. |

I will be using my previous multi stage docker file as the target of changes. 

```powershell
FROM python:3.9-alpine as builder
WORKDIR /app

# Only copy the exact file we need to avoid storing unnessary files 
COPY requirements .

# Install dependencies with --no-cache-dir to avoid storing unnecessary files
RUN pip install --no-cache-dir -r requirements.txt

FROM alpine:3.14
# Copy only the installed packages from the builder stage
COPY --from=builder /usr/local /usr/local
WORKDIR /app
COPY . .
CMD ["python", "-m", "http.server", "--bind", "0.0.0.0", "80"]
HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost/ || exit 1
```

- Removed step to install requirements (was not needed and increased complexity for no rason)
- Changes the workdirectory to `/app` allowing us to keep the file systme organised
- Changed the Python command to allow for the binding to all avaialble IP addresses
- Implementing health check to identify when docker container is unhealthy

**********Note:********** Installing requirements is not needed but I included it to make it simulate what an actual docker file may look like if the python script being executed if it actually had requirements and was not just a default library that came with python.