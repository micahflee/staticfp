import sys
import os
import subprocess
import shutil
import hashlib

from urllib.request import urlretrieve

CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cache')
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

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

def download_archives(archive_filenames, mirror):
    for filename in archive_filenames:
        url = '{}/{}'.format(mirror, filename)
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

def extract_archives(archive_filenames, extracted_dir_format, version_func):
    for filename in archive_filenames:
        abs_filename = os.path.join(CACHE_DIR, filename)
        extracted_dir = os.path.join(CACHE_DIR, extracted_dir_format.format(version_func(filename)))

        if os.path.exists(extracted_dir):
            print("Archive {} has already been extracted into {}, skipping".format(filename, extracted_dir))
        else:
            os.mkdir(extracted_dir)
            try:
                print("Extracting {} into {}".format(filename, extracted_dir))
                subprocess.call(['tar', '-xf', abs_filename, '--directory', extracted_dir])
            except KeyboardInterrupt:
                shutil.rmtree(extracted_dir)
                print("")
                sys.exit()

def build_data(archive_filenames, extracted_dir_format, version_func, filename_mod_func=None):
    """
    This function returns a tuple with a data dictionary containing all of the
    owncloud data, along with a list of filenames sorted by the most hashes first.

    The data dict is structured like this:

    {
        'somefile.txt': {
            'sha256_hash1': ['version1', 'version2'],
            'sha256_hash2': ['version3']
        },
        'some_other_file.png': {
            'sha256_hash3': ['version1']
        }
    }

    The list is sorted so that it starts with the filenames that contain the most
    unique hashes for all of the owncloud versions (basically, that change the most
    frequently), and ends with the filenames that change the least frequently.
    """
    sys.stdout.write("Parsing versions: ")

    # Start by building a dictionary version of the data this isn't sorted
    data = {}

    for archive_filename in archive_filenames:
        version = version_func(archive_filename)
        abs_archive_filename = os.path.join(CACHE_DIR, archive_filename)
        extracted_dir = os.path.join(CACHE_DIR, extracted_dir_format.format(version))

        sys.stdout.write("{} ".format(version))
        sys.stdout.flush()

        # Loop through all of the files in this archive
        for (dirpath, _, filenames) in os.walk(extracted_dir):
            for f in filenames:
                # Skip php files
                if f.endswith('.php'):
                    continue

                # Get the hash
                filename = os.path.join(dirpath, f)
                with open(filename, 'rb') as f:
                    sha256_hash = hashlib.sha256(f.read()).hexdigest()

                # Fix the filename so it's not prefixed with the absolute path to extracted_dir
                # e.g. 'owncloud/settings/l10n/th_TH.js' instead of '/home/user/code/staticfp/cache/owncloud-9.1.4/owncloud/settings/l10n/th_TH.js'
                filename = filename[len(extracted_dir)+1:]

                # Modify the filename in some other way
                if filename_mod_func:
                    filename = filename_mod_func(filename)

                # Add it to the dictionary
                if filename not in data:
                    data[filename] = {}
                if sha256_hash not in data[filename]:
                    data[filename][sha256_hash] = []
                if version not in data[filename][sha256_hash]:
                    data[filename][sha256_hash].append(version)

    sys.stdout.write("\n")
    sys.stdout.flush()

    # Now sort the data by the number of hashes each file has
    freq_tuple = [(len(val), key) for (key, val) in data.items()]
    freq_tuple.sort(reverse=True)
    freq = [key for (count, key) in freq_tuple]

    return (data, freq)
