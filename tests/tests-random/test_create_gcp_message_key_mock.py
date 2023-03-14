from uuid import uuid4

def create_message():
    payload = {
        "assignment_item_key": str(uuid4()),
        "status": "pending_alguma_coisa"
    }

    return payload

def create_mock_key_gcp(message_data: dict):
    message_data["message_key"] = str(uuid4())
    
    new_message_data = message_data

    return new_message_data

message = create_message()

new_message = create_mock_key_gcp(message)

print(new_message)
