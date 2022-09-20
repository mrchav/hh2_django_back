from django.http import JsonResponse, Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import viewsets, status, mixins
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from hh_main.models import TgmUser, KeyWords
from hh_main.serializers import TgmUserSerializer, UserKeyWordsSerializer


class UserView(mixins.CreateModelMixin,
               GenericViewSet):
    serializer_class = TgmUserSerializer

    queryset = TgmUser.objects.all()

    def post(self, request):
        serializer = TgmUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KeyWordsView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   RetrieveModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = UserKeyWordsSerializer


    def get_queryset(self):
        try:
            queryset = KeyWords.objects.get(pk=3)
            serializer = UserKeyWordsSerializer(queryset)
            # print
            return serializer.data

        except TgmUser.DoesNotExist:
            raise Http404

    def post(self, request):
        serializer = UserKeyWordsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #user_id =
        #user = TgmUser.objects.get(pk=req.query_params.get('user'))


    '''
    def get(self, request):
        #queryset = TgmUser.objects.get(pk=pk)

        queryset = self.get_object(3)
        #serializer = TgmUserSerializer(user)
        return Response('Test'
                        )
        #
        # print('222')
        # queryset = TgmUser.objects.get(pk=3)
        # serializer = TgmUserSerializer(queryset)
        # return JsonResponse(serializer.data)
        # #serializer = TgmUserSerializer(queryset, many=True)
    '''
    #
    # queryset = TgmUser.objects.filter(
    #         tgm_id=11111111,
    #         username='test_user',
    #          ).first()
