# 🚀 Docker Quick Start Guide

A simplified reference for getting started with Docker: from installation, pulling images, running containers, and publishing to Docker Hub.

---

## 📥 Installation

Install Docker from the official site:  
👉 [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

Verify installation:

```bash
docker --version
docker info
```

---

## 📦 Pulling and Managing Docker Images

```bash
docker pull <image_name>       # Download image from Docker Hub
docker images                  # List all downloaded images
```

Example:

```bash
docker pull hello-world
```

---

## 🏃 Running Containers

```bash
docker run <image_name>        # Runs a new container
docker run -it <image_name>    # Runs interactively
```

> Each run creates a new container with a random ID and name.

---

## 📋 Viewing Containers

```bash
docker ps                      # Show running containers
docker ps -a                   # Show all containers (running + stopped)
```

---

## 🧱 Container Management

```bash
docker start <container_id|name>     # Start a container
docker stop <container_id|name>      # Stop a container
docker rename old_name new_name      # Rename a container
docker rm <container_id|name>        # Remove a stopped container
docker container prune               # Remove all stopped containers
```

---

## 🔄 Running Commands in Containers

```bash
docker exec -it <container_id|name> <command>  # Run command inside container
docker exec -it my_container node              # Start Node.js shell
docker exec -it my_container /bin/bash         # Access Linux shell
```

---

## 📁 Copying Files

### From Host to Container

```bash
docker cp ./example.txt <container_name>:/example.txt
```

### From Container to Host

```bash
docker cp <container_name>:/example.txt ./copied.txt
```

> Use `cat <filename>` inside the container to view file contents.

---

## 📄 Building Docker Images

### Dockerfile Example:

```Dockerfile
FROM alpine:latest
CMD ["echo", "Hello, Docker"]
```

### Build Image

```bash
docker build -t my_custom_image .
```

---

## 🗃️ Docker Volumes (Data Persistence)

```bash
docker volume create my_volume
docker run -v my_volume:/data alpine
docker volume ls
```

> Volumes allow data to persist even after a container is deleted.

---

## 📦 Docker Compose (Multi-Container Apps)

Create a `docker-compose.yml` file:

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "80:80"
```

Start with:

```bash
docker-compose up
```

Stop with:

```bash
docker-compose down
```

---

## 🚫 Ignoring Files: `.dockerignore`

Create a `.dockerignore` file to exclude files/folders from the image:

```
node_modules
*.log
Dockerfile
```

---

## 📤 Docker Hub: Push Image

1. Login:

```bash
docker login
```

2. Tag the image:

```bash
docker tag my_image <username>/<repository>:latest
```

3. Push the image:

```bash
docker push <username>/<repository>:latest
```

4. Pull from anywhere:

```bash
docker pull <username>/<repository>:latest
```

---

## 🏢 Docker Registry

> A Docker registry is a system for storing and distributing Docker images.

- Docker Hub is the default public registry.
- Run your own private registry:

```bash
docker run -d -p 5000:5000 --name registry registry:2
```

---

## 🛡️ Best Practices

- Use lightweight base images (like `alpine`)
- Use multi-stage builds for production apps
- Clean up unused packages in Dockerfile
- Tag images clearly (e.g., `:v1`, `:latest`, `:prod`)
- Use `.dockerignore` to reduce image size and build time

---

## ✅ Useful Summary Commands

| Action                 | Command                             |
|------------------------|-------------------------------------|
| List Images            | `docker images`                     |
| Run Container          | `docker run <image>`                |
| List Containers        | `docker ps -a`                      |
| Build Image            | `docker build -t name .`            |
| Exec into Container    | `docker exec -it <id> bash`         |
| Copy Files             | `docker cp`                         |
| Push to Docker Hub     | `docker push`                       |

---
