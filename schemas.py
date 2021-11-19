from marshmallow import Schema, fields


class MessageSchema(Schema):
    """Объект входящего сообщения на сервер."""
    number = fields.Str()
    id = fields.Str()
    time = fields.Str()
    group = fields.Str()
