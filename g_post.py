from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
   <form method="post" action="">
        <p>
           Age: <input type="text" name="age">
        </p>
        <p>
            <input type="submit" value="Submit">
        </p>
    </form>
"""


def app(environ, start_response):

    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    response = html
    res_template = "{0}: {1} </br>"

    response += "POST params: </br>"
    for key, value in d.items():
        response += res_template.format(key, value)

    response += "</body> </html>"
    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response)))
    ])
    return [bytes(response, 'utf-8')]
