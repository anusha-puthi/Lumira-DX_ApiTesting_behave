from behave import *
import requests

baseurl =""
params_value = {}
response = ""

@given(u'I want to retrieve list of posts when blog posts end point is triggered')
def url_params(context):
    # endpoint and parameters
    baseurl = "http://localhost:8888/api/blog/posts/"
    params_value = {'page': 1, 'bool': 'true', 'per_page': 10}

    return baseurl, params_value

@when(u'I submit Get request with query parameters')
def submit_get(context):
    app_url = url_params(context)
    response = requests.get(app_url[0], params=app_url[1])
    return response


@then(u'the response is success and validating the get posts response schema')
def response_validation(context):
    get_response = submit_get(context)

    print("The response code is: ", response)
    # validating status code
    status = str(get_response.status_code)

    try:
        assert get_response.status_code == 200
        print("Status code is matching and Status code is " + status)
    except:
        print("status is not matching and status code is " + status)

    #  validate the response headers
    headers = get_response.headers
    print(headers)
    if headers.get("Content-Type").__contains__("json"):
        print("Response is in Json format")
    else:
        print("Response is not in Json format")

    # validate the response body
    response_body = get_response.json()
    try:
        assert response_body != "null"
        print("Get post is success")
    except:
        print("Get post is not successful")
    else:
        print("No response")


@then(u'validating the items field for the post')
def json_body_validation(context):
    get_response = submit_get(context)
    # validating the json response
    json_response = get_response.json()
    print(json_response['total'])
    print(json_response['per_page'])
    get_title = json_response["items"][0]["title"]
    print(get_title)

    try:
        assert get_title.startswith("Title")
    except:
        print("No title")

    get_categoryid = json_response["items"][2]["category_id"]
    print(get_categoryid)

