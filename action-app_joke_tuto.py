from hermes_python.hermes import Hermes


def action_wrapper(hermes, intent_message):
    result_sentence = 'Wie geht es dir?'
    hermes.publish_end_session(intent_message.session_id, result_sentence)

with Hermes("localhost:1883") as h:
    h.subscribe_intent("snips-qOPRiLbJKW:Hallo", action_wrapper).start()