#!/usr/bin/env python3
"""
Simple rule-based chatbot demo.

Run:
  python3 chatbot.py

Supports:
 - Keyword / regex-based rules
 - Named-group extraction (e.g. "my name is Alice")
 - A small test mode: python3 chatbot.py --test
"""
import re
import sys

# Rules: list of (pattern, response_template, optional_action)
# pattern: regex applied with re.IGNORECASE
# response_template: may include {name} or other named-group keys from regex
RULES = [
    (r"^(hi|hello|hey)\b", "Hello! What's your name?"),
    (r"my name is (?P<name>[A-Za-z]+)", "Nice to meet you, {name}! How can I help you today?"),
    (r"what is my name\??", "You told me your name is {name}.", "requires_name"),
    (r"(help|what can you do)\b", "I can greet you, remember your name, and answer simple FAQs. Try: 'my name is ...'"),
    (r"(bye|goodbye|see you)\b", "Goodbye!"),
    (r"thanks?|thank you", "You're welcome!"),
    (r"(time|what time is it)\b", "I don't have a clock in this demo, but you can check your system clock."),
]

DEFAULT_RESPONSE = "Sorry, I don't understand that. Try 'help'."

def get_response(user_text, context):
    user_text = user_text.strip()
    for rule in RULES:
        pattern, template = rule[0], rule[1]
        m = re.search(pattern, user_text, flags=re.IGNORECASE)
        if m:
            # If regex has named groups, update context
            groupdict = m.groupdict()
            if "name" in groupdict and groupdict["name"]:
                context["name"] = groupdict["name"].strip().title()
            # Some rules may require a known name
            if len(rule) >= 3 and rule[2] == "requires_name" and not context.get("name"):
                return "I don't know your name yet. Tell me: 'my name is <yourname>'"
            # Format the response with context and groupdict
            data = {}
            data.update(context)
            data.update(groupdict)
            try:
                return template.format(**data)
            except KeyError:
                return template
    return DEFAULT_RESPONSE

def repl():
    print("Rule-based chatbot (type 'exit' to quit).")
    context = {}
    try:
        while True:
            user = input("> ").strip()
            if not user:
                continue
            if user.lower() in ("exit", "quit"):
                print("Goodbye!")
                break
            resp = get_response(user, context)
            print(resp)
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

def run_tests():
    tests = [
        "hello",
        "my name is Shruti",
        "what is my name?",
        "what can you do",
        "thanks",
        "bye",
    ]
    print("Running test conversation...")
    context = {}
    for t in tests:
        print("User:", t)
        print("Bot: ", get_response(t, context))
    print("Test finished. Current context:", context)

if __name__ == "__main__":
    if "--test" in sys.argv:
        run_tests()
    else:
        repl()