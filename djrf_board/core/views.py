from rest_framework import generics, viewsets, mixins


class DynamicDepthView(generics.GenericAPIView):
  def get_serializer_context(self):
    context = super().get_serializer_context()
    try:
      context["depth"] = int(self.request.query_params.get("depth", 0))
    except ValueError:
      # ignore non-numeric params and keep default 0 depth
      pass
    return context


class DynamicDepthGenericViewSet(viewsets.GenericViewSet):
  def get_serializer_context(self):
    context = super().get_serializer_context()
    try:
      context["depth"] = int(self.request.query_params.get("depth", 0))
    except ValueError:
      # ignore non-numeric params and keep default 0 depth
      pass
    return context


class DynamicDepthModelViewSet(
  viewsets.ModelViewSet,
  DynamicDepthGenericViewSet
):
  pass


class DynamicDepthReadOnlyModelViewSet(
  viewsets.ReadOnlyModelViewSet,
  DynamicDepthGenericViewSet
):
  pass
