# fetch-tweets



## Setup
### Prerequisites
- Download latest **[Docker](https://store.docker.com/editions/community/docker-ce-desktop-mac)**. (Need an account to download)
- rbenv
- yarn

```bash
$ brew install rbenv yarn
$ rbenv install $(cat .ruby-version)
```


### Install GCloud SDK

```bash
$ curl https://sdk.cloud.google.com | bash
$ exec -l $SHELL
$ gcloud init --account YOUR_EMAIL_ADDRESS --project stg-heim --configuration stg-heim
$ gcloud auth login
```

### Build Docker Containers in your local environment

```bash
$ ./switch-dockerfile.sh local

$ gcloud auth configure-docker
$ gcloud docker -- pull asia.gcr.io/stg-heim/ruby-base-docker-image


### Create a common network on Docker
```bash
$ docker network create common_link
```

### DB setup
We use [`ridgepole`](https://github.com/winebarrel/ridgepole) to migrate DB instead of Rails' default migrations.

Run on docker.

We don't have critical personal information for now, so recommend to **import production data**, not use seeds.

See [Import production data](#import-production-data).

### Import production data
To import production data, run the following shell.
Select **[1] heim\_production**

```bash
$ docker-compose exec web ./tools/import_production_data_to_local_db.sh
```

### Put a master key

```bash
$ gcloud config configurations activate stg-heim
$ gsutil cp gs://stg-heim-config-files/heim-front/config/secrets.yml.key config/secrets.yml.key
```

### Install self-signed certificate

To enable HTTPS on local, install certificate.

#### Mac OS 10.15+ (Catalina)


### Run containers

We currently have 6 containers.


```bash
### Start all containers
$ docker-compose up

...
web_1     | Puma starting in single mode...
web_1     | * Version 3.12.1 (ruby 2.6.1-p33), codename: Llamas in Pajamas
web_1     | * Min threads: 5, max threads: 5
web_1     | * Environment: development
web_1     | * Listening on tcp://0.0.0.0:3000
web_1     | Use Ctrl-C to stop
```


### Stop all containers
Press **Ctrl + C** and **wait a few seconds**.

```bash
### Stop all containers
Gracefully stopping... (press Ctrl+C again to force)
Stopping heimfront_web_1 ... done
Stopping heimfront_mail_1 ... done
Stopping heimfront_db_1 ... done
```

### Install linters

```bash
### Install ruby linters (To global for your editor)
$ ./tools/install_linter_gems.sh

### Install JS linters (To global for your editor)
$ ./tools/install_linter_node_modules.sh

### Install pip linters (To global for your editor)
$ ./tools/install_linter_pips.sh
```
