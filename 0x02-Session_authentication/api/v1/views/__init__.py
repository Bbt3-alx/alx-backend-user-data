<<<<<<< HEAD
#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *

User.load_from_file()
=======
#!/usr/bin/env python3
""" DocDocDocDocDocDoc
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

User.load_from_file()
>>>>>>> 602ad2db873e584a6748b04570a1f0b84a6e88bf
