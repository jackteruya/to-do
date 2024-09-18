import json


class ToDoJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            to_serialize = {
                "id": obj.id,
                "title": obj.title,
                "description": obj.description,
                "completed": obj.completed,
                "start_date": obj.start_date,
                "end_date": obj.end_date
            }
            return to_serialize
        except AttributeError:  # pragma: no cover
            return super().default(obj)