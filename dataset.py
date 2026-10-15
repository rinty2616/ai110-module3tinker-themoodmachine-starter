"""
Shared data for the Mood Machine lab.

Contains positive and negative words, example posts, and human labels.
"""

# Starter and additional positive words
POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "hopeful",
    "proud",
    "wonderful",
    "fantastic",
    "enjoy",
    "glad",
    "best",
    "nice",
]

# Starter and additional negative words
NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "exhausted",
    "disappointed",
    "worst",
    "annoying",
    "failed",
    "traffic",
    "😭",
    ":(",
]

# Example posts written like social media updates
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "Lowkey stressed but kind of proud of myself",
    "No cap, this is awesome!",
    "I missed the bus again :(",
    "I absolutely love getting stuck in traffic",
    "Just got home at 6 pm",
    "I'm fine, just exhausted",
    "This movie was not bad",
    "I failed the test 😂 but at least I studied hard",
]

# Human-assigned labels for each post above
TRUE_LABELS = [
    "positive",
    "negative",
    "mixed",
    "neutral",
    "positive",
    "negative",
    "mixed",
    "positive",
    "negative",
    "negative",
    "neutral",
    "mixed",
    "positive",
    "mixed",
]

# Keep the dataset and labels aligned
assert len(SAMPLE_POSTS) == len(TRUE_LABELS), (
    "SAMPLE_POSTS and TRUE_LABELS must have the same length!"
)
