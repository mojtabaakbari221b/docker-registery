#!/usr/bin/env python3

import os
from getpass import getpass


def get_docker_registry_username_and_password():
    return input("Enter docker registry new username: "), getpass()

def create_auth_password(username, password):
    os.system('mkdir -p auth')
    os.system(f'htpasswd -bB auth/registry.password {username} {password}')

def rebuild_docker_container():
    os.system('docker-compose up --build -d')

if __name__ == "__main__" :
    username, password = get_docker_registry_username_and_password()
    create_auth_password(username, password)
    rebuild_docker_container()