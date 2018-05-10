# Example Containerized App

## Prerequisites
  1. [Install](https://www.docker.com/get-docker) and open the
`docker app` on your machine.
  2. [Install](https://git-lfs.github.com/) `git lfs` and clone this
  repo.
  3. Install the `docker python sdk`:
``` bash
pip3 install docker
```
  4. `cd` into the repo.

## Getting Started
First, build the `docker image` and create a `docker container`
from that image:
``` bash
python build.py
```

Once we have a container, we can start it up with:
``` bash
python start.py
```

We can then send data to the model, running inside the container, through `POST` requests:
``` bash
sh post.sh
```

When we are done with the container, we can stop it with:
``` bash
python stop.py
```

## Production Setting
In a production setting, the flow would be as follows:
  1. An app is approved for the marketplace
  2. A `docker image` is automatically created for the app and uploaded
  to our image registry (public or private)
  3. A provider machine would then enroll in the app
    * i.e. the `dvm-cli` will create a `docker container` locally using
    the `docker image` found in our registry
  4. The provider would then start providing
    * i.e. the `docker container` will start allowing it to process
    prediction requests
