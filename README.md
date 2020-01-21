# Simple Site Generator

Static Site Generator created by Python

## Getting Started
### Prerequisites

* Python >= ver3.7.x

### Installing ###
Before installing, you need to setup Python and pip.

#### Setup enviroment on Ubuntu by Docker
##### Dockerfile

```
FROM ubuntu:18.04
RUN apt-get -y update
RUN apt-get -y install software-properties-common
RUN apt-get -y update
RUN apt-get -y install git docker vim
RUN apt-get -y install nginx
RUN apt-get -y install python3.6-dev
RUN apt-get -y install python3-pip
COPY default.conf /etc/nginx/conf.d/default.conf
CMD ["nginx"]
```

##### run.sh

```bash
docker build -t ubuntu_site_generater .
docker stop ubuntu_site_generater_con
docker rm ubuntu_site_generater_con
docker run -p 8080:80 -v -it --name ubuntu_site_generater_con ubuntu_site_generater:latest /bin/bash
```

##### default.conf (for nginx)

```
server {
  listen 80;
  server_name localhost;
  server_tokens off;
  location / {
    root /var/www/simple-site-generator/public;
  }
}
```

Execute run.sh

#### checkout this project on Ubuntu container
After you go into container, move to web dir and chekout this project.

```bash
cd /var/www
git clone git@github.com:uzura8/simple-site-generator.git
cd simple-site-generator
```

#### Install required libraries

```bash
pip3 install -r requirements.txt
```

### Edit config ###

Edit configs for your site by yaml format, after copy from sample.

```bash
cp config.yml.sample config.yml
cp content/en.yml.sample content/en.yml
cp content/ja.yml.sample content/ja.yml
vi config.yml content/en.yml content/ja.yml
```

### Generate! ###
After execute below command, index.html generated under public dir.

```bash
python builder.py
```

And you upload to public space
