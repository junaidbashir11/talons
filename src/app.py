from ai71 import AI71 
apikey="apikey"


client = AI71(apikey)

# Simple invocation
print(client.chat.completions.create(
        model="tiiuae/falcon-180B-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"},
        ],
    ))
