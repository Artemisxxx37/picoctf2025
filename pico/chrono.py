import random
import time
import socket

# Function to generate a random token based on a seed
def get_random(length, seed):
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    random.seed(seed)
    s = ""
    for i in range(length):
        s += random.choice(alphabet)
    return s

def generate_tokens(target_time, range_ms):
    tokens = []
    for delta in range(50, 100):
        seed = int(target_time * 1000) + delta
        token = get_random(20, seed)
        tokens.append(token)
    return tokens

def connect_and_submit_tokens(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    target_time = time.time()
    tokens = generate_tokens(target_time, range_ms=25) 
    data = s.recv(1024).decode() 
    print(data)  
    # Loop through each token and submit it
    for token in tokens:
        # Send the token to the server
        s.sendall((token + "\n").encode())

        # Receive the server's response
        response = s.recv(1024).decode().strip()
        print(f"Token: {token} -> Response: {response}")

        # Check if the response indicates success
        if "picoCTF{" in response:
            print("\nFlag found!")
            print(response)  # Print the flag
            break

    # Close the connection
    s.close()

# Main function
def main():
    # Server details
    host = "verbal-sleep.picoctf.net"
    port = 59848
    connect_and_submit_tokens(host, port)

if __name__ == "__main__":
    main()
