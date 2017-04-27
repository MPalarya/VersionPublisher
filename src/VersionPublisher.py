import os
import sys
import utils
import BuildSetup

"""
This file defines the functions manage the files between source-path and destination-path
Used as a shortcut to publish new versions easier

Created:    2017-03-06
By:         Michael Palarya
"""

SHOW_COPY_PROGRESS = True
KEEP_N_RECENT_FILES = 7


def publish_recent(src, dst, ext=".exe", keep_n_recent=KEEP_N_RECENT_FILES):
    """
    Copy most recent file with 'ext' extension from src directory to dst directory

    :param src: source directory
    :param dst: destination directory
    :param ext: file extension to be copied
    :param keep_n_recent: indicates max number of files to keep, deletes oldest (if n > 0)
    :return: void
    """
    print "\n>>> Looking for most recent \'%s\' file in \'%s\'\n" % (ext, src)
    lst_files = utils.get_files(src, ext)
    if not lst_files:
        print "\t No such file found, aborting."
        return

    latest_version = os.path.basename(max(lst_files, key=os.path.getctime))
    print "\t Latest version available: \'%s\'\n" % latest_version

    publish(os.path.join(src, latest_version), dst)
    utils.delete_old_files(dst, ext, keep_n_recent)
    utils.delete_old_files(src, ext, keep_n_recent)


def publish(src, dst):
    """
    Copy a src file to dst
    if dst is a directory, the src file will be copied using the same name
    otherwise, the src file will be copied to the absolute path of dst
    * if file already exists, it will be overwritten

    :param src: path of source file to be copied
    :param dst: full path including file name, or only directory path of destination
    :return: void
    """
    print "\n>>> Trying to copy:\n"
    print "\t %s \n\t -> \n\t %s \n" % (src, dst)

    try:
        utils.make_file_copy(src, dst, SHOW_COPY_PROGRESS)

    except EnvironmentError, err:
        print "Unable to copy file. %s" % err

    else:
        print ">>> Copy successful!"


if __name__ == '__main__':
    """
    Assumes parameters are passed correctly, [1]-tester name
    """

    tester_name = sys.argv[1]

    if tester_name == "va":
        output_folder = r"I:\VA Tester"
        publish_folder = r"\\jellyfish02\Projects\Manpack SDR\VA"
        BuildSetup.build_setup_va(output_folder)
        publish_recent(output_folder, publish_folder)

    elif tester_name == "manpack":
        #######
        output_folder = r"I:\ManPack-SDR Tester"
        publish_folder = r"\\jellyfish02\Projects\Manpack SDR\GUI Tester"
        BuildSetup.build_setup_manpack(output_folder)
        publish_recent(output_folder, publish_folder)

    elif tester_name == "uwb":
        output_folder = r"I:\UWB Tester"
        publish_folder = r"\\jellyfish02\Projects\Manpack SDR\UWB Tester"
        BuildSetup.build_setup_uwb(output_folder)
        publish_recent(output_folder, publish_folder)

    elif tester_name == "eladin":
        output_folder = r"I:\Eladin Tester"
        publish_folder = r"\\jellyfish02\Projects\Manpack SDR\WCF"
        BuildSetup.build_setup_eladin(output_folder)
        publish_recent(output_folder, publish_folder)

    elif tester_name == "nmn":
        output_folder = r"I:\VA Tester"
        publish_folder = r"\\jellyfish02\Projects\Manpack SDR\VA"
        BuildSetup.build_setup_va(output_folder)
        publish_recent(output_folder, publish_folder)

    elif tester_name == "hh":
        output_folder = r"I:\VA Tester"
        publish_folder = r"\\jellyfish02\Projects\Manpack SDR\VA"
        BuildSetup.build_setup_va(output_folder)
        publish_recent(output_folder, publish_folder)

    else:
        print "Error."
