# staticfp

Fingerprint the exact version of web apps based on their static resources. (Starting with OwnCloud.)

Set up the virtualenv:

```sh
$ virtualenv-3 env/
$ . env/bin/activate
(env) $ pip install -r requirements.txt
```

Create the owncloud data (this takes a long time, uses a lot of disk space):

```sh
(env) $ ./script/build_owncloud_data.py
```

How to use:

```sh
(env) $ ./staticfp -h
usage: staticfp [-h] [--user-agent user_agent] [--no-verify-ssl] webapp url

positional arguments:
  webapp                web app software being targeted (e.g. 'owncloud')
  url                   URL of the web app

optional arguments:
  -h, --help            show this help message and exit
  --user-agent user_agent
                        user agent string (default is Firefox in Windows)
  --no-verify-ssl       don't verify SSL certificate
```
