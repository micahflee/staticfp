#!/usr/bin/env python3
import os
import json

import common

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

def owncloud_version_from_filename(filename):
    """
    If filename is 'owncloud-9.1.4RC2.tar.bz2', this returns '9.1.4RC2'
    """
    return filename[len('owncloud-'):][0:-len('.tar.bz2')]

def main():
    # Make a list of all owncloud versions
    versions = []
    for filename in ARCHIVE_FILENAMES:
        versions.append(owncloud_version_from_filename(filename))
    with open(os.path.join(common.DATA_DIR, 'owncloud_versions.json'), 'w') as outfile:
        json.dump(versions, outfile)

    # Download all of the owncloud archives
    print("[] Downloading owncloud archives")
    common.download_archives(ARCHIVE_FILENAMES, MIRROR)

    # Extract all of the owncloud archives
    print("[] Extract all owncloud archives")
    common.extract_archives(ARCHIVE_FILENAMES, 'owncloud-{}', owncloud_version_from_filename)

    # Build the owncloud data object, write to json
    def filename_mod_func(filename):
        # Remove the 'owncloud/' at the beginning
        return filename[len('owncloud/'):]

    print("[] Building the owncloud data object")
    (data, freq) = common.build_data(ARCHIVE_FILENAMES, 'owncloud-{}', owncloud_version_from_filename, filename_mod_func)
    with open(os.path.join(common.DATA_DIR, 'owncloud_data.json'), 'w') as outfile:
        json.dump(data, outfile)
    with open(os.path.join(common.DATA_DIR, 'owncloud_freq.json'), 'w') as outfile:
        json.dump(freq, outfile)

if __name__ == '__main__':
    main()
