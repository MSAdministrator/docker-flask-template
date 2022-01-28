from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
cache = Cache()
session = Session()