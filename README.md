# Automotive Service Log

Python app using TinyDB for storage and Flask for CRUD.

ToDo:

- [x] CRUD with TinyDB
- [x] Display on Flask/Jinja template
- [x] Add formatting/CSS to template
- [x] Add favicon and meta to template
- [x] Create entry in TinyDB from template
- [x] Delete entry from TinyDB from template
- [ ] Update entry in TinyDB from template
  - [x] Match on mileage, updates date, vehicle, notes
  - [ ] Able to update all fields

## Docker-Compose Setup

So that my Caddy config below makes a little more sense, I'm going to post all the relevant services from my `docker-compose.yml` file. However, only the `autolog` service is necessary for this setup. If you want the service to be available by itself, make sure to uncomment the `ports` lines. If used in a `docker-compose.yml` with the reverse_proxy service, then the ports are not needed since the services will both see each other.

**Docker folder structure**
```bash
~/docker
  |-- config/
  |    |-- caddy/
  |         |-- Caddyfile
  |         |-- www/
  |              |-- tools.domain.tld/
  |                   |-- web files
  |-- flask_autolog/
  |    |-- git sync'd repo
  |-- docker-compose.yml
```


**docker-compose.yml**
```bash
version: "3.3"
services:
  # flask ipcalc
  autolog:
    build: ./flask_autolog
    image: drowland/autolog:latest
    container_name: autolog
    restart: unless-stopped
#    ports:
#      - "8001:8001"
  # Web Host
  webhost:
    image: caddy
    container_name: webhost
    restart: unless-stopped
    volumes:
      - caddy_data:/data
      - caddy_config:/config
      - ./config/caddy/www:/srv
      - ./config/caddy/Caddyfile:/etc/caddy/Caddyfile
    ports:
      - "80:80"
      - "443:443"
  # Web Host PHP-FPM
  phpfpm:
    image: php:fpm-alpine
    container_name: phpfpm
    restart: unless-stopped
    volumes:
      - ./config/caddy/www:/srv

volumes:
  caddy_data:
    external: true
  caddy_config:
```

## Reverse Proxy Setup

I used this app with my Caddy Server configuration, as a suffix on an existing site.

```bash
tools.domain.tld {
    root * /srv/tools.domain.tld
    php_fastcgi * phpfpm:9000
    file_server

    route /autolog/* {
        reverse_proxy autolog:8001
    }
}
```