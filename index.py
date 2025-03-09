import requests
import json
import os

def gpt(auth_headers):

    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

    with open('body.json', 'r', encoding='utf-8') as f:
        data = json.dumps(json.load(f))
    resp = requests.post(url, headers=auth_headers, data=data)

    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                {resp.status_code}, {resp.text}
            )
        )

    return resp.text

if __name__ == "__main__":
    if os.getenv('IAM_TOKEN') is not None:
        iam_token = os.environ['IAM_TOKEN']
        headers = {
            'Authorization': f'Bearer {iam_token}',
        }
    elif os.getenv('API_KEY') is not None:
        api_key = os.environ['API_KEY']
        headers = {
            'Authorization': f'Api-Key {api_key}',
        }
    else:
        print ('Please save either an IAM token or an API key into a corresponding `IAM_TOKEN` or `API_KEY` environment variable.')
        exit()

    print(gpt(headers))