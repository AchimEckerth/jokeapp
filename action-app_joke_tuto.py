from hermes_python.hermes import Hermes


def action_wrapper(hermes, intent_message):
    hermes.publish_end_session(current_session_id, "Lets go!")


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("snips-qOPRiLbJKW:askJoke", action_wrapper).start()