# Collection Stack for IOSXE and IOSXR Devices


### Install
Installs Docker, Docker-compose and in containers grafana, influxdb and telegraf with initial configurations

1. [Install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
    Make sure ansible can be run as the local user (not as root/sudo)
2. clone this repo - `git clone https://github.com/beano38/mdt-demo.git`
3. get into repo directory - `cd mdt-demo`
4. Install Requirements `ansible-galaxy install -r requirements.yml`
5. Run Playbook `ansible-playbook playbooks/local_install.yml`

After the install, there is a note to log out and back in to set the new environment variables and run docker compose to bring up the containers.
```
cd ~/docker
docker-compose up -d
```

Alternatively, you may install docker and docker-compose yourself and just run the docker-compose file.  `~/docker/docker-compose up -d`
