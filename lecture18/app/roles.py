from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from .models import db, Role

bp = Blueprint('roles', __name__)

@bp.route("/roles/index")
def index():
    roles = Role.query.all()
    return render_template("roles/index.html", roles=roles)

@bp.route("/roles/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        name = request.form.get("name")
        new_role = Role(name=name)
        db.session.add(new_role)
        db.session.commit()
        return redirect(url_for("roles.index"))
    return render_template("roles/create.html")

@bp.route("/roles/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    role = Role.query.get_or_404(id)
    if request.method == "POST":
        role.name = request.form.get("name")
        db.session.commit()
        return redirect(url_for("roles.index"))
    return render_template("roles/update.html", role=role)

@bp.route("/roles/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    return redirect(url_for("roles.index"))


