import re

# --- SECURITY CONFIGURATION ---
# Common phrases used in Prompt Injection / Jailbreaking
BLACKSET_PHRASES = [
    "ignore all previous instructions",
    "forget everything you know",
    "system prompt",
    "developer mode",
    "you are now a",
    "act as a",
    "bypass",
    "jailbreak"
]

# Restricted topics to prevent the bot from talking about dangerous things
RESTRICTED_TOPICS = [
    "hack", "virus", "bomb", "kill", "drug", "illegal", "password", "credit card"
]

def check_input_safety(user_input):
    """
    Checks if the user input is safe or a prompt injection attempt.
    Returns: (is_safe: bool, message: str)
    """
    input_lower = user_input.lower()

    # 1. Check for Prompt Injection Phrases
    for phrase in BLACKSET_PHRASES:
        if phrase in input_lower:
            return False, "⚠️ Security Alert: Prompt injection attempt detected."

    # 2. Check for Restricted Content (Safety)
    for topic in RESTRICTED_TOPICS:
        if topic in input_lower:
            return False, "🚫 I'm sorry, I can only discuss school-related academic topics."

    # 3. Check for Length (Prevents Buffer Overflow style attacks)
    if len(user_input) > 500:
        return False, "📏 Message is too long. Please keep questions concise."

    return True, "Safe"

def check_output_safety(ai_response):
    """
    Checks if the AI is leaking any sensitive info or using bad language.
    """
    # Example: Check for PII (Personally Identifiable Information) like phone numbers
    phone_pattern = r'\b\d{10}\b'
    if re.search(phone_pattern, ai_response):
        return "🛡️ Response blocked: Contains sensitive contact information."
    
    return ai_response