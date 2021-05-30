import requests as rq


def requests(trigger: str) -> None:
    response = rq.get(trigger)
    print(response.status_code)
    print(response.text)
