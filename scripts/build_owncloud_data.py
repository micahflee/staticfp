#!/usr/bin/env python3
import sys
import os
import shutil
import subprocess
import hashlib

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

def download_archives():
    print("[] Downloading owncloud archives")
    for filename in ARCHIVE_FILENAMES:
        url = '{}/{}'.format(MIRROR, filename)
        abs_filename = os.path.join(CACHE_DIR, filename)

        if os.path.exists(abs_filename):
            print("Archive {} already exists, skipping".format(filename))
        else:
            print("GET {}".format(url))
            try:
                urlretrieve(url, abs_filename, reporthook=reporthook)
            except KeyboardInterrupt:
                os.remove(abs_filename)
                print("")
                sys.exit()

def extract_archives():
    print("[] Extract all owncloud archives")
    for filename in ARCHIVE_FILENAMES:
        abs_filename = os.path.join(CACHE_DIR, filename)
        extracted_dir = abs_filename.rstrip('.tar.bz2')

        if os.path.exists(extracted_dir):
            print("Archive {} has already been extracted, skipping".format(filename))
        else:
            os.mkdir(extracted_dir)
            try:
                print("Extracting {}".format(filename))
                subprocess.call(['tar', '-xf', abs_filename, '--directory', extracted_dir])
            except KeyboardInterrupt:
                shutil.rmtree(extracted_dir)
                print("")
                sys.exit()

def build_data():
    """
    This function returns a tuple with a data dictionary containing all of the
    owncloud data, along with a list of filenames sorted by the most hashes first.

    The data dict is structured like this:

    {
        'owncloud/somefile.txt': {
            'sha256_hash1': ['version1', 'version2'],
            'sha256_hash2': ['version3']
        },
        'owncloud/some_other_file.png': {
            'sha256_hash3': ['version1']
        }
    }

    The list is sorted so that it starts with the filenames that contain the most
    unique hashes for all of the owncloud versions (basically, that change the most
    frequently), and ends with the filenames that change the least frequently.
    """

    # Start by building a dictionary version of the data this isn't sorted
    data = {}

    for archive_filename in ARCHIVE_FILENAMES:
        abs_archive_filename = os.path.join(CACHE_DIR, archive_filename)
        extracted_dir = abs_archive_filename.rstrip('.tar.bz2')
        version = archive_filename.lstrip('owncloud-').rstrip('.tar.bz2')

        # Loop through all of the files in this archive
        for (dirpath, _, filenames) in os.walk(extracted_dir):
            for f in filenames:
                # Skip php files
                if f.endswith('.php'):
                    continue

                # Get the hash
                filename = os.path.join(dir_path, f)
                with open(filename, 'rb') as f:
                    sha256_hash = hashlib.sha256(f.read()).hexdigest()

                # Add it to the dictionary
                if filename not in data:
                    data[filename] = {}
                if sha256_hash not in d[filename]:
                    data[filename][sha256_hash] = []
                if version not in d[filename][sha256_hash]:
                    data[filename][sha256_hash].append(version)

    # Now sort the data by the number of hashes each file has
    freq_tuple = [(len(val), key) for (key, val) in data.items()]
    freq_tuple.sort(reverse=True)
    freq = [key for (count, key) in freq_tuple]

    return (data, freq)

def main():
    # Download all of the owncloud archives
    download_archives()

    # Extract all of the owncloud archives
    extract_archives()

    # Build the owncloud data object
    #(data, freq) = build_data()

if __name__ == '__main__':
    main()
