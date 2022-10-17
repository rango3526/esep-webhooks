import http.client

def lambda_handler(event, context):
    issue_url = event["issue"]["html_url"]
    payload = '{"text":"Issue created: ' + issue_url + '"}'

    client = http.client.HTTPSConnection("hooks.slack.com")
    client.request("POST", "fake_url", payload)
    response = client.getresponse()

    return response.read()

# if __name__ == "__main__":
#     event = {
#         "issue": {
#             "html_url": "www.FakeUrl.com"
#         }
#     }
#     context = {}
#     print("Before")
#     print(function_handler(event, context))
#     print("After")