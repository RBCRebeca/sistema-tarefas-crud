# tests/test_notes.py

from logic import (
    create_note_logic,
    list_notes_logic,
    update_note_logic,
    delete_note_logic,
    clear_notes
)

def setup_function():
    clear_notes()

def test_create_note():
    note = create_note_logic("Primeira anotação")
    assert note["text"] == "Primeira anotação"
    assert len(list_notes_logic()) == 1

def test_list_notes():
    create_note_logic("Nota 1")
    create_note_logic("Nota 2")
    notes = list_notes_logic()
    assert len(notes) == 2

def test_update_note():
    create_note_logic("Antiga")
    result = update_note_logic(0, "Nova")
    assert result == True
    assert list_notes_logic()[0]["text"] == "Nova"

def test_delete_note():
    create_note_logic("Excluir")
    result = delete_note_logic(0)
    assert result == True
    assert len(list_notes_logic()) == 0

def test_invalid_update():
    result = update_note_logic(0, "Teste")
    assert result == False

def test_invalid_delete():
    result = delete_note_logic(0)
    assert result == False
