# Create Docker container for Python Environment

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
 - Do not forget to ```start Docker Desktop``` before get started coding and ```exit/quit Docker Desktop``` after you have done the project.
2. Create Project folder
3. Create files
 - project structure
    ```
    +-- your-project-folder
    |    +-- .dockerignore
    |    +-- Dockerfile
    |    +-- docker-compose.yml
    ```

    .dockerignore
    ```
    .vscode-server
    ```

    Dockerfile
    ```Dockerfile
    FROM python:3.10.4-buster
    WORKDIR /root/src

    RUN pip install "numpy==1.22.3"
    RUN pip install "pandas==1.4.2"
    RUN pip install "matplotlib==3.5.1"
    RUN pip install "ipykernel==6.13.0"

    CMD tail -f /dev/null
    ```

    docker-compose.yml
    ```yml
    version: "3.8"
    services:
    app:
        build: 
        context: .
        volumes:
            - ./src:/root/src
            - ./.vscode-server:/root/.vscode-server
    ```

4. Start Docker container (Python Environment)

```sh
docker-compose up --build -d
```
```
+-- your-project-folder
|    +-- .vscode-server
|    +-- src
|    +-- .dockerignore
|    +-- Dockerfile
|    +-- docker-compose.yml
```

5. Use [VSCode Remote - Containers](https://code.visualstudio.com/docs/remote/containers) and select ```/root/src``` for your code and other files.

6. After finished the project, please remove the container.

```sh
docker-compose down
```

PS. Do not forget to ```exit/quit Docker Desktop```.
