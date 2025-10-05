#!/usr/bin/env python3

from pytm import TM, Server, Dataflow, Boundary, Actor

tm = TM("Web Application Threat Model")
tm.description = "Basic web application threat model"
tm.isOrdered = True

# Define boundaries
internet = Boundary("Internet")
web_dmz = Boundary("Web DMZ")

# Define actors
user = Actor("User")
user.inBoundary = internet

# Define assets
web_server = Server("Web Server")
web_server.inBoundary = web_dmz
web_server.OS = "Linux"
web_server.isHardened = False

# Define dataflows
user_to_web = Dataflow(user, web_server, "HTTP Request")
user_to_web.protocol = "HTTP"
user_to_web.dstPort = 80
user_to_web.data = "User credentials"

web_to_user = Dataflow(web_server, user, "HTTP Response")
web_to_user.protocol = "HTTP"

print("=== THREAT MODEL ANALYSIS ===")
print(f"Model: {tm.name}")
print(f"Description: {tm.description}")
print("\n=== COMPONENTS ===")
print(f"- {user.name} (Actor)")
print(f"- {web_server.name} (Server, OS: {web_server.OS})")
print("\n=== DATA FLOWS ===")
print(f"- {user_to_web.name}: {user_to_web.source.name} -> {user_to_web.sink.name}")
print(f"- {web_to_user.name}: {web_to_user.source.name} -> {web_to_user.sink.name}")

tm.process()