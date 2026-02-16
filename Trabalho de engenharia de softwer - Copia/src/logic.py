notes = []
next_id = 1   # contador automático de ID

def create_note_logic(text):
    global next_id
    note = {
        "id": next_id,
        "text": text
    }
    notes.append(note)
    next_id += 1
    return note

def list_notes_logic():
    return notes

def update_note_logic(note_id, text):
    for note in notes:
        if note["id"] == note_id:
            note["text"] = text
            return True
    return False

def delete_note_logic(note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return True
    return False

def clear_notes():
    global next_id
    notes.clear()
    next_id = 1
