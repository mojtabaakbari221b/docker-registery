## Docker Registry

### Requirements

you should install **nginx**, and **htpasswd** package for serve docker registry and create bcrypted password.

### Installation

for setup docker registry on your machine or server, after clone from repo, run setup script:
```python
python3 setup.py
```

* enter your domain, if you are in local, enter localhost, else enter your valid domain name.
* enter your password if required for copy nginx file to nginx conf.d folder.
* enter your username and password for docker registry, script use this for set on docker registry, it is used in push and pull from docker private registry, don't forgot it.

#### Link:
you can custom your setup with this link: https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-docker-registry-on-ubuntu-20-04