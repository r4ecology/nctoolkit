import subprocess


def cf_checks(self, version=None):
    """
    Method to run the cf checker from the Met Office on files
    """
    self.run()
    if type(self.current) is list:
        raise TypeError("This presently only works for single file datasets")

    if version is None:
        version = 1.6
        print("Using CF version 1.6")

    if version not in [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8]:
        raise ValueError("Version supplied is not valid!")

    version = str(version)
    command = f"cfchecks -v {version} {self.current}"
    out = subprocess.Popen(
        command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    result, ignore = out.communicate()
    return result.decode()
