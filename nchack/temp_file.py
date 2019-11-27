import tempfile
import os


from .session import session_stamp

def temp_file(ext = ""):

        # check space left in temp dir and switch it if there isn't much
        if session_stamp["temp_dir"] == "/tmp/":
            result = os.statvfs("/tmp/")
            result = result.f_frsize * result.f_bavail

            if result <  0.5 * 1e9:
                if session_stamp["temp_dir"] == "/tmp/":
                    session_stamp["temp_dir"] = "/var/tmp/"

        actual_temp = session_stamp["temp_dir"]
        actual_temp = actual_temp + "/"
        actual_temp = actual_temp.replace("//", "/")

        target = tempfile.NamedTemporaryFile().name
        target = target.replace("tmp/", "tmp/" + session_stamp["stamp"])

        if ext is not None:
            target = actual_temp + os.path.basename(target)
            if type(ext) is not str:
                raise TypeError("Extension supplied is not a str")
            if ext.startswith("."):
                target = target + ext
            else:
                target = target + "." +  ext

        else:
            target = actual_temp + os.path.basename(target)

        return target


