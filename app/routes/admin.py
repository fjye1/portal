from flask import Blueprint, render_template, request, url_for
from flask_login import login_required

from app.decorators import admin_required
from app.extensions import db
from app.forms import ProjectForm
from app.models import ProjectAccess

admin_bp = Blueprint('admin', __name__)


@admin_bp.route("/admin/access", methods=["GET", "POST"])
@admin_required
@login_required
def manage_access():
    if request.method == "POST":
        project_name = request.form.get("project_name")
        email = request.form.get("email").lower().strip()

        entry = ProjectAccess(project_name=project_name, email=email)
        db.session.add(entry)
        db.session.commit()

    access_list = ProjectAccess.query.all()
    return render_template("home/access.html", access_list=access_list)
