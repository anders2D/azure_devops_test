import os
import sqlite3
import pickle
import subprocess

# SQL Injection vulnerability
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

# Command Injection vulnerability
def ping_host(host):
    os.system("ping -c 1 " + host)

# Hardcoded credentials
API_KEY = "sk-1234567890abcdef"
PASSWORD = "admin123"

# Insecure deserialization
def load_data(data):
    return pickle.loads(data)

# Path traversal
def read_file(filename):
    with open("/var/data/" + filename, 'r') as f:
        return f.read()

# Weak cryptography
def hash_password(password):
    import hashlib
    return hashlib.md5(password.encode()).hexdigest()

# Shell injection
def run_command(cmd):
    subprocess.call("bash -c " + cmd, shell=True)
