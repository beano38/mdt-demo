# Collection Stack for IOSXE and IOSXR Devices


### Install
Installs Docker, Docker-compose and in containers grafana, influxdb and telegraf with initial configurations

1. [Install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
2. Install Requirements 
`ansible-galaxy install -r requirements.yml`
3. Run Playbook
`ansible-playbook -i inventory.ini playbooks.main.yml`

Alternatively, you may install docker and docker-compsose yourself and just run the docker-compose file.  '~/docker/docker-compose up -d'
