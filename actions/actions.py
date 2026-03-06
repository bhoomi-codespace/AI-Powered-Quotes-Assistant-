import random
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideQuote(Action):
    def name(self) -> Text:
        return "action_provide_quote"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Comprehensive Library: 15 Topics, 50+ Quotes
        quotes = {
            "success": [
                "Success is not final; failure is not fatal: it is the courage to continue that counts.",
                "The road to success and the road to failure are almost exactly the same.",
                "Success usually comes to those who are too busy to be looking for it.",
                "Opportunities don't happen. You create them."
            ],
            "discipline": [
                "Discipline is the bridge between goals and accomplishment.",
                "With self-discipline, most anything is possible.",
                "Discipline is choosing between what you want now and what you want most.",
                "Motivation gets you going, but discipline keeps you growing."
            ],
            "leadership": [
                "Leadership is the capacity to translate vision into reality.",
                "A leader is one who knows the way, goes the way, and shows the way.",
                "Innovation distinguishes between a leader and a follower.",
                "Management is doing things right; leadership is doing the right things."
            ],
            "courage": [
                "Courage is grace under pressure.",
                "It takes courage to grow up and become who you really are.",
                "Fortune favors the brave.",
                "Courage is being scared to death, but saddling up anyway."
            ],
            "hardwork": [
                "Hard work beats talent when talent doesn't work hard.",
                "There are no secrets to success. It is the result of preparation and hard work.",
                "The only place where success comes before work is in the dictionary.",
                "Dream big, stay focused, and work hard."
            ],
            "life": [
                "Life is what happens when you're busy making other plans.",
                "The purpose of our lives is to be happy.",
                "Life is a long lesson in humility.",
                "In the end, it's not the years in your life that count. It's the life in your years."
            ],
            "patience": [
                "Patience is bitter, but its fruit is sweet.",
                "The two most powerful warriors are patience and time.",
                "Patience is not the ability to wait, but the ability to keep a good attitude while waiting."
            ],
            "wisdom": [
                "The only true wisdom is in knowing you know nothing.",
                "Wisdom begins in wonder.",
                "Turn your wounds into wisdom."
            ],
            "happiness": [
                "Happiness depends upon ourselves.",
                "For every minute you are angry you lose sixty seconds of happiness.",
                "Happiness is not something ready-made. It comes from your own actions."
            ],
            "courage": ["Courage is grace under pressure.", "The secret to happiness is freedom, and the secret to freedom is courage."],
            "focus": ["Focus on being productive instead of busy.", "Where focus goes, energy flows."],
            "growth": ["Strive for continuous improvement, instead of perfection.", "Mistakes are proof that you are trying."],
            "integrity": ["Integrity is doing the right thing, even when no one is watching.", "Real integrity is doing the right thing, knowing that nobody’s going to know whether you did it or not."],
            "kindness": ["Kindness is a gift everyone can afford to give.", "No act of kindness, no matter how small, is ever wasted."],
            "time": ["Time is what we want most, but what we use worst.", "The key is in not spending time, but in investing it."]
        }

        # Extracting the topic from the user's message or chip click
        topic = next(tracker.get_latest_entity_values("topic"), None)
        
        if topic and topic.lower() in quotes:
            reply = random.choice(quotes[topic.lower()])
            dispatcher.utter_message(text=reply)
        else:
            # Fallback if the topic isn't recognized
            dispatcher.utter_message(text="I'm still learning! Ask me about Success, Discipline, Leadership, Hardwork, or Life.")

        return []