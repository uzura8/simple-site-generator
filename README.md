# Simple Site Generator

Static Site Generator created by Python

### Prerequisites

* Python >= ver3.6.x



## Installing on local environment

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
python3 builder.py
nginx
```

You can access http://localhost:8080/





## Deliver from Google Cloud Strage 

### Preparation 

#### About Hosting Static WebSite on Google Cloud Strage

* Read docs: https://cloud.google.com/storage/docs/hosting-static-website
* You have to do below for preparation
    * Domain ownership verification
    * Register "c.storage.googleapis.com" to CNAME of your domain  
    * Create GCP Project

#### Domain ownership verification

* Access to Google Search Console( https://search.google.com/search-console )

* Register TXT your domain of DNS record

    + Refer to: https://support.google.com/webmasters/answer/9008080

          

#### Register "c.storage.googleapis.com" to CNAME of your domain

* Register "c.storage.googleapis.com" to CNAME of your domain 

* Refer to https://cloud.google.com/storage/docs/hosting-static-website#cname

      

#### Create GCP Project

* Refer to [GCP docs](https://cloud.google.com/resource-manager/docs/creating-managing-projects) to create project

* Make sure that billing is enabled for your Google Cloud project

    * Refer to https://cloud.google.com/billing/docs/how-to/modify-project

* Get gcp credential json file

    * Refer to https://cloud.google.com/iam/docs/creating-managing-service-account-keys

    

### Setup enviroment on Ubuntu by Docker

##### Dockerfile

```
RUN chsh -s /usr/bin/zsh
FROM ubuntu:18.04
USER root
RUN apt-get -y update
RUN apt-get -y install software-properties-common
RUN yes | add-apt-repository ppa:jonathonf/vim
RUN apt-get -y update
RUN apt-get -y install zsh
RUN chsh -s /usr/bin/zsh
RUN /usr/bin/zsh
RUN apt-get -y install git docker vim neovim
RUN apt-get -y install python3.6-dev
RUN apt-get -y install python3-pip
RUN pip install --upgrade pip
RUN apt-get -y update
RUN apt-get install wget
RUN apt-get -y install zip unzip
RUN apt-get install -y curl
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
    echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk -y

WORKDIR /root
```

##### run.sh

```bash
docker build -t ubuntu_sg .
docker stop ubuntu_sg_con
docker rm ubuntu_sg_con
docker run -v /Users/hogehoge/.config/gcloud:/root/.config/gcloud -it --name ubuntu_sg_con ubuntu_sg:latest /bin/bash
```

Execute run.sh, and move to Docker container



#### Checkout site-generater repository

Move to your work dir on Docker container, and chekout this.

````bash
# Below on Docker Container

mkdir ~/.ssh
vim ~/.ssh/id_rsa
# Put your key and save
chmod 600 ~/.ssh/id_rsa
cd /path-to-your-work-dir/
git clone git@github.com:************.git your-project-dir-name
cd your-project-dir-name
git checkout this-branch # if need
````

#### Install required libraries

```bash
pip3 install -r requirements.txt
```

#### Edit config

Edit configs for your site by yaml format, after copy from sample.

```bash
cp config.yml.sample config.yml
cp content/en.yml.sample content/en.yml
cp content/ja.yml.sample content/ja.yml
vi config.yml content/en.yml content/ja.yml
```

#### Generate!

After execute below command, index.html generated under public dir.

```bash
python3 builder.py
```

#### Upload to GCS

````
bash gcs_upload.sh your-domain.example.com
````

