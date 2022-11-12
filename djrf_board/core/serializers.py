from rest_framework import serializers


class DynamicDepthModelSerializer(serializers.ModelSerializer):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    max_depth = 0
    try:
      # NOTE: limiting nested depth to 1 makes it less likely that 
      # you'll accidentally expose sensitive data by expanding items
      # nested inside items you've explicitly listed in `Meta.fields`
      max_depth = min(int(getattr(self.Meta, "max_depth")), 1)
    except (ValueError, AttributeError):
      pass
    depth = self.context.get("depth", 0)
    self.Meta.depth = depth if depth <= max_depth else max_depth
