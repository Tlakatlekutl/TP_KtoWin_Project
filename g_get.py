from cgi import parse_qs, escape


def app(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])

    res_template = "{0}: {1} </br>"
    test_dict = {
        'a': 12,
        'b': 'hello',
    }
    response = "GET params: </br>"
    for key, value in d.items():
        response += res_template.format(escape(key), [escape(x) for x in value])

    start_response("200 OK", [
        ("Content-Type", "text/html"),
        ("Content-Length", str(len(response)))
    ])
    return [bytes(response, 'utf-8')]
