import docker

NAME = 'containerized-app'


if __name__ == '__main__':
    client = docker.from_env()
    print('Building image...')
    client.images.build(path='.', tag=NAME)
    print('Creating container...')
    client.containers.create(NAME, detach=True, ports={5000:5000}, name=NAME)
