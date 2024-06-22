import socket
import threading
import pickle

# Sample data for provider login credentials
provider_credentials = {
    "John": "password123",
    "David": "password123",
    "Michael": "password123",
    "Sophie": "password123",
    "Ethan": "password123",
    "Jacob": "password123",
    "Mike": "password123",
    "Emily": "password123",
    "Luke": "password123",
    "Emma": "password123",
    "Sophia_Painter": "password123",
    "Michael_Painter": "password123",
    "Ella": "password123",
    "Daniel_Driver": "password123",
    "Emma_Driver": "password123",
    "Daniel": "password123",
    "Olivia": "password123",
    "James_Electrician": "password123",
    "Harry": "password123"
}

client_requests = {}

def handle_client_connection(client_socket, address):
    print(f"Client {address} connected.")
    try:
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            message = pickle.loads(data)
            if message["type"] == "request":
                service_request = message["data"]
                provider = service_request["provider"]
                client_id = service_request["client_id"]
                print(f"Request from Client {client_id} for {provider}: {service_request}")

                if provider not in client_requests:
                    client_requests[provider] = []

                client_requests[provider].append((client_id, service_request))
                response = f"Request sent to provider {provider}."
                client_socket.send(pickle.dumps(response))

            elif message["type"] == "login":
                login_data = message["data"]
                provider_name = login_data["provider"]
                password = login_data["password"]

                if provider_name in provider_credentials and provider_credentials[provider_name] == password:
                    response = {"status": "success", "message": f"Welcome, {provider_name}!"}
                    client_socket.send(pickle.dumps(response))

                    threading.Thread(target=handle_provider_requests, args=(client_socket, provider_name)).start()
                else:
                    response = {"status": "failure", "message": "Invalid credentials."}
                    client_socket.send(pickle.dumps(response))

            elif message["type"] == "response":
                response_data = message["data"]
                request_info = response_data["request_info"]
                status = response_data["status"]
                print(f"Provider response: {status} - {request_info}")
                # Process provider response (e.g., send to client)
                # In a real application, we would locate the client socket and send the response

    except Exception as e:
        print(f"Error handling client {address}: {e}")
    finally:
        client_socket.close()
        print(f"Client {address} disconnected.")

def handle_provider_requests(provider_socket, provider_name):
    try:
        while True:
            if provider_name in client_requests and client_requests[provider_name]:
                client_id, service_request = client_requests[provider_name].pop(0)
                provider_socket.send(pickle.dumps(service_request))
    except Exception as e:
        print(f"Error handling provider {provider_name}: {e}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345")

    while True:
        client_socket, address = server_socket.accept()
        threading.Thread(target=handle_client_connection, args=(client_socket, address)).start()

if __name__ == "__main__":
    main()
