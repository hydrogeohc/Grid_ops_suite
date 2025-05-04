import requests

# Example SQL injection attack
payload = {
    "name": "attacker",
    "phone": "123'); DROP TABLE contacts;--"
}
response = requests.post('http://localhost:5001/contacts', json=payload)
print("Attack response:", response.text)

# Fetch contacts to see if table still exists
response = requests.get('http://localhost:5001/contacts')
print("Contacts after attack:", response.text)
