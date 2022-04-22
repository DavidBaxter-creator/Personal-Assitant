import wikipedia
from Voice_engine import speak
from nlkt_run import query
import wolframalpha


def Search_up(filtered_speech):
    try:
        app_id = "PUT WOLFRAMALPHA API KEY HERE" # https://products.wolframalpha.com/api/
        client = wolframalpha.Client(app_id)
        res = client.query(filtered_speech)
        for pod in res.pods:
            for sub in pod.subpods:
                print(sub.plaintext)
        speak(next(res.results).text)
    except StopIteration as e:
        print('StopIteration Error handled successfully')
        pass

