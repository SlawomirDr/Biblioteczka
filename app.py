from flask import Flask, request, render_template, redirect, url_for, jsonify, abort

from forms import BookForm
from models import books

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/todos/", methods=["GET"])
def books_list():
    form = BookForm()
    error = ""
    return render_template("books.html", form=form, books=books.all(), error=error)    
    
@app.route("/todos/", methods=["POST"])
def create_book():
    form = BookForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
            books.save_all()
        return redirect(url_for("books_list"))


@app.route("/todos/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = books.get(book_id - 1)
    form = BookForm(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            books.update(book_id - 1, form.data)
        return redirect(url_for("books_list"))
    return render_template("book.html", form=form, book_id=book_id)



if __name__ == "__main__":
    app.run(debug=True)