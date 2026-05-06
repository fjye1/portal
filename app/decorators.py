from functools import wraps
from flask import abort
from flask_login import current_user
from app.models import ProjectAccess

def has_project_access(project_name):
    if current_user.admin:
        return True
    return ProjectAccess.query.filter_by(
        project_name=project_name,
        email=current_user.email.lower()
    ).first() is not None


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.admin:
            abort(403)  # forbidden
        return f(*args, **kwargs)
    return wrapper