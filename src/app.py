from ai71 import AI71 
apikey="ai71-api-e829e1a8-0d13-4094-9920-ddb9153ab7bb"


client = AI71(apikey)

# Simple invocation
print(client.chat.completions.create(
        model="tiiuae/falcon-180B-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"},
        ],
    ))
