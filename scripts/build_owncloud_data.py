#!/usr/bin/env python3
import sys
import os
import subprocess
from urllib.request import urlretrieve

CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cache')
MIRROR = 'https://ftp.icm.edu.pl/packages/owncloud'
ARCHIVE_FILENAMES = [
    'owncloud-4.0.13.tar.bz2', 'owncloud-4.0.14.tar.bz2', 'owncloud-4.0.15.tar.bz2', 'owncloud-4.0.16.tar.bz2',
    'owncloud-4.5.10.tar.bz2', 'owncloud-4.5.11.tar.bz2', 'owncloud-4.5.12.tar.bz2', 'owncloud-4.5.13.tar.bz2',
    'owncloud-4.5.8.tar.bz2', 'owncloud-4.5.9.tar.bz2', 'owncloud-5.0.0.tar.bz2', 'owncloud-5.0.10.tar.bz2',
    'owncloud-5.0.11.tar.bz2', 'owncloud-5.0.12.tar.bz2', 'owncloud-5.0.13.tar.bz2', 'owncloud-5.0.14a.tar.bz2',
    'owncloud-5.0.15.tar.bz2', 'owncloud-5.0.16.tar.bz2', 'owncloud-5.0.17.tar.bz2', 'owncloud-5.0.18.tar.bz2',
    'owncloud-5.0.19.tar.bz2', 'owncloud-5.0.1.tar.bz2', 'owncloud-5.0.2.tar.bz2', 'owncloud-5.0.3.tar.bz2',
    'owncloud-5.0.4.tar.bz2', 'owncloud-5.0.5.tar.bz2', 'owncloud-5.0.6.tar.bz2', 'owncloud-5.0.7.tar.bz2',
    'owncloud-5.0.8.tar.bz2', 'owncloud-5.0.9.tar.bz2', 'owncloud-6.0.0a.tar.bz2', 'owncloud-6.0.0.tar.bz2',
    'owncloud-6.0.1.tar.bz2', 'owncloud-6.0.2.tar.bz2', 'owncloud-6.0.3.tar.bz2', 'owncloud-6.0.4.tar.bz2',
    'owncloud-6.0.5.tar.bz2', 'owncloud-6.0.6.tar.bz2', 'owncloud-6.0.7.tar.bz2', 'owncloud-6.0.8.tar.bz2',
    'owncloud-6.0.9.tar.bz2', 'owncloud-7.0.0.tar.bz2', 'owncloud-7.0.10.tar.bz2', 'owncloud-7.0.11.tar.bz2',
    'owncloud-7.0.12.tar.bz2', 'owncloud-7.0.13.tar.bz2', 'owncloud-7.0.15.tar.bz2', 'owncloud-7.0.1.tar.bz2',
    'owncloud-7.0.2.tar.bz2', 'owncloud-7.0.3.tar.bz2', 'owncloud-7.0.4.tar.bz2', 'owncloud-7.0.5.tar.bz2',
    'owncloud-7.0.6.tar.bz2', 'owncloud-7.0.7.tar.bz2', 'owncloud-7.0.8.tar.bz2', 'owncloud-7.0.9.tar.bz2',
    'owncloud-8.0.0.tar.bz2', 'owncloud-8.0.10.tar.bz2', 'owncloud-8.0.11.tar.bz2', 'owncloud-8.0.12.tar.bz2',
    'owncloud-8.0.13.tar.bz2', 'owncloud-8.0.14.tar.bz2', 'owncloud-8.0.15.tar.bz2', 'owncloud-8.0.16.tar.bz2',
    'owncloud-8.0.1.tar.bz2', 'owncloud-8.0.2.tar.bz2', 'owncloud-8.0.3.tar.bz2', 'owncloud-8.0.4.tar.bz2',
    'owncloud-8.0.5.tar.bz2', 'owncloud-8.0.6.tar.bz2', 'owncloud-8.0.7.tar.bz2', 'owncloud-8.0.8.tar.bz2',
    'owncloud-8.0.9.tar.bz2', 'owncloud-8.1.0.tar.bz2', 'owncloud-8.1.10.tar.bz2', 'owncloud-8.1.11.tar.bz2',
    'owncloud-8.1.12.tar.bz2', 'owncloud-8.1.1.tar.bz2', 'owncloud-8.1.2.tar.bz2', 'owncloud-8.1.3.tar.bz2',
    'owncloud-8.1.4.tar.bz2', 'owncloud-8.1.5.tar.bz2', 'owncloud-8.1.6.tar.bz2', 'owncloud-8.1.7.tar.bz2',
    'owncloud-8.1.8.tar.bz2', 'owncloud-8.1.9.tar.bz2', 'owncloud-8.2.0.tar.bz2', 'owncloud-8.2.10.tar.bz2',
    'owncloud-8.2.11.tar.bz2', 'owncloud-8.2.1.tar.bz2', 'owncloud-8.2.2.tar.bz2', 'owncloud-8.2.3.tar.bz2',
    'owncloud-8.2.4.tar.bz2', 'owncloud-8.2.5.tar.bz2', 'owncloud-8.2.6.tar.bz2', 'owncloud-8.2.7.tar.bz2',
    'owncloud-8.2.8.tar.bz2', 'owncloud-8.2.9.tar.bz2', 'owncloud-9.0.0.tar.bz2', 'owncloud-9.0.1.tar.bz2',
    'owncloud-9.0.2.tar.bz2', 'owncloud-9.0.3.tar.bz2', 'owncloud-9.0.4.tar.bz2', 'owncloud-9.0.5.tar.bz2',
    'owncloud-9.0.6.tar.bz2', 'owncloud-9.0.7.tar.bz2', 'owncloud-9.0.8.tar.bz2', 'owncloud-9.0.9.tar.bz2',
    'owncloud-9.1.0.tar.bz2', 'owncloud-9.1.1.tar.bz2', 'owncloud-9.1.2.tar.bz2', 'owncloud-9.1.3RC1.tar.bz2',
    'owncloud-9.1.3.tar.bz2', 'owncloud-9.1.4RC2.tar.bz2', 'owncloud-9.1.4.tar.bz2', 'owncloud-9.1.5.tar.bz2',
    'owncloud-10.0.0beta.tar.bz2', 'owncloud-10.0.0RC2.tar.bz2', 'owncloud-10.0.0.tar.bz2', 'owncloud-10.0.1.tar.bz2'
]

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end
            sys.stderr.write("\n")
    else: # total size is unknown
        sys.stderr.write("read %d\n" % (readsofar,))

def download_files():
    print("[] Downloading owncloud archives")
    for filename in ARCHIVE_FILENAMES:
        url = '{}/{}'.format(MIRROR, filename)
        abs_filename = os.path.join(CACHE_DIR, filename)

        if os.path.exists(abs_filename):
            print("Archive {} already exists, skipping".format(filename))
        else:
            print("GET {}".format(url))
            urlretrieve(url, abs_filename, reporthook=reporthook)

def main():
    try:
        # Download all of the owncloud archives
        download_files()

        # Extract all of the owncloud archives

    except KeyboardInterrupt:
        print()
        pass

if __name__ == '__main__':
    main()
