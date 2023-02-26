## Docker Registry

### Requirements

you should install **nginx**, and **htpasswd** package for serve docker registry and create bcrypted password.

if you wanna install automatically, run install_requirements.py script.

### Installation

1. for setup docker registry on your machine or server, after clone from repo, run setup script:
```python
python3 setup.py
```

* enter your domain, if you are in local, enter localhost, else enter your valid domain name.
* enter your password if required for copy nginx file to nginx conf.d folder.
* enter your username and password for docker registry, script use this for set on docker registry, it is used in push and pull from docker private registry, don't forgot it.

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


#### Link:
you can custom your setup with this link: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-docker-registry-on-ubuntu-20-04