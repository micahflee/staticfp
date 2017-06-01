#!/usr/bin/env python3
import os
import json

import common

MIRROR = 'https://wordpress.org'
ARCHIVE_FILENAMES = [
    'wordpress-4.7.5.tar.gz', 'wordpress-4.7.4.tar.gz', 'wordpress-4.7.3.tar.gz', 'wordpress-4.7.2.tar.gz',
    'wordpress-4.7.1.tar.gz', 'wordpress-4.7.tar.gz', 'wordpress-4.6.6.tar.gz', 'wordpress-4.6.5.tar.gz',
    'wordpress-4.6.4.tar.gz', 'wordpress-4.6.3.tar.gz', 'wordpress-4.6.2.tar.gz', 'wordpress-4.6.1.tar.gz',
    'wordpress-4.6.tar.gz', 'wordpress-4.5.9.tar.gz', 'wordpress-4.5.8.tar.gz', 'wordpress-4.5.7.tar.gz',
    'wordpress-4.5.6.tar.gz', 'wordpress-4.5.5.tar.gz', 'wordpress-4.5.4.tar.gz', 'wordpress-4.5.3.tar.gz',
    'wordpress-4.5.2.tar.gz', 'wordpress-4.5.1.tar.gz', 'wordpress-4.5.tar.gz', 'wordpress-4.4.10.tar.gz',
    'wordpress-4.4.9.tar.gz', 'wordpress-4.4.8.tar.gz', 'wordpress-4.4.7.tar.gz', 'wordpress-4.4.6.tar.gz',
    'wordpress-4.4.5.tar.gz', 'wordpress-4.4.4.tar.gz', 'wordpress-4.4.3.tar.gz', 'wordpress-4.4.2.tar.gz',
    'wordpress-4.4.1.tar.gz', 'wordpress-4.4.tar.gz', 'wordpress-4.3.11.tar.gz', 'wordpress-4.3.10.tar.gz',
    'wordpress-4.3.9.tar.gz', 'wordpress-4.3.8.tar.gz', 'wordpress-4.3.7.tar.gz', 'wordpress-4.3.6.tar.gz',
    'wordpress-4.3.5.tar.gz', 'wordpress-4.3.4.tar.gz', 'wordpress-4.3.3.tar.gz', 'wordpress-4.3.2.tar.gz',
    'wordpress-4.3.1.tar.gz', 'wordpress-4.3.tar.gz', 'wordpress-4.2.15.tar.gz', 'wordpress-4.2.14.tar.gz',
    'wordpress-4.2.13.tar.gz', 'wordpress-4.2.12.tar.gz', 'wordpress-4.2.11.tar.gz', 'wordpress-4.2.10.tar.gz',
    'wordpress-4.2.9.tar.gz', 'wordpress-4.2.8.tar.gz', 'wordpress-4.2.7.tar.gz', 'wordpress-4.2.6.tar.gz',
    'wordpress-4.2.5.tar.gz', 'wordpress-4.2.4.tar.gz', 'wordpress-4.2.3.tar.gz', 'wordpress-4.2.2.tar.gz',
    'wordpress-4.2.1.tar.gz', 'wordpress-4.2.tar.gz', 'wordpress-4.1.18.tar.gz', 'wordpress-4.1.17.tar.gz',
    'wordpress-4.1.16.tar.gz', 'wordpress-4.1.15.tar.gz', 'wordpress-4.1.14.tar.gz', 'wordpress-4.1.13.tar.gz',
    'wordpress-4.1.12.tar.gz', 'wordpress-4.1.11.tar.gz', 'wordpress-4.1.10.tar.gz', 'wordpress-4.1.9.tar.gz',
    'wordpress-4.1.8.tar.gz', 'wordpress-4.1.7.tar.gz', 'wordpress-4.1.6.tar.gz', 'wordpress-4.1.5.tar.gz',
    'wordpress-4.1.4.tar.gz', 'wordpress-4.1.3.tar.gz', 'wordpress-4.1.2.tar.gz', 'wordpress-4.1.1.tar.gz',
    'wordpress-4.1.tar.gz', 'wordpress-4.0.18.tar.gz', 'wordpress-4.0.17.tar.gz', 'wordpress-4.0.16.tar.gz',
    'wordpress-4.0.15.tar.gz', 'wordpress-4.0.14.tar.gz', 'wordpress-4.0.13.tar.gz', 'wordpress-4.0.12.tar.gz',
    'wordpress-4.0.11.tar.gz', 'wordpress-4.0.10.tar.gz', 'wordpress-4.0.9.tar.gz', 'wordpress-4.0.8.tar.gz',
    'wordpress-4.0.7.tar.gz', 'wordpress-4.0.6.tar.gz', 'wordpress-4.0.5.tar.gz', 'wordpress-4.0.4.tar.gz',
    'wordpress-4.0.3.tar.gz', 'wordpress-4.0.2.tar.gz', 'wordpress-4.0.1.tar.gz', 'wordpress-4.0.tar.gz',
    'wordpress-3.9.19.tar.gz', 'wordpress-3.9.18.tar.gz', 'wordpress-3.9.17.tar.gz', 'wordpress-3.9.16.tar.gz',
    'wordpress-3.9.15.tar.gz', 'wordpress-3.9.14.tar.gz', 'wordpress-3.9.13.tar.gz', 'wordpress-3.9.12.tar.gz',
    'wordpress-3.9.11.tar.gz', 'wordpress-3.9.10.tar.gz', 'wordpress-3.9.9.tar.gz', 'wordpress-3.9.8.tar.gz',
    'wordpress-3.9.7.tar.gz', 'wordpress-3.9.6.tar.gz', 'wordpress-3.9.5.tar.gz', 'wordpress-3.9.4.tar.gz',
    'wordpress-3.9.3.tar.gz', 'wordpress-3.9.2.tar.gz', 'wordpress-3.9.1.tar.gz', 'wordpress-3.9.tar.gz',
    'wordpress-3.8.21.tar.gz', 'wordpress-3.8.20.tar.gz', 'wordpress-3.8.19.tar.gz', 'wordpress-3.8.18.tar.gz',
    'wordpress-3.8.17.tar.gz', 'wordpress-3.8.16.tar.gz', 'wordpress-3.8.15.tar.gz', 'wordpress-3.8.14.tar.gz',
    'wordpress-3.8.13.tar.gz', 'wordpress-3.8.12.tar.gz', 'wordpress-3.8.11.tar.gz', 'wordpress-3.8.10.tar.gz',
    'wordpress-3.8.9.tar.gz', 'wordpress-3.8.8.tar.gz', 'wordpress-3.8.7.tar.gz', 'wordpress-3.8.6.tar.gz',
    'wordpress-3.8.5.tar.gz', 'wordpress-3.8.4.tar.gz', 'wordpress-3.8.3.tar.gz', 'wordpress-3.8.2.tar.gz',
    'wordpress-3.8.1.tar.gz', 'wordpress-3.8.tar.gz', 'wordpress-3.7.21.tar.gz', 'wordpress-3.7.20.tar.gz',
    'wordpress-3.7.19.tar.gz', 'wordpress-3.7.18.tar.gz', 'wordpress-3.7.17.tar.gz', 'wordpress-3.7.16.tar.gz',
    'wordpress-3.7.15.tar.gz', 'wordpress-3.7.14.tar.gz', 'wordpress-3.7.13.tar.gz', 'wordpress-3.7.12.tar.gz',
    'wordpress-3.7.11.tar.gz', 'wordpress-3.7.10.tar.gz', 'wordpress-3.7.9.tar.gz', 'wordpress-3.7.8.tar.gz',
    'wordpress-3.7.7.tar.gz', 'wordpress-3.7.6.tar.gz', 'wordpress-3.7.5.tar.gz', 'wordpress-3.7.4.tar.gz',
    'wordpress-3.7.3.tar.gz', 'wordpress-3.7.2.tar.gz', 'wordpress-3.7.1.tar.gz', 'wordpress-3.7.tar.gz',
    'wordpress-3.6.1.tar.gz', 'wordpress-3.6.tar.gz', 'wordpress-3.5.2.tar.gz', 'wordpress-3.5.1.tar.gz',
    'wordpress-3.5.tar.gz', 'wordpress-3.4.2.tar.gz', 'wordpress-3.4.1.tar.gz', 'wordpress-3.4.tar.gz',
    'wordpress-3.3.3.tar.gz', 'wordpress-3.3.2.tar.gz', 'wordpress-3.3.1.tar.gz', 'wordpress-3.3.tar.gz',
    'wordpress-3.2.1.tar.gz', 'wordpress-3.2.tar.gz', 'wordpress-3.1.4.tar.gz', 'wordpress-3.1.3.tar.gz',
    'wordpress-3.1.2.tar.gz', 'wordpress-3.1.1.tar.gz', 'wordpress-3.1.tar.gz', 'wordpress-3.0.6.tar.gz',
    'wordpress-3.0.5.tar.gz', 'wordpress-3.0.4.tar.gz', 'wordpress-3.0.3.tar.gz', 'wordpress-3.0.2.tar.gz',
    'wordpress-3.0.1.tar.gz', 'wordpress-3.0.tar.gz', 'wordpress-2.9.2.tar.gz', 'wordpress-2.9.1.tar.gz',
    'wordpress-2.9.tar.gz', 'wordpress-2.8.6.tar.gz', 'wordpress-2.8.5.tar.gz', 'wordpress-2.8.4.tar.gz',
    'wordpress-2.8.3.tar.gz', 'wordpress-2.8.2.tar.gz', 'wordpress-2.8.1.tar.gz', 'wordpress-2.8.tar.gz',
    'wordpress-2.7.1.tar.gz', 'wordpress-2.7.tar.gz', 'wordpress-2.6.5.tar.gz', 'wordpress-2.6.3.tar.gz',
    'wordpress-2.6.2.tar.gz', 'wordpress-2.6.1.tar.gz', 'wordpress-2.6.tar.gz', 'wordpress-2.5.1.tar.gz',
    'wordpress-2.5.tar.gz', 'wordpress-2.3.3.tar.gz', 'wordpress-2.3.2.tar.gz', 'wordpress-2.3.1.tar.gz',
    'wordpress-2.3.tar.gz', 'wordpress-2.2.3.tar.gz', 'wordpress-2.2.2.tar.gz', 'wordpress-2.2.1.tar.gz',
    'wordpress-2.2.tar.gz', 'wordpress-2.1.3.tar.gz', 'wordpress-2.1.2.tar.gz', 'wordpress-2.1.1.tar.gz',
    'wordpress-2.1.tar.gz', 'wordpress-2.0.11.tar.gz', 'wordpress-2.0.10.tar.gz', 'wordpress-2.0.9.tar.gz',
    'wordpress-2.0.8.tar.gz', 'wordpress-2.0.7.tar.gz', 'wordpress-2.0.6.tar.gz', 'wordpress-2.0.5.tar.gz',
    'wordpress-2.0.4.tar.gz', 'wordpress-2.0.1.tar.gz', 'wordpress-2.0.tar.gz', 'wordpress-1.5.2.tar.gz',
    'wordpress-1.5.1.3.tar.gz', 'wordpress-1.5.1.2.tar.gz', 'wordpress-1.5.1.1.tar.gz', 'wordpress-1.5.1.tar.gz',
    'wordpress-1.5-strayhorn.tar.gz', 'wordpress-1.2.2.tar.gz', 'wordpress-1.2.1.tar.gz', 'wordpress-1.2-mingus.tar.gz',
    'wordpress-1.2-delta.tar.gz', 'wordpress-1.0.2-blakey.tar.gz', 'wordpress-1.0.1-miles.tar.gz', 'wordpress-1.0-platinum.tar.gz',
    'wordpress-0.71-gold.tar.gz'
]

def wordpress_version_from_filename(filename):
    """
    If filename is 'wordpress-1.0.2-blakey.tar.gz', this returns '1.0.2-blakey'
    """
    return filename[len('wordpress-'):][0:-len('.tar.gz')]

def main():
    # Make a list of all owncloud versions
    versions = []
    for filename in ARCHIVE_FILENAMES:
        versions.append(wordpress_version_from_filename(filename))
    with open(os.path.join(common.DATA_DIR, 'wordpress_versions.json'), 'w') as outfile:
        json.dump(versions, outfile)

    # Download all of the owncloud archives
    print("[] Downloading wordpress archives")
    common.download_archives(ARCHIVE_FILENAMES, MIRROR)

    # Extract all of the owncloud archives
    print("[] Extract all wordpress archives")
    common.extract_archives(ARCHIVE_FILENAMES, 'wordpress-{}', wordpress_version_from_filename)

    # Build the owncloud data object, write to json
    print("[] Building the wordpress data object")
    (data, freq) = common.build_data(ARCHIVE_FILENAMES, 'wordpress-{}', wordpress_version_from_filename)
    with open(os.path.join(common.DATA_DIR, 'wordpress_data.json'), 'w') as outfile:
        json.dump(data, outfile)
    with open(os.path.join(common.DATA_DIR, 'wordpress_freq.json'), 'w') as outfile:
        json.dump(freq, outfile)

if __name__ == '__main__':
    main()
