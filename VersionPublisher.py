import os
import sys

"""
This file defines the functions manage the files between source-path and destination-path
Used as a shortcut to publish new versions easier

Created:    2017-03-06
By:         Michael Palarya
"""


def delete_old_files(directory, ext, keep_n_recent):
    """
    deletes 'ext' files from dir, while keeping n most recent files
    :param directory:
    :param ext:
    :param keep_n_recent:
    :return: void
    """
    print ">>> Trying to remove older versions from: %s\n" % directory
    dst_files = get_files(directory, ext, sort=True)
    if 0 < keep_n_recent < len(dst_files):
        for i in range(len(dst_files) - keep_n_recent):
            print "\t removing: %s" % dst_files[i]
            os.remove(dst_files[i])
    print ""


def get_files(dir, ext, sort=False):
    """
    returns a list of all 'ext' extension files from dir, sorted by creation time on request
    :param dir: directory path
    :param ext: file extension
    :param sort: sort list by creation time
    :return: list file paths
    """
    lst_files = [os.path.join(dir, x) for x in os.listdir(dir) if x.lower().endswith(ext)]
    if sort:
        lst_files.sort(key=lambda x: os.path.getctime(x))
    return lst_files


def publish_recent(src, dst, ext=".exe", show_progress=True, keep_n_recent=7):
    """
    Copy most recent file with 'ext' extension from src directory to dst directory

    :param src: source directory
    :param dst: destination directory
    :param ext: file extension to be copied
    :param show_progress: prints progress of copying
    :param keep_n_recent: indicates max number of files to keep, deletes oldest (if n > 0)
    :return: void
    """
    print "\n>>> Looking for most recent \'%s\' file in \'%s\'\n" % (ext, src)
    lst_files = get_files(src, ext)
    if not lst_files:
        print "\t No such file found, aborting."
        return

    latest_version = os.path.basename(max(lst_files, key=os.path.getctime))
    print "\t Latest version available: \'%s\'\n" % latest_version

    publish(os.path.join(src, latest_version), dst, show_progress)
    delete_old_files(dst, ext, keep_n_recent)
    delete_old_files(src, ext, keep_n_recent)


def publish(src, dst, show_progress=True):
    """
    Copy a src file to dst
    if dst is a directory, the src file will be copied using the same name
    otherwise, the src file will be copied to the absolute path of dst
    * if file already exists, it will be overwritten

    :param src: path of source file to be copied
    :param dst: full path including file name, or only directory path of destination
    :param show_progress: prints progress of copying
    :return: void
    """
    MAX_BUFFER_SIZE = 5 * 1024 * 1024  # 1 MB
    print "\n>>> Trying to copy:\n"
    print "\t %s" % src
    print "\t ->"
    print "\t %s\n" % dst

    try:
        fsrc = open(src, "rb")

        if os.path.isdir(dst):
            path = os.path.join(dst, os.path.basename(src))
        else:
            path = dst

        copied = 0
        total_size = os.path.getsize(src)

        fdst = open(path, "wb+")
        while True:
            buf = fsrc.read(MAX_BUFFER_SIZE)
            if not buf:
                break

            fdst.write(buf)
            copied += len(buf)

            if show_progress:
                print '\r\t Copying.. {0}%'.format(int(copied * 100.0 / total_size)),

        if show_progress:
            print "\n\n\n"

    except EnvironmentError, err:
        print "Unable to copy file. %s" % err

    else:
        print ">>> Copy successful!"

    finally:
        fsrc.close()
        print ">>> Closing the new file, please wait..."
        fdst.close()
        print ">>> Finished finalizing the new file."


if __name__ == '__main__':
    """
    Assumes parameters are passed correctly, [1]-src [2]-dst
    """
    publish_recent(sys.argv[1], sys.argv[2])
