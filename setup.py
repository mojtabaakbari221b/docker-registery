#!/usr/bin/env python3

import os
from getpass import getpass


def get_domain():
    domain = None

    while not domain :
        domain = input("Enter domain name: ")
    
    return domain

def create_nginx_conf_and_copy_to_nginx_confd_folder(domain):
    with open('nginx.conf', 'r') as nginx_conf :
        data = nginx_conf.read()
        data = data.replace('$ENTER_YOUR_DOMAIN', domain)

        with open('nginx.conf.tmp', 'w') as tmp_nginx_file :
            tmp_nginx_file.write(data)
        
        os.system(f'sudo cp nginx.conf.tmp /etc/nginx/conf.d/{domain}.conf')
        os.system(f'rm nginx.conf.tmp')
        os.system(f'sudo systemctl reload nginx')

def get_docker_registry_username_and_password():
    return input("Enter docker registry username: "), getpass()

def create_auth_password(username, password):
    os.system('mkdir -p auth')
    os.system(f'htpasswd -bBc auth/registry.password {username} {password}')


if __name__ == "__main__" :
    domain = get_domain()
    create_nginx_conf_and_copy_to_nginx_confd_folder(domain)

    username, password = get_docker_registry_username_and_password()
    create_auth_password(username, password)