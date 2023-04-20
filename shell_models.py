from initial_data import Position, PositionSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

json_str = """{
    "position": 
        "name": "Developer",
        "department": "Development"
    }"""

stream = io.BytesIO(json_str)
data = JSONParser().parse(stream)

serializer = PositionSerializer(data= data)
serializer.is_valid()
print(serializer.errors)
print(serializer.validated_data)