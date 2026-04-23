from flask import Blueprint, send_from_directory, render_template, redirect, url_for, current_app
from flask_login import login_required
import os
home_bp = Blueprint('home', __name__)


@home_bp.route("/")
def index():
    return redirect(url_for("auth.login"))

@home_bp.route('/portal')
@login_required # Add this if you want only logged-in users to see the portal
def portal():
    portal_path = os.path.join(current_app.root_path, 'projects', 'portal')
    return send_from_directory(portal_path, 'index.html')


@home_bp.route('/kit_website/')
@home_bp.route('/kit_website/<path:path>')
@login_required
def kit_website(path='index.html'):
    kit_path = os.path.join(current_app.root_path, 'projects', 'kit_website')
    return send_from_directory(kit_path, path)

# 4. Samadhi Therapies (Matches your HTML link: /SamadhiTherapies/)
@home_bp.route('/SamadhiTherapies/')
@home_bp.route('/SamadhiTherapies/<path:path>')
@login_required
def samadhi_therapies(path='index.html'):
    saba_path = os.path.join(current_app.root_path, 'projects', 'Samadhi-Therapies')
    return send_from_directory(saba_path, path)

