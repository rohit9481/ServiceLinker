import socket
import pickle
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # type: ignore

def request_service_providers(service_type, location):
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send the requested service type to the server
    client_socket.send(service_type.encode())

    # Receive permission request for location
    permission_request = client_socket.recv(1024).decode()
    if permission_request == "LocationPermission":
        # Send the location to the server
        client_socket.send(location.encode())

        # Receive the list of service providers from the server
        response = client_socket.recv(4096)
        service_providers = pickle.loads(response)

        # Close the client socket
        client_socket.close()

        return service_providers

def search_service_providers():
    service_type = service_var.get()
    location = location_var.get()

    # Request the list of service providers for the specified service type and location
    service_providers = request_service_providers(service_type, location)

    if service_providers:
        available_providers = service_providers["Available"]
        not_available_providers = service_providers["Not Available"]

        # Clear previous selections
        available_list.delete(0, 'end')
        not_available_list.delete(0, 'end')

        # Populate the available list
        for provider, phone in available_providers.items():
            available_list.insert('end', f"{provider} - {phone}")

        # Populate the not available list
        for provider, reason in not_available_providers.items():
            not_available_list.insert('end', f"{provider} - {reason}")

    else:
        messagebox.showerror("Service Not Found", "No service providers found for {} in {}".format(service_type, location))

def resize_background(event):
    new_width = event.width
    new_height = event.height
    resized_image = bg_image.resize((new_width, new_height), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(resized_image)
    bg_label.config(image=bg_photo)
    bg_label.image = bg_photo

# GUI setup
root = tk.Tk()
root.title("Service Provider Search")
root.geometry("800x600")

# Load the background image
bg_image = Image.open("bg5.jpg")

# Create a background label
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Bind the resize event
root.bind('<Configure>', resize_background)

# Create a central frame
central_frame = ttk.Frame(root, padding=20, relief="solid", borderwidth=2)
central_frame.place(relx=0.5, rely=0.5, anchor="center")

# Style the central frame and other widgets
style = ttk.Style()
style.theme_use("clam")
style.configure('TFrame', background='#2e3f4f')
style.configure('TButton', background='#6c757d', foreground='white', font=('Helvetica', 12), padding=10)
style.map('TButton', background=[('active', '#5a6268')])
style.configure('TLabel', background='#2e3f4f', foreground='white', font=('Helvetica', 12), padding=10)

# Title label
title_label = ttk.Label(central_frame, text="Service Provider Search", font=('Helvetica', 18, 'bold'))
title_label.pack(pady=10)

# Service type label and dropdown
service_label = ttk.Label(central_frame, text="Select service type:")
service_label.pack(pady=5)

service_var = tk.StringVar()
service_menu = ttk.Combobox(central_frame, textvariable=service_var)
service_menu['values'] = ["Carpenter", "Plumber", "Painter", "Driver", "Electrician"]
service_menu.pack(pady=5)

# Location label and entry
location_label = ttk.Label(central_frame, text="Enter location:")
location_label.pack(pady=5)

location_var = tk.StringVar()
location_entry = ttk.Entry(central_frame, textvariable=location_var)
location_entry.pack(pady=5)

# Search button
search_button = ttk.Button(central_frame, text="Search Service Providers", command=search_service_providers)
search_button.pack(pady=20)

# Available service providers list
available_label = ttk.Label(central_frame, text="Available Service Providers:")
available_label.pack(pady=10)

available_list = tk.Listbox(central_frame, width=50, height=5)
available_list.pack(pady=5)

# Not available service providers list
not_available_label = ttk.Label(central_frame, text="Not Available Service Providers:")
not_available_label.pack(pady=10)

not_available_list = tk.Listbox(central_frame, width=50, height=5)
not_available_list.pack(pady=5)

root.mainloop()
