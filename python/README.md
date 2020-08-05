## SNMP-Poller
Simple Python based SNMP-Poller HTTP server with API

clone this repo - `git clone https://github.com/beano38/mdt-demo.git`


1. Build the Docker Container
```
cd mdt-demo/python
docker build -t snmp .
```
2. Check if it's there - `docker images`
3. Copy the sample config.yml file to ~/docker/snmp/config.yml and modify with your environment
4. Add to docker-compose file 
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
    extra_hosts:
      - "cbr8-lab:10.128.128.3"
    restart: always

```
5. Bring up new container - `docker-compose up -d`
6. Check log - `docker logs snmp -f`

