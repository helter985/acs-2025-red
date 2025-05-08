from marshmallow import Schema, fields

class ProductSchema(Schema):
    code = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    image_url = fields.Str(required=True)
    last_updated = fields.DateTime(dump_only=True)