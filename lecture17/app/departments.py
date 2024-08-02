from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Department

bp = Blueprint('departments', __name__)

@bp.route("/departments/index")
def index():
    departments = Department.query.all()
    return render_template("departments/index.html", departments=departments)

@bp.route("/departments/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form.get("name")
        new_department = Department(name=name)
        db.session.add(new_department)
        db.session.commit()
        return redirect(url_for("departments.index"))
    return render_template("departments/create.html")

