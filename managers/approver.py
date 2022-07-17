from werkzeug.exceptions import BadRequest
from werkzeug.security import check_password_hash

from managers.auth import AuthManager
from models.user import ApproverModel


class ApproverManager:
    @staticmethod
    def login(data):
        #TO DO refactor as sub-func and reuse in complainer as well, later in admin
        approver = ApproverModel.query.filter_by(email=data['email']).first()
        if not approver:
            raise BadRequest('Please register!')

        if check_password_hash(approver.password,data['password']):
            return AuthManager.encode_token(approver)
        raise BadRequest('Invalid Credentials')        