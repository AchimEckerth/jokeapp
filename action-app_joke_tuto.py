from hermes_python.hermes import Hermes


def action_wrapper(hermes, intent_message):
    result_sentence = 'How are you'
    hermes.publish_end_session(intentMessage.session_id, result_sentence)


if __name__ == "__main__":
    with Hermes("localhost:1883") as h:
        h.subscribe_intent("snips-qOPRiLbJKW:askJoke", action_wrapper).start()