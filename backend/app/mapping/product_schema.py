from marshmallow import Schema, fields

class ProductSchema(Schema):
    codigo = fields.Str(required=True)
    nombre = fields.Str(required=True)
    precio = fields.Float(required=True)
    imagen_url = fields.Str()
    ultima_actualizacion = fields.Date()