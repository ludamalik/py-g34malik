from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Role

bp = Blueprint('roles', __name__)

@bp.route("/roles/index")
def index():
    roles = Role.query.all()
    return render_template("roles/index.html", roles=roles)

@bp.route("/roles/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form.get("name")
        new_role = Role(name=name)
        db.session.add(new_role)
        db.session.commit()
        return redirect(url_for("roles.index"))
    return render_template("roles/create.html")

