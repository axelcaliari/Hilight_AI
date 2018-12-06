import json

def handler(event, context):
  data = {
    'output': launch_hilight(event["pathParameters"]["website_name"])
  }
  return {'statusCode': 200,
    'body': json.dumps(data),
    'headers': {'Content-Type': 'application/json'}}


def launch_hilight(name):
    return "c'est partie on lance l'AI avec le parametre " + name