## Docker Registry

### Requirements

you should install **nginx**, and **htpasswd** package for serve docker registry and create bcrypted password.

if you wanna install automatically, run install_requirements.py script.

### Installation

1. for setup docker registry on your machine or server, after clone from repo, run setup script:
```python
python3 setup.py
```

* enter your docker registry domain, if you are in local, enter localhost, else enter your valid domain name.
* enter your password if required for copy nginx file to nginx conf.d folder.
* enter your username and password for docker registry, script use this for set on docker registry, it is used in push and pull from docker private registry, don't forgot it.
* enter your username and password for docker registry ui, script use this for set on docker registry ui, it is used in login to registry ui.
* enter your docker registry ui domain, if you are in local, enter localhost, else enter your valid domain name.

2. up docker containers:
```
docker-compose up --build -d
```

### Add another user to docker registry
run add_user_to_registry.py and enter new username and password.

### lts for domain
you can set lts with cerbot:
```
sudo certbot --nginx
```

## Publishing to Your Private Docker Registry
Now that your Docker Registry server is up and running, and accepting large file sizes, you can try pushing an image to it.

The new image is now available locally, and you’ll push it to your new container registry. First, you have to log in:
```
docker login https://your_domain
```
When prompted, enter in a username and password combination that you’ve defined in setup script.

The output will be: **Login Succeeded**.

Once you’re logged in, rename the created image:
```
docker tag test-image your_domain/test-image
```

Finally, push the newly tagged image to your registry:
```
docker push your_domain/test-image
```

## Pulling From Your Private Docker Registry
Now that you’ve pushed an image to your private registry, you’ll try pulling from it.

On the main server, log in with the username and password you set up previously:
```
docker login https://your_domain
```

Try pulling the test-image by running:
```
docker pull your_domain/test-image
```


#### Link:
you can custom your setup with this link: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-docker-registry-on-ubuntu-20-04