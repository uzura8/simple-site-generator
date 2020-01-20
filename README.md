# Simple Site Generator

Static Site Generator created by Python

## Getting Started
### Prerequisites

* Python >= ver3.7.x

### Installing ###
Before installing, you need to setup Python and pip.

#### Install required libraries

```bash
pip install -r requirements.txt
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
