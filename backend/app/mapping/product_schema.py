from marshmallow import Schema, fields

class ProductSchema(Schema):
    codigo = fields.Str(required=True)
    nombre = fields.Str(required=True)
    precio = fields.Float(required=True)
    imagen_url = fields.Str(allow_none=True)
    ultima_actualizacion = fields.Date(allow_none=True)

    def dump(self, obj, *args, **kwargs):
        # Si el objeto es un diccionario, lo devolvemos tal cual
        if isinstance(obj, dict):
            return obj
        return super().dump(obj, *args, **kwargs)

    @classmethod
    def dump_many(cls, obj_list, *args, **kwargs):
        # Si la lista contiene diccionarios, los devolvemos tal cual
        if obj_list and isinstance(obj_list[0], dict):
            return obj_list
        return super().dump_many(obj_list, *args, **kwargs)