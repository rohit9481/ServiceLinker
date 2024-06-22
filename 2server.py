import socket
import pickle

professional_groups = {
    "Carpenter": {
        "John": {"phone": "+917859643201", "location": "vijay nagar", "available": True},
        "David": {"phone": "+918745612309", "location": "vijay nagar", "available": False},
        "Michael": {"phone": "+917263548190", "location": "vijay nagar", "available": True},
        "Sophie": {"phone": "+919876543210", "location": "kormangala", "available": True},
        "Emma": {"phone": "+918765432109", "location": "kormangala", "available": False},
        "Oliver": {"phone": "+919876543201", "location": "kormangala", "available": True},
        "Luke": {"phone": "+918765432109", "location": "indiranagar", "available": True},
        "William": {"phone": "+917263548190", "location": "indiranagar", "available": True},
        "Ethan": {"phone": "+917859643201", "location": "indiranagar", "available": True},
        "Jacob": {"phone": "+918765432109", "location": "whitefield", "available": False},
        "Sophia": {"phone": "+918745612309", "location": "whitefield", "available": True},
        "Emily": {"phone": "+919876543210", "location": "whitefield", "available": False},
        "Jack": {"phone": "+918765432109", "location": "electronic city", "available": False},
        "Daniel": {"phone": "+917263548190", "location": "electronic city", "available": True},
        "Ava": {"phone": "+917859643201", "location": "electronic city", "available": False},
        "Nathan": {"phone": "+918765432109", "location": "btm layout", "available": True},
        "Olivia": {"phone": "+917263548190", "location": "btm layout", "available": False},
        "Isabella": {"phone": "+919876543210", "location": "btm layout", "available": True},
        "Mia": {"phone": "+918765432109", "location": "hsr layout", "available": False},
        "Benjamin": {"phone": "+917859643201", "location": "hsr layout", "available": True},
        "Evelyn": {"phone": "+919876543210", "location": "hsr layout", "available": True},
    },
    "Plumber": {
        "Mike": {"phone": "+1122334455", "location": "vijay nagar", "available": True},
        "Emily": {"phone": "+9988776655", "location": "vijay nagar", "available": False},
        "Sophie": {"phone": "+1234567890", "location": "vijay nagar", "available": True},
        "Luke": {"phone": "+9988776655", "location": "kormangala", "available": True},
        "Emma": {"phone": "+1122334455", "location": "kormangala", "available": False},
        "Ethan": {"phone": "+1234567890", "location": "kormangala", "available": True},
        "Mia": {"phone": "+9988776655", "location": "indiranagar", "available": True},
        "Ava": {"phone": "+1122334455", "location": "indiranagar", "available": False},
        "Jacob": {"phone": "+1234567890", "location": "indiranagar", "available": True},
        "Sophia": {"phone": "+9988776655", "location": "whitefield", "available": False},
        "Daniel": {"phone": "+1122334455", "location": "whitefield", "available": True},
        "Emily": {"phone": "+1234567890", "location": "whitefield", "available": False},
        "Jack": {"phone": "+9988776655", "location": "electronic city", "available": True},
        "David": {"phone": "+1122334455", "location": "electronic city", "available": True},
        "Ava": {"phone": "+1234567890", "location": "electronic city", "available": False},
        "Nathan": {"phone": "+9988776655", "location": "btm layout", "available": True},
        "Olivia": {"phone": "+1122334455", "location": "btm layout", "available": False},
        "Isabella": {"phone": "+1234567890", "location": "btm layout", "available": False},
        "Mia": {"phone": "+9988776655", "location": "hsr layout", "available": False},
        "Benjamin": {"phone": "+1122334455", "location": "hsr layout", "available": True},
        "Evelyn": {"phone": "+1234567890", "location": "hsr layout", "available": False},
    },
    "Painter": {
        "Sophia": {"phone": "+123454321", "location": "whitefield", "available": True},
        "Michael": {"phone": "+987654321", "location": "whitefield", "available": True},
        "Ella": {"phone": "+1234567890", "location": "whitefield", "available": False},
        "James": {"phone": "+1987654321", "location": "kormangala", "available": True},
        "Grace": {"phone": "+1122334455", "location": "kormangala", "available": False},
        "William": {"phone": "+1234432121", "location": "kormangala", "available": True},
        "Evelyn": {"phone": "+1987654321", "location": "electronic city", "available": False},
        "Abigail": {"phone": "+1234987654", "location": "electronic city", "available": True},
        "Oliver": {"phone": "+1111111111", "location": "electronic city", "available": False},
        "Sophia": {"phone": "+123454321", "location": "vijay nagar", "available": True},
        "Michael": {"phone": "+987654321", "location": "vijay nagar", "available": True},
        "Ella": {"phone": "+1234567890", "location": "vijay nagar", "available": True},
        "James": {"phone": "+1987654321", "location": "indiranagar", "available": False},
        "Grace": {"phone": "+1122334455", "location": "indiranagar", "available": False},
        "William": {"phone": "+1234432121", "location": "indiranagar", "available": False},
        "Evelyn": {"phone": "+1987654321", "location": "kormangala", "available": False},
        "Abigail": {"phone": "+1234987654", "location": "kormangala", "available": False},
        "Oliver": {"phone": "+1111111111", "location": "kormangala", "available": False},
        "Sophia": {"phone": "+123454321", "location": "electronic city", "available": False},
        "Michael": {"phone": "+987654321", "location": "electronic city", "available": False},
        "Ella": {"phone": "+1234567890", "location": "electronic city", "available": False},
    },
    "Driver": {
        "Daniel": {"phone": "+1122334455", "location": "whitefield", "available": True},
        "Emma": {"phone": "+9988776655", "location": "whitefield", "available": True},
        "Oliver": {"phone": "+1234567890", "location": "whitefield", "available": False},
        "Isabella": {"phone": "+1987654321", "location": "kormangala", "available": True},
        "Jack": {"phone": "+1122334455", "location": "kormangala", "available": False},
        "Liam": {"phone": "+1234567890", "location": "kormangala", "available": False},
        "Sophia": {"phone": "+9988776655", "location": "electronic city", "available": True},
        "Charlotte": {"phone": "+1122334455", "location": "electronic city", "available": False},
        "Noah": {"phone": "+1234567890", "location": "electronic city", "available": True},
        "Daniel": {"phone": "+1122334455", "location": "vijay nagar", "available": False},
        "Emma": {"phone": "+9988776655", "location": "vijay nagar", "available": True},
        "Oliver": {"phone": "+1234567890", "location": "vijay nagar", "available": True},
        "Isabella": {"phone": "+1987654321", "location": "indiranagar", "available": False},
        "Jack": {"phone": "+1122334455", "location": "indiranagar", "available": True},
        "Liam": {"phone": "+1234567890", "location": "indiranagar", "available": True},
        "Sophia": {"phone": "+9988776655", "location": "whitefield", "available": False},
        "Charlotte": {"phone": "+1122334455", "location": "whitefield", "available": True},
        "Noah": {"phone": "+1234567890", "location": "whitefield", "available": True},
        "Daniel": {"phone": "+1122334455", "location": "electronic city", "available": False},
        "Emma": {"phone": "+9988776655", "location": "electronic city", "available": True},
        "Oliver": {"phone": "+1234567890", "location": "electronic city"}, "available": False,
    },
    "Electrician": {
        "Olivia": {"phone": "+123454321", "location": "whitefield", "available": False},
        "James": {"phone": "+987654321", "location": "whitefield", "available": True},
        "Harry": {"phone": "+1234567890", "location": "whitefield", "available": True},
        "Amelia": {"phone": "+1987654321", "location": "kormangala", "available": False},
        "William": {"phone": "+1122334455", "location": "kormangala", "available": False},
        "Benjamin": {"phone": "+1234432121", "location": "kormangala", "available": True},
        "Mason": {"phone": "+1987654321", "location": "electronic city", "available": False},
        "Elijah": {"phone": "+1234987654", "location": "electronic city", "available": False},
        "Oliver": {"phone": "+1111111111", "location": "electronic city", "available": True},
        "Harry": {"phone": "+1234567890", "location": "vijay nagar", "available": False},
        "Amelia": {"phone": "+1987654321", "location": "indiranagar", "available": False},
        "William": {"phone": "+1122334455", "location": "indiranagar", "available": True},
        "Benjamin": {"phone": "+1234432121", "location": "indiranagar", "available": False},
        "Mason": {"phone": "+1987654321", "location": "btm layout", "available": False},
        "Elijah": {"phone": "+1234987654", "location": "btm layout", "available": True},
        "Oliver": {"phone": "+1111111111", "location": "btm layout", "available": False},
        "Olivia": {"phone": "+1234567890", "location": "hsr layout", "available": False},
        "James": {"phone": "+987654321", "location": "hsr layout", "available": False},
        "Harry": {"phone": "+1234567890", "location": "hsr layout", "available": True},
    },
}

def find_providers(service_type, location):
    available_providers = {}
    not_available_providers = {}
    for provider, details in professional_groups.get(service_type, {}).items():
        if details['location'] == location:
            if details['available']:
                available_providers[provider] = details['phone']
            else:
                not_available_providers[provider] = details['phone']
    return available_providers, not_available_providers

def handle_client(client_socket):
    try:
        service_type = client_socket.recv(1024).decode()

        client_socket.send("LocationPermission".encode())
        location = client_socket.recv(1024).decode()

        available_providers, not_available_providers = find_providers(service_type, location)
        service_providers = {
            "Available": available_providers,
            "Not Available": not_available_providers
        }

        response = pickle.dumps(service_providers)
        client_socket.send(response)
    finally:
        client_socket.close()

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server listening on port", port)

    while True:
        client_socket, addr = server_socket.accept()
        handle_client(client_socket)

if __name__ == "__main__":
    main()
