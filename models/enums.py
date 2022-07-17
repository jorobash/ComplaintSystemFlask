from enum import Enum

class UserRole(Enum):
    complainer = "Complainer"
    approver   = "Approver"
    admmin     = "Admin"


class ComplaintState(Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"    