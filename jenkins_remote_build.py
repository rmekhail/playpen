def request_build(token, tag, email):
    """Requests that jenkins build the job"""
    crumb_resp= requests.get('https://jenkins.com/crumbIssuer/api/json', auth=('sdm', token))
    crumb_json = json.loads(crumb_resp.text)

    headers = {
        crumb_json['crumbRequestField']: crumb_json['crumb'],
    }

    params = (
        ('token', 'foobar'),
        ('TAG', tag),
        ('REQUESTOR_EMAIL', email)
    )

    response = requests.post('https://jenkins.com/job/myamazingjob/buildWithParameters', headers=headers, params=params, auth=('sdm', token))

request_build('my_api_token', 'v1.3.105', 'me@mailserver.com')
