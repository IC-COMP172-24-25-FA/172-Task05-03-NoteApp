from flask import Flask, request

app = Flask(__name__)
notes = ["Here is note 1", "and note 2"]


@app.route("/")
def show_notes():
    note_display_str = ""
    for i in range(len(notes)):
        note_display_str += "{}: {}<br>".format(i+1, notes[i])

    add_note_form = """
        <form action="/addnote" method="post">
             <input type='text' name='new_note'>
             <input type='submit' value='Add Note'>
        </form>
    """

    remove_note_form = ""

    clear_all_notes_form = ""

    return note_display_str + add_note_form + remove_note_form + clear_all_notes_form


@app.route("/addnote", methods=["POST"])
def new_note_confirmation():
    new_note = request.form.get("new_note", "")
    if new_note != "":
        notes.append(new_note)
        message = "New Note Added."
    else:
        message = "No new note to add."
    return message + "<br><br><a href='/'> Back to notes </a>"


if __name__ == "__main__":
    app.run(host="localhost", debug=True)
