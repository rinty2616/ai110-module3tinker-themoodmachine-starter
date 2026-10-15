"""
Rule-based mood analyzer for short text snippets.

Improvements:
- Preprocess punctuation, repeated letters, and common emojis.
- Count positive and negative words.
- Handle simple negation, such as "not happy" and "not bad".
- Predict positive, negative, neutral, or mixed.
- Explain the prediction.
"""

import re
from typing import List, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """A simple, rule-based mood classifier."""

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        positive_words = (
            positive_words if positive_words is not None else POSITIVE_WORDS
        )
        negative_words = (
            negative_words if negative_words is not None else NEGATIVE_WORDS
        )

        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    def preprocess(self, text: str) -> List[str]:
        """Normalize text, punctuation, and common emojis."""
        cleaned = text.strip().lower()

        # Convert common emoticons and emojis into readable tokens.
        replacements = {
            ":-)": " smileemoji ",
            ":)": " smileemoji ",
            ":-(": " sademoji ",
            ":(": " sademoji ",
            "😂": " laughemoji ",
            "😭": " cryemoji ",
            "🥲": " mixedemoji ",
            "💀": " deademoji ",
        }

        for symbol, word in replacements.items():
            cleaned = cleaned.replace(symbol, word)

        # Reduce repeated characters: "soooo" becomes "soo".
        cleaned = re.sub(r"(.)\1{2,}", r"\1\1", cleaned)

        # Remove punctuation while keeping apostrophes in contractions.
        cleaned = re.sub(r"[^\w\s']", " ", cleaned)

        return cleaned.split()

    def _analyze(self, text: str):
        """Count sentiment signals and calculate a score."""
        tokens = self.preprocess(text)

        positive_hits = []
        negative_hits = []
        score = 0

        negations = {"not", "never", "no", "isn't", "wasn't", "don't", "didn't"}

        for i, token in enumerate(tokens):
            # Handle common emojis.
            if token in {"smileemoji", "laughemoji"}:
                positive_hits.append(token)
                score += 1
                continue

            if token in {"sademoji", "cryemoji"}:
                negative_hits.append(token)
                score -= 1
                continue

            if token == "deademoji":
                # This emoji can mean laughter, shock, or distress.
                continue

            if token == "mixedemoji":
                positive_hits.append(token)
                negative_hits.append(token)
                continue

            is_positive = token in self.positive_words
            is_negative = token in self.negative_words

            if not is_positive and not is_negative:
                continue

            # Reverse the sentiment when preceded by a simple negation.
            previous_tokens = tokens[max(0, i - 2):i]
            negated = any(word in negations for word in previous_tokens)

            if is_positive:
                if negated:
                    negative_hits.append(token)
                    score -= 1
                else:
                    positive_hits.append(token)
                    score += 1

            if is_negative:
                if negated:
                    positive_hits.append(token)
                    score += 1
                else:
                    negative_hits.append(token)
                    score -= 1

        return score, positive_hits, negative_hits

    def score_text(self, text: str) -> int:
        """Return the total sentiment score."""
        score, _, _ = self._analyze(text)
        return score

    def predict_label(self, text: str) -> str:
        """Predict positive, negative, neutral, or mixed sentiment."""
        score, positive_hits, negative_hits = self._analyze(text)

        if positive_hits and negative_hits:
            return "mixed"

        if score > 0:
            return "positive"

        if score < 0:
            return "negative"

        return "neutral"

    def explain(self, text: str) -> str:
        """Explain which words influenced the prediction."""
        score, positive_hits, negative_hits = self._analyze(text)
        label = self.predict_label(text)

        return (
            f"Prediction = {label}; Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
