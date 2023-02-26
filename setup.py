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
        os.system(f'sudo systemctl restart nginx')

def get_docker_registry_username_and_password():
    return input("Enter docker registry username: "), getpass(prompt="Enter docker registry Password: ")

def create_auth_password(registry_username, registry_password):
    os.system('mkdir -p auth')
    os.system(f'htpasswd -bBc auth/registry.password {registry_username} {registry_password}')

def get_docker_registry_ui_username_and_password():
    return input("Enter docker registry ui username: "), getpass(prompt="Enter docker registry ui Password: ")

def create_registry_ui_env(registry_ui_username, registry_ui_password, registry_username, registry_password):
    with open('.env.sample', 'r') as env_sample_file :
        data = env_sample_file.read()
        data = data.replace(
            'RGY_UI_USERNAME',
            registry_ui_username,
        )
        data = data.replace(
            'RGY_UI_PASSWORD',
            registry_ui_password,
        )
        data = data.replace(
            'RGY_USERNAME',
            registry_username,
        )
        data = data.replace(
            'RGY_PASSWORD',
            registry_password,
        )

        with open('.env', 'w') as env_file :
            env_file.write(data)

def get_registeryui_domain():
    registeryui_domain = None

    while not registeryui_domain :
        registeryui_domain = input("Enter registery ui domain name: ")
    
    return registeryui_domain

def create_registeryui_nginx_conf_and_copy_to_nginx_confd_folder(registeryui_domain):
    with open('registry_ui.nginx.conf', 'r') as nginx_conf :
        data = nginx_conf.read()
        data = data.replace('$ENTER_YOUR_DOMAIN', registeryui_domain)

        with open('registry_ui.nginx.conf.tmp', 'w') as tmp_nginx_file :
            tmp_nginx_file.write(data)
        
        os.system(f'sudo cp registry_ui.nginx.conf.tmp /etc/nginx/conf.d/{registeryui_domain}.conf')
        os.system(f'rm registry_ui.nginx.conf.tmp')
        os.system(f'sudo systemctl restart nginx')


if __name__ == "__main__" :
    domain = get_domain()
    create_nginx_conf_and_copy_to_nginx_confd_folder(domain)

    registry_username, registry_password = get_docker_registry_username_and_password()
    create_auth_password(
        registry_username,
        registry_password,
    )

    registry_ui_username, registry_ui_password = get_docker_registry_ui_username_and_password()
    create_registry_ui_env(
        registry_ui_username, 
        registry_ui_password,
        registry_username,
        registry_password,
    )

    registeryui_domain = get_registeryui_domain()
    create_registeryui_nginx_conf_and_copy_to_nginx_confd_folder(registeryui_domain)
