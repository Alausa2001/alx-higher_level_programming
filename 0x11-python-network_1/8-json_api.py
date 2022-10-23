#!/usr/bin/python3
"""script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>"""


if __name__ == "__main__":
    import requests
    from sys import argv

    value = {'q': ''}
    if len(argv) > 1:
        value = {'q': argv[1]}
        response = requests.post('http://0.0.0.0:5000/search_user', value)
        content_type = response.headers.get('Content-Type')
        if content_type == 'application/json':
            dict_cnt = eval(response.content)
            if (dict_cnt) != {}:
                print('[{}] {}'.format(dict_cnt['id'], dict_cnt['name']))
            else:
                print('No result')
        else:
            print('Not a valid JSON')
    else:
        print('No result')
