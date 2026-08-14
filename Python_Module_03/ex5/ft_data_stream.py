import typing
import random


players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "move"]


def gen_event() -> typing.Generator[tuple, None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(events: list) -> typing.Generator[tuple, None, None]:
    for _ in range(len(events)):
        rd_evt = random.choice(events)
        print(f"Got event from list: {rd_evt}")
        events.remove(rd_evt)
        print(f"Remains in list: {events}")
        yield rd_evt


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    evt_gen = gen_event()
    for i in range(1000):
        evt = next(evt_gen)
        print(f"Event {i}: Player {evt[0]} did action {evt[1]}")

    evt_10 = []
    for i in range(10):
        evt_10.append(next(evt_gen))
    print(f"Built list of 10 events: {evt_10}")

    cons_evt = consume_event(evt_10)
    for _ in range(len(evt_10)):
        pick_evt = next(cons_evt)
