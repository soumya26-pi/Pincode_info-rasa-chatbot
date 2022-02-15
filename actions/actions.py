# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json
api="https://api.postalpincode.in/pincode/"

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class apipindetails(Action):

    def name(self) -> Text:
        return "api_pin_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = []
        #print("tracker : ", tracker)
        for event in (list(tracker.events)):
            #print("Event : ",event)
            if event.get("event") == "user":
                messages.append(event.get("text"))
        print("Messages : ",messages)


        reg_no = messages[-2]
        api="https://api.postalpincode.in/pincode/"
        pin=str((tracker.latest_message)['text'])
        response=requests.get(api+pin)
        pin_info=json.loads(response.text)
        info=pin_info[0]['PostOffice'][0]
        state=info['State']
        print(info['District'])
        print(info['Block'])
        print(info['Division'])
        dispatcher.utter_message(text="Your state is")
        dispatcher.utter_message(text=state)
        return []
class apipindetails(Action):

    def name(self) -> Text:
        return "api_pin_dis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = []
        #print("tracker : ", tracker)
        for event in (list(tracker.events)):
            #print("Event : ",event)
            if event.get("event") == "user":
                messages.append(event.get("text"))
        print("Messages : ",messages)


        reg_no = messages[-2]
        api="https://api.postalpincode.in/pincode/"

        pin=str((tracker.latest_message)['text'])

        response=requests.get(api+pin)
        pin_info=json.loads(response.text)
        info=pin_info[0]['PostOffice'][0]
        state=info['State']
        dis=info['District']
        print(info['Block'])
        print(info['Division'])
        dispatcher.utter_message(text="Your district is")
        dispatcher.utter_message(text=dis)
        return []

class apipindetails(Action):

    def name(self) -> Text:
        return "api_pin_blk"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = []
        #print("tracker : ", tracker)
        for event in (list(tracker.events)):
            #print("Event : ",event)
            if event.get("event") == "user":
                messages.append(event.get("text"))
        print("Messages : ",messages)


        reg_no = messages[-2]
        api="https://api.postalpincode.in/pincode/"

        pin=str((tracker.latest_message)['text'])

        response=requests.get(api+pin)
        pin_info=json.loads(response.text)
        info=pin_info[0]['PostOffice'][0]
        state=info['State']
        dis=info['District']
        blk=info['Block']
        print(info['Division'])
        dispatcher.utter_message(text="Your Block is")
        dispatcher.utter_message(text=blk)
        return []

class apipindetails(Action):

    def name(self) -> Text:
        return "api_pin_div"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = []
        #print("tracker : ", tracker)
        for event in (list(tracker.events)):
            #print("Event : ",event)
            if event.get("event") == "user":
                messages.append(event.get("text"))
        print("Messages : ",messages)


        reg_no = messages[-2]
        api="https://api.postalpincode.in/pincode/"

        pin=str((tracker.latest_message)['text'])

        response=requests.get(api+pin)
        pin_info=json.loads(response.text)
        info=pin_info[0]['PostOffice'][0]
        state=info['State']
        dis=info['District']
        div=info['Division']
        dispatcher.utter_message(text="Your Division is")
        dispatcher.utter_message(text=div)
        return []


class apipindetails(Action):

    def name(self) -> Text:
        return "api_pin_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        messages = []
        #print("tracker : ", tracker)
        for event in (list(tracker.events)):
            #print("Event : ",event)
            if event.get("event") == "user":
                messages.append(event.get("text"))
        print("Messages : ",messages)


        reg_no = messages[-2]
        api="https://api.postalpincode.in/pincode/"

        pin=str((tracker.latest_message)['text'])

        response=requests.get(api+pin)
        pin_info=json.loads(response.text)
        info=pin_info[0]['PostOffice'][0]
        state=info['State']
        city=info['District']
        print(info['Block'])
        print(info['Division'])
        dispatcher.utter_message(text="Your city is")
        dispatcher.utter_message(text=city)
        return []