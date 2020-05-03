# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import paho.mqtt.client as mqtt
broker="103.19.250.241"
port=1883

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from firebase import firebase
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


firebase = firebase.FirebaseApplication('https://raspberrypi-1e7c2.firebaseio.com/', None)
result = firebase.get('/room1', None)
print (result)

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to skill"
       

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
)
        
        
#main code for controlling fan
class fanOnIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("fanOnIntent")(handler_input)
    def handle(self,handler_input):
        
        if (res["Fan_1"]==0):
            speak_output ="Fan is on allready"
        else:
            client = mqtt.Client()
            client.connect("103.19.250.241",1883,60)
            client.publish("room1/Fan_1", "0");
            speak_output='fan on '
            firebase.put("/room1","Fan_1",0)
            print("recoed updated")
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
class fanOfIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("fanOfIntent")(handler_input)
    def handle(self,handler_input):
        if (result["Fan_1"]==1):
            speak_output= "Fan is of"
        else:
            
            client = mqtt.Client()
            client.connect("103.19.250.241",1883,60)
            client.publish("room1/Fan_1", "1");
            speak_output= "fan of"
            firebase.put("/room1","Fan_1",1)
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
            
#code for contolling light 1
class LightOneOnIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("LightOneOnIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Corner_Light_1", "0");
        
       
        speak_output= "Light  1 on"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
class LightOneOfIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("LightOneOfIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Corner_Light_1", "1");
        
       
        speak_output= "Light  1 of"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
            
#code for contolling light 2
class LightTwoOnIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("LightTwoOnIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Corner_Light_2", "0");
        
       
        speak_output= "Light  2 on"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
class LightTwoOfIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("LightTwoOfIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Corner_Light_2", "1");
        
       
        speak_output= "Light  2 of"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
#code for controlling Garden_Light
class GardenLightOnIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("GardenLightOnIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Garden_Light", "0");
        
       
        speak_output= "Garden  Light  on"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
class GardenLightOfIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("GardenLightOfIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Garden_Light", "1");
        
       
        speak_output= "Garden light  of"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
#code for controlling Wall_Plug

class WallPlugOnIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("WallPlugOnIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Wall_Plug", "0");
        
       
        speak_output= "Wall Plug  on"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
class WallPlugOfIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("WallPlugOfIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Wall_Plug", "1");
        
       
        speak_output= "Wall Plug  of"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
#code for controlling led 1

class YellowLedOneOnIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("YellowLedOneOnIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Yellow_Led_1", "0");
        
       
        speak_output= "Led 1  on"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
class YellowLedOneOfIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("YellowLedOneOfIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Yellow_Led_1", "1");
        
       
        speak_output= "Led 1  of"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
            
#code for controlling led 2

class YellowLedTwoOnIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("YellowLedTwoOnIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Yellow_Led_2", "0");
        
       
        speak_output= "Led 2  on"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            )
class YellowLedTwoOfIntent(AbstractRequestHandler):
    def can_handle(self,handler_input):
        return ask_utils.is_intent_name("YellowLedTwoOfIntent")(handler_input)
    def handle(self,handler_input):
        client = mqtt.Client()
        client.connect("103.19.250.241",1883,60)
        client.publish("room1/Yellow_Led_2", "1");
        
       
        speak_output= "Led 2  of"
        return(
            handler_input.response_builder
            .speak(speak_output)
            .response
            
class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
       
        speak_output = "Hello World!"

        return (
          
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(fanOnIntent())
sb.add_request_handler(fanOfIntent())
sb.add_request_handler(LightOneOnIntent())
sb.add_request_handler(LightOneOfIntent())
sb.add_request_handler(LightTwoOnIntent())
sb.add_request_handler(LightTwoOfIntent())
sb.add_request_handler(GardenLightOnIntent())
sb.add_request_handler(GardenLightOfIntent())
sb.add_request_handler(YellowLedOneOfIntent())
sb.add_request_handler(YellowLedOneOnIntent())
sb.add_request_handler(YellowLedTwoOnIntent())
sd.add_request_handler(YellowLedTwoOfIntent())
sb.add_request_handler(WallPlugOnIntent())
sb.add_request_handler(WallPlugOfIntent())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()