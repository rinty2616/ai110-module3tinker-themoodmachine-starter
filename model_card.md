# Model Card: Mood Machine

## 1. Model Overview

**Model type:** I tested both the rule-based model and the machine-learning (ML) model.

**Intended purpose:** The models classify short text messages into positive, negative, neutral, or mixed moods.

**How it works (brief):** The rule-based model looks for positive and negative words, handles some negations, and recognizes common emojis. The ML model learns patterns from labeled example posts and uses those patterns to predict the mood of new messages.

## 2. Data

**Dataset description:** My dataset contains 14 short posts in `SAMPLE_POSTS`, with corresponding labels in `TRUE_LABELS`. I expanded the word lists and included examples involving slang, emojis, negation, sarcasm, and mixed feelings.

**Labeling process:** I assigned labels based on the overall meaning and mood of each message. Some examples were difficult to label because they contained both positive and negative feelings. For example, "Feeling tired but kind of hopeful" expresses mixed emotions. Sarcastic messages can also be difficult to label.

**Important characteristics of my dataset:**
- Contains slang and emojis.
- Includes negation, such as "I am not happy."
- Includes sarcasm, such as "I absolutely love getting stuck in traffic."
- Contains mixed emotions and ambiguous messages.
- Includes neutral messages without clear emotional language.

**Possible issues with the dataset:** The dataset is small and may not represent the way different people express emotions. Some labels are subjective, and the models may learn patterns that do not work well on unfamiliar messages.

## 3. How the Rule-Based Model Works

**My scoring rules:** I expanded the positive and negative word lists. Positive words increase the score, while negative words decrease it. I added preprocessing to handle punctuation, repeated letters, and common emojis. I also added simple negation handling for phrases such as "not happy" and "not bad." The model predicts a mood based on the sentiment score and the positive and negative signals it detects.

**Strengths of this approach:** The rules are easy to understand, and the model works well for straightforward messages such as "I love my class" and "I am not happy." Its predictions can be explained by identifying the words and emojis that influenced them.

**Weaknesses of this approach:** The model can struggle with sarcasm, unfamiliar slang, and complex sentences. For example, "I absolutely love getting stuck in traffic" was predicted as mixed because the model detected both positive and negative words without fully understanding the sarcasm.

## 4. How the ML Model Works

**Features used:** The ML model uses text features created by the scikit-learn pipeline in `ml_experiments.py`. These features allow the model to learn patterns from the training messages. The exact feature representation depends on the implementation in the project code.

**Training data:** The model was trained using `SAMPLE_POSTS` and their corresponding `TRUE_LABELS` from `dataset.py`.

**Training behavior:** The ML model reported an accuracy of 1.00 on the dataset, while the rule-based model reported an accuracy of 0.86. I also tested new sentences interactively. The ML model predicted "I don't know" as negative, while the rule-based model predicted it as neutral.

**Strengths and weaknesses:** The ML model can learn patterns automatically from labeled examples. However, its high accuracy on this small dataset does not guarantee good predictions on new messages. It may learn misleading patterns or fail to understand context that is not represented in its training data.

## 5. Evaluation

**How I evaluated the models:** I ran `python main.py` to evaluate the rule-based model and `python ml_experiments.py` to evaluate the ML model. The rule-based model reported an accuracy of 0.86, and the ML model reported an accuracy of 1.00 on the dataset. I also tested both models with the same three interactive messages.

**Examples of