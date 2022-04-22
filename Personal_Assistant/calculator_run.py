import wolframalpha
from Voice_engine import speak


def calculator(filtered_speech):
    app_id = "PUT WOLFRAMAPLHA API HERE" # https://products.wolframalpha.com/api/
    client = wolframalpha.Client(app_id)
    res = client.query(filtered_speech)
    answer = next(res.results).text
    print(answer)
    speak(answer)


















