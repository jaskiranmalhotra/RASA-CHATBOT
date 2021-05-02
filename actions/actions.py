# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSeatsTable(Action):

    def name(self) -> Text:
        return "seats_table"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="How many seats would you like to reserve?")

        return []



class ActionAcNonAc(Action):

    def name(self) -> Text:
        return "ac_non_ac"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Which section would you like to book  AC or Non-AC")

        return []


class ActionAcTime(Action):

    def name(self) -> Text:
        return "ac_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="When would you like to book a reservation? (We are only open from 7pm to 10pm)")

        return []

class ActionTimming(Action):

    def name(self) -> Text:
        return "timming"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="You have reserved {numberofseats} in our {acnonac} section for {time} slot")

        return []


class ActionDailytime(Action):

    def name(self) -> Text:
        return "daily_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="We are only open from 7pm to 10pm")

        return []

