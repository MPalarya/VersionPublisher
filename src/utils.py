import os
import shutil

MAX_BUFFER_SIZE = 1024


def make_file_copy(src, dst, show_progress):
    """
    Copy a src file to dst
    if dst is a directory, the src file will be copied using the same name
    otherwise, the src file will be copied to the absolute path of dst
    * if file already exists, it will be overwritten
    :param src:
    :param dst:
    :param show_progress:
    :return:
    """
    if not show_progress:
        shutil.copy2(src, dst)

    else:
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
            print '\r\t Copying.. {0}%'.format(int(copied * 100.0 / total_size)),
        print "\n\n\n"
        fsrc.close()
        fdst.close()


def delete_old_files(directory, ext, keep_n_recent, show_print=True):
    """
    deletes 'ext' files from dir, while keeping n most recent files
    :param directory:
    :param ext:
    :param keep_n_recent:
    :return: void
    """
    if show_print:
        print ">>> Trying to remove older versions from: %s\n" % directory
    dst_files = get_files(directory, ext, sort=True)
    if 0 < keep_n_recent < len(dst_files):
        for i in range(len(dst_files) - keep_n_recent):
            if show_print:
                print "\t removing: %s" % dst_files[i]
            os.remove(dst_files[i])
    print ""


def get_files(directory, ext, sort=False):
    """
    returns a list of all 'ext' extension files from dir, sorted by creation time on request
    :param directory: directory path
    :param ext: file extension
    :param sort: sort list by creation time
    :return: list file paths
    """
    lst_files = [os.path.join(directory, x) for x in os.listdir(directory) if x.lower().endswith(ext)]
    if sort:
        lst_files.sort(key=lambda y: os.path.getctime(y))
    return lst_files
