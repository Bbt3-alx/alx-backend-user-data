<<<<<<< HEAD
#!/usr/bin/env python3
""" Cookie server
"""
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def root_path():
    """ Root path
    """
    return "Cookie value: {}\n".format(auth.session_cookie(request))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
=======
#!/usr/bin/env python3
""" Cookie server
"""
from flask import Flask, request
from api.v1.auth.auth import Auth

auth = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def root_path():
    """Root path"""
    return "Cookie value: {}\n".format(auth.session_cookie(request))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
>>>>>>> 602ad2db873e584a6748b04570a1f0b84a6e88bf
