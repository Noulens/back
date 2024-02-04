from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from uppy.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import (IsAuthenticated,
                                        IsAdminUser,
                                        DjangoModelPermissionsOrAnonReadOnly,
                                        DjangoModelPermissions,
                                        BasePermission, SAFE_METHODS,
                                        IsAuthenticatedOrReadOnly, )
from rest_framework.response import Response


class PostUserWritePermission(BasePermission):
    message = 'Editing files is restricted to the owner only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)

    def get_queryset(self):
        return Post.postobjects.all()



# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()
#
#     def list(self, request):
#         serializer = PostSerializer(self.queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)


# class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer


   # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

    # class PostList(viewsets.ModelViewSet):
    #     permission_classes = [IsAuthenticated]
    #     queryset = Post.postobjects.all()
    #     serializer_class = PostSerializer

    # class PostDetail(viewsets.ModelViewSet, PostUserWritePermission):
    #     permission_classes = [PostUserWritePermission]
    #     queryset = Post.objects.all()
    #     serializer_class = PostSerializer

""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""