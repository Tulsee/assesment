from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .gadget import Gadgets
from .political import Political
from user.models import User


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def index(request):
    user = get_object_or_404(User, email=request.user.email)
    print(user.subscription)
    if(user.subscription == 'GD'):
        data = Gadgets.get_data()
        return Response(data)
    if(user.subscription == 'PL'):
        data = Political.get_data()
        return Response(data)
