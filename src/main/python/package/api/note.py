import json
from uuid import uuid4

from package.api.constants import NOTES_DIR


def get_notes():
    notes = []
    for file in NOTES_DIR.glob("*.json"):
        with open(file, "r") as f:
            note_data = json.load(f)
            note_uuid = file.stem
            note_title = note_data.get("title")
            note_content = note_data.get("content")
            note = Note(uuid=note_uuid, title=note_title, content=note_content)
            notes.append(note)
    return notes


class Note:
    def __init__(self, title="", content="", uuid=None):
        if uuid:
            self.uuid = uuid
        else:
            self.uuid = str(uuid4())
        self.title = title
        self.content = content

    def __repr__(self):
        return f"{self.title} ({self.uuid})"

    def __str__(self):
        return self.title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, str):
            self._content = value
        else:
            raise TypeError("Valeur incorrecte (Seules les chaînes de caractères sont acceptées.)")

    def delete(self):
        self.path.unlink()
        if self.path.exists():
            return False
        return True

    @property
    def path(self):
        return NOTES_DIR / (self.uuid + ".json")

    def save(self):
        NOTES_DIR.mkdir(exist_ok=True, parents=True)
        data = {"title": self.title, "content": self.content}
        with open(self.path, "w", encoding="utf8") as f:
            json.dump(data, f, indent=4)


if __name__ == '__main__':
    pass
