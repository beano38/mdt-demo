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

## SNMP-Poller
Simple Python based SNMP-Poller HTTP server with API

1. Build the Docker Container
```
cd mdt-demo/python
nano config.yml (modify the config for your environment)
docker build -t snmp .
```
2. Check if it's there - `docker images`
3. Add to docker-compose file 
```
nano ~/docker/docker-compose.yml

add this to end of file:


  snmp:
    image: snmp
    container_name: snmp
    ports:
      - 9998:9998
    volumes:
      - ${DOCKERDIR}/snmp-poller/config.yml:/usr/bin/app/config.yml
    restart: always

```
4. Bring up new container - `docker-compose up -d`
5. Check log - `docker logs snmp -f`

