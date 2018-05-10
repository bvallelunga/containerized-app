import docker
from build import NAME


if __name__ == '__main__':
    print('Stopping container...')
    client = docker.from_env()
    client.containers.get(NAME).stop()
