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

1. Open Safari
2. Access to https://dev-heim.jp
3. Click "See this website" in the certificate warning, and then Keychain window will open
4. Double-click installed "dev-heim.jp" certificate
5. Open "Trust > When use this certificate" field and Change "Custom" => "Always Trust"

#### Mac OS < 10.15 (Before Mojave)

```bash
$ cd heim-front

$ sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain nginx/ssl/certs/ca.crt
```

### Configure /etc/hosts

To enable to access via `dev-heim.jp`, `api.dev-heim.jp`, edit `/etc/hosts`.

There are 2 methods to edit.

- (a) Install `Gas Mask`.
  - https://github.com/2ndalpha/gasmask#download

- (b) Directly edit `/etc/hosts` via text editor like `vim`.
```bash
$ sudo vim /etc/hosts
```

And then, add `dev-heim.jp`, `api.dev-heim.jp` to the tail of `127.0.0.1` line.

`/etc/hosts`

```conf
127.0.0.1   localhost dev-heim.jp api.dev-heim.jp
```

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

Go to https://dev-heim.jp

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

### Install Vue.js devtools
Install [Vue.js devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd).

### When you want to use Rails Console
Run it on docker.

```bash
$ docker-compose exec web bundle exec rails c
```

### When update DB schema (migration)
```bash
### Dry-run
$ docker-compose exec web bundle exec ridgepole -c config/database.yml -f db/Schemafile.rb -s heim -a --dry-run

### Execute
$ docker-compose exec web bundle exec ridgepole -c config/database.yml -f db/Schemafile.rb -s heim -a
```

### When JS libraries updated

If JS libraries updated, we recommend to install those libraries on your local for editor.

```bash
$ yarn install
```

Please refer to [this doc](https://github.com/crispy-inc/heim-front/blob/develop/docs/operations_on_production.md#how-to-connect-to-cloudsql-from-your-local-environment) when you want to migrate DB on staging or production.

## Install MySQL GUI tool
We recommend to use GUI tools to operate to MySQL.

- [SequelPro](https://sequelpro.com/test-builds) ... Free
- [TablePlus](https://tableplus.io/) ... Free (upto 2 tabs), can connect to Redis, too.

## When you want to restart Rails server (e.g. When reload new config files)

```bash
$ docker-compose exec web touch tmp/restart.txt
```

or

```bash
$ docker-compose exec web rake restart
```

## When your PC volume has no space
**[CAUTION]** The following command will **delete all containers**.
You need to re-build those containers.

```bash
### Delete old containers only
$ docker container prune

### Delete volumes only
$ docker volume prune

### Delete volumes + stoppted containers
$ docker system prune

### Delete completely
$ docker system prune -a
```

## How to debug with binding.pry
To use `binding.pry` to debug, need attaching to running container.
Open another console and attach the container.

```
$ ./docker_attach.sh
```

## Branches and merge PR policies


### Branch types
We have these branche types.
- `master`: Corresponding to production environment
- `develop`: Default, corresponding to stating environment
- `feature`: Name is optional, create this branch for development and send PR to `develop`
- `hotfix`: Name is optional, create this branch to deploy urgent fix for production, send PR to `master`, and merge to `develop` after the deployment

Branch name should be **kebab case (e.g.: add-some-feature)** with lower case.

### Merge PR policies
We have policies for merge PRs on GitHub.

- `master` <= `develop`: `Create a merge commit`
- `master` <= `hotfix`: `Create a merge commit`
- `develop` <= `feature`: `Squash and merge`

Please refer to [this article](https://qiita.com/ko-he-8/items/94e872f2154829c868df) about merge policies.

## Other documents

See [docs/](https://github.com/crispy-inc/heim-front/blob/develop/docs).
