from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash,check_password_hash

from db import db
from managers.auth import AuthManager
from models.user import ComplainerModel
