try:
    raise ValueError("Just a test message")

except ValueError as e:
    print(e)

print("Reach me this time please")
