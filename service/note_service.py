from perfumer.resource import load_notes
from model.note import Note


def get_notes() -> [Note]:
    notes_json = load_notes()
    notes_list = []
    for note_object in notes_json['notes']:
        note = Note(note_object['id'],
                    note_object['name'],
                    note_object['normal_image_url'],
                    note_object['thumb_image_url'])
        notes_list.append(note)
    return notes_list

