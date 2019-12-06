import sys


def application(env, start_response):
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    start_response("200 OK", [("Content-Type", "text/plain")])
    message = "222222222222222222 default Nginx uWSGI Python 3.6 app in a Docker container in Alpine (default)".format(
        version
    )
    return [message.encode("utf-8")]
