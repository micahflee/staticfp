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
