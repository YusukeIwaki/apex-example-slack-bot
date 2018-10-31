from main_router import router as app

def handle(event, context):
  method = event["httpMethod"]
  path = event["resource"]
  if method != "GET":
    print("Body", event["body"])
  result = app.handle("%s %s"%(method, path), event)
  print(result)
  return result
