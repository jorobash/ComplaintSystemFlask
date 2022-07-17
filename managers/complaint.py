from db import db
from models import ComplaintModel,UserRole,ComplaintState


class ComplaintManager:
    @staticmethod
    def get_complaints(user):
        if user.role == UserRole.complainer:
            return ComplaintModel.query.filter_by(complainer_id=user.id).all()
        return ComplaintModel.query.all()