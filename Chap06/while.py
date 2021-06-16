#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5


while pw != secret:
    count += 1
    if count > max_attempt: break
    pw = input(f"{count}: What's the secret word? ")
else:
    auth = True

print("Authorized" if auth else "You're not authorized")

# break will break all the way out of the loop and skip the else clause
# continue will shortcut the loop and will go back up to the test without finishing the body of the loop
