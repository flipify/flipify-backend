from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET',])
def greet(request):
    """
    Greets the user with a message.
    The name is passed as a query parameter.
    """
    if request.method != 'GET':
        return Response(status=405)
    name = request.query_params.get('name', 'World')
    return Response({'message': f'Hello, {name}!'})

