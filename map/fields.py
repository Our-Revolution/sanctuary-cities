from django.contrib.gis.db.models.fields import MultiPolygonField
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon, WKTWriter


class CachedMultiPolygonField(MultiPolygonField):

    def __init__(self, **kwargs):

        self.simplify = kwargs.pop('simplify', 0.0002)
        self.precision = kwargs.pop('precision', 8)
        self.field_name = kwargs.pop('field_name', None)

        kwargs['null'] = True
        kwargs['blank'] = True

        return super(CachedMultiPolygonField, self).__init__(**kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(CachedMultiPolygonField, self).deconstruct()
        
        if self.simplify != 0.0002:
            kwargs['simplify'] = self.simplify

        if self.precision != 8:
            kwargs['precision'] = self.precision

        if self.field_name != None:
            kwargs['field_name'] = self.field_name

        if 'null' in kwargs:
            del kwargs['null']

        if 'blank' in kwargs:
            del kwargs['blank']

        return name, path, args, kwargs

    def pre_save(self, model_instance, add):

        if not getattr(model_instance, self.attname):

            try:
                wkt_writer = WKTWriter(precision=self.precision)
                value = GEOSGeometry(wkt_writer.write(getattr(model_instance, self.field_name).simplify(self.simplify, preserve_topology=True)))
                if not isinstance(value, MultiPolygon):
                    value = MultiPolygon(value)
                setattr(model_instance, self.attname, value)
                return value
            except:
                pass

        return super(CachedMultiPolygonField, self).pre_save(model_instance, add)