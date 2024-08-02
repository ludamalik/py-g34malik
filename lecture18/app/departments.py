from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from .models import db, Department

bp = Blueprint('departments', __name__)

@bp.route("/departments/index")
def index():
    departments = Department.query.all()
    return render_template("departments/index.html", departments=departments)

@bp.route("/departments/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        name = request.form.get("name")
        new_department = Department(name=name)
        db.session.add(new_department)
        db.session.commit()
        return redirect(url_for("departments.index"))
    return render_template("departments/create.html")

@bp.route("/departments/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    department = Department.query.get_or_404(id)
    if request.method == "POST":
        department.name = request.form.get("name")
        db.session.commit()
        return redirect(url_for("departments.index"))
    return render_template("departments/update.html", department=department)

@bp.route("/departments/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    return redirect(url_for("departments.index"))


