import requests

def send_message(agent_id, message):
    url = f'http://agent-{agent_id}/api/messages'
    response = requests.post(url, json={'message': message})
    return response.json()

def receive_message():
    url = 'http://agent-self/api/messages'
    response = requests.get(url)
    return response.json()