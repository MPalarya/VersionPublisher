import re
import NSIScript

INSTALL_DIR = "$INSTDIR"
APP_DATA_DIR = "$APPDATA"
COMPANY_NAME = "Elbit Systems Land and C4I"

exclude_extensions = "pdb|db|obj|log|metagen|cache|config|manifest"
exclude_extensions = ".+\.(" + exclude_extensions + ")$"

NOTHING = "(?!x)x"
EVERYTHING = ".+\..+"
class CopyFiles:
    def __init__(self, name, source, destination, relative_path="",
                 recursive=True, include_regex=EVERYTHING, exclude_regex=NOTHING):
        self.name = name
        self.source = source
        self.destination = destination
        self.relative_path = relative_path
        self.recursive = recursive
        self.include_regex = include_regex
        self.exclude_regex = exclude_regex


def get_common():
    return [
        CopyFiles(
            name="Common DLLs",
            source=r"W:\TestersBundle\ModulesLauncher\bin\Debug",
            destination=INSTALL_DIR,
            recursive=False,
            exclude_regex=".?\.vshost\.exe.?",
            include_regex=".+\.(dll|exe|ini)$"
        ),
        CopyFiles(
            name="DevExpress DLLs",
            source=r"W:\TestersBundle\Common\bin\Debug",
            destination=INSTALL_DIR,
            relative_path=r"DevExpress",
            recursive=False,
            include_regex="^DevExpress\..+\.dll$"
        ),
        CopyFiles(
            name="Devices Module",
            source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\DevicesModule",
            destination=INSTALL_DIR,
            relative_path=r"Modules\DevicesModule",
            recursive=False,
            exclude_regex=exclude_extensions
        ),
        CopyFiles(
            name="Devices Module bin",
            source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\DevicesModule\bin",
            destination=INSTALL_DIR,
            relative_path=r"Modules\DevicesModule\bin",
            recursive=False,
            include_regex=".+\.dll$"
        ),
    ]


def get_script_va(output_folder):
    product_name = "VA Tester"
    product_version = "0.0.0.0"
    assembly = r"W:\TestersBundle\Testers\VaTester\Properties\AssemblyInfo.cs"

    # get version from Visual Studio's project
    with open(assembly) as assembly_file:
        for l in assembly_file.readlines():
            if re.match("^\[assembly: AssemblyVersion\(\"\d+\.\d+\.\d+\.\d+\"\)\]$", l, flags=re.IGNORECASE):
                product_version = l.split("\"")[1]
                print "\n>>> Creating NSIS script for version %s\n" % product_version

    # TODO: skip stupid folders

    commands = get_common()
    commands.extend(
        [
            CopyFiles(
                name="VA Module",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\VA",
                destination=INSTALL_DIR,
                relative_path=r"Modules\VA",
                exclude_regex=exclude_extensions
            ),
            CopyFiles(
                name="Program Data Files",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\VA\Files\ProgramData",
                destination=APP_DATA_DIR,
                exclude_regex=exclude_extensions
            ),
            CopyFiles(
                name="Launcher Files",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\VA\Files",
                destination=INSTALL_DIR,
                recursive=False,
            ),
            CopyFiles(
                name="Device Templates",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\DevicesModule\Devices\Templates\VA",
                destination=INSTALL_DIR,
                relative_path=r"Modules\DevicesModule\Devices\Templates\VA",
                exclude_regex=exclude_extensions
            )
        ]
    )
    return NSIScript.create_script(commands, COMPANY_NAME, product_name, product_version, output_folder)


def get_script_manpack(output_folder):
    product_name = "Manpack Tester"
    product_version = "0.0.0.0"
    assembly = r"W:\TestersBundle\Testers\ManPack SDR Tester\Properties\AssemblyInfo.cs"

    # get version from Visual Studio's project
    with open(assembly) as assembly_file:
        for l in assembly_file.readlines():
            if re.match("^\[assembly: AssemblyVersion\(\"\d+\.\d+\.\d+\.\d+\"\)\]$", l, flags=re.IGNORECASE):
                product_version = l.split("\"")[1]
                print "\n>>> Creating NSIS script for version %s\n" % product_version

    # TODO: skip stupid folders

    commands = get_common()
    commands.extend(
        [
            CopyFiles(
                name="Manpack Module",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\Manpack-SDR",
                destination=INSTALL_DIR,
                relative_path=r"Modules\Manpack-SDR",
                exclude_regex=exclude_extensions
            ),
            CopyFiles(
                name="Program Data Files",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\Manpack-SDR\Files\ProgramData",
                destination=APP_DATA_DIR,
                exclude_regex=exclude_extensions
            ),
            CopyFiles(
                name="Launcher Files",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\Manpack-SDR\Files",
                destination=INSTALL_DIR,
                recursive=False,
            ),
            CopyFiles(
                name="Manpack Device Template",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\DevicesModule\Devices\Templates\ManPackSDR",
                destination=INSTALL_DIR,
                relative_path=r"Modules\DevicesModule\Devices\Templates\ManPackSDR",
                exclude_regex=exclude_extensions
            ),
            CopyFiles(
                name="Matrix Device Template",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\DevicesModule\Devices\Templates\MatrixDevice",
                destination=INSTALL_DIR,
                relative_path=r"Modules\DevicesModule\Devices\Templates\MatrixDevice",
                exclude_regex=exclude_extensions
            )
        ]
    )
    return NSIScript.create_script(commands, COMPANY_NAME, product_name, product_version, output_folder)


def get_script_uwb(output_folder):
    product_name = "UWB Tester"
    product_version = "0.0.0.0"
    assembly = r"W:\TestersBundle\Testers\UWBTester\Properties\AssemblyInfo.cs"

    # get version from Visual Studio's project
    with open(assembly) as assembly_file:
        for l in assembly_file.readlines():
            if re.match("^\[assembly: AssemblyVersion\(\"\d+\.\d+\.\d+\.\d+\"\)\]$", l):
                product_version = l.split("\"")[1]
                print "\n>>> Creating NSIS script for version %s\n" % product_version

    # TODO: skip stupid folders

    commands = get_common()
    commands.extend(
        [
            CopyFiles(
                name="UWB Module",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\UWB",
                destination=INSTALL_DIR,
                relative_path=r"Modules\UWB",
                exclude_regex=exclude_extensions
            ),
            CopyFiles(
                name="Program Data Files",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\UWB\Files\ProgramData",
                destination=APP_DATA_DIR,
                exclude_regex=exclude_extensions
            ),
            CopyFiles(
                name="Launcher Files",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\UWB\Files",
                destination=INSTALL_DIR,
                recursive=False,
            ),
            CopyFiles(
                name="Device Templates",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\DevicesModule\Devices\Templates\UWB",
                destination=INSTALL_DIR,
                relative_path=r"Modules\DevicesModule\Devices\Templates\UWB",
                exclude_regex=exclude_extensions
            )
        ]
    )
    return NSIScript.create_script(commands, COMPANY_NAME, product_name, product_version, output_folder)

def get_script_eladin(output_folder):
    product_name = "Eladin Tester"
    product_version = "0.0.0.0"
    assembly = r"W:\TestersBundle\Testers\EladinTester\Properties\AssemblyInfo.cs"

    # get version from Visual Studio's project
    with open(assembly) as assembly_file:
        for l in assembly_file.readlines():
            if re.match("^\[assembly: AssemblyVersion\(\"\d+\.\d+\.\d+\.\d+\"\)\]$", l):
                product_version = l.split("\"")[1]
                print product_version
                print "\n>>> Creating NSIS script for version %s\n" % product_version

    # TODO: skip stupid folders

    commands = get_common()
    commands.extend(
        [
            CopyFiles(
                name="Eladin Module",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\EladinTester",
                destination=INSTALL_DIR,
                relative_path=r"Modules\EladinTester",
                exclude_regex=exclude_extensions
            ),
            CopyFiles(
                name="Program Data Files",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\EladinTester\Files\ProgramData",
                destination=APP_DATA_DIR,
                exclude_regex=exclude_extensions
            ),
            CopyFiles(
                name="Launcher Files",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\EladinTester\Files",
                destination=INSTALL_DIR,
                recursive=False,
            ),
            CopyFiles(
                name="Eladin Device Templates",
                source=r"W:\TestersBundle\ModulesLauncher\bin\Debug\Modules\DevicesModule\Devices\Templates\Eladin",
                destination=INSTALL_DIR,
                relative_path=r"Modules\DevicesModule\Devices\Templates\Eladin",
                exclude_regex=exclude_extensions
            )
        ]
    )
    return NSIScript.create_script(commands, COMPANY_NAME, product_name, product_version, output_folder)


def build_setup_va(output_folder):
    NSIScript.compile_script(get_script_va(output_folder))


def build_setup_manpack(output_folder):
    NSIScript.compile_script(get_script_manpack(output_folder))


def build_setup_nmn(output_folder):
    NSIScript.compile_script(get_script_va(output_folder))


def build_setup_uwb(output_folder):
    NSIScript.compile_script(get_script_uwb(output_folder))


def build_setup_eladin(output_folder):
    NSIScript.compile_script(get_script_eladin(output_folder))


def build_setup_hh(output_folder):
    NSIScript.compile_script(get_script_va(output_folder))