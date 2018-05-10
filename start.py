import docker
from build import NAME


if __name__ == '__main__':
    client = docker.from_env()
    print('Starting container...')
    client.containers.get(NAME).start()
