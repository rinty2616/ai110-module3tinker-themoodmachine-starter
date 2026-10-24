# 🎵 Music Recommender Simulation

## Project Summary

I built a simple music recommendation system using Python. The program recommends songs based on a user's favorite genre, mood, and preferred energy level.

My system reads 15 songs from a CSV file, calculates a score for each song, and recommends the top 5 songs.

I also tested different user profiles and experimented with changing the scoring weights to understand how recommendations work.

## How The System Works

My music recommendation system compares each song with the user's music preferences.

The scoring rules are:

- Genre match: 2 points
- Mood match: 1 point
- Energy similarity: up to 1 point

The maximum score is 4 points.

The program calculates scores for all 15 songs and recommends the top 5 songs with the highest scores.

The main features used are genre, mood, and energy.

One limitation is that the system may favor certain genres and miss other songs the user might enjoy.

## Getting Started

### Setup

1. Create a virtual environment:

```bash
python3 -m venv .venv
```

2. Activate it on Mac:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the music recommender:

```bash
python -m src.main
```

### Running Tests

Run the tests using:

```bash
python -m pytest -v
```

I ran the tests successfully. Both automated tests passed.

## Sample Recommendation Output

The following results were generated using a Pop / Happy user profile with target energy 0.8.

```text
Top recommendations:

Sunrise City - Score: 3.98
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.98)

Gym Hero - Score: 2.87
Because: Genre match (+2.0), Energy similarity (+0.87)

Rooftop Lights - Score: 1.96
Because: Mood match (+1.0), Energy similarity (+0.96)

Electric Dreams - Score: 1.85
Because: Mood match (+1.0), Energy similarity (+0.85)

Night Drive Loop - Score: 0.95
Because: Energy similarity (+0.95)
```

## Evaluation: Three Music Profiles

I tested three different user profiles to see whether my system produces different recommendations.

### Profile 1: High-Energy Pop

```text
Sunrise City - Score: 3.92
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.92)

Gym Hero - Score: 2.97
Because: Genre match (+2.0), Energy similarity (+0.97)

Electric Dreams - Score: 1.95
Because: Mood match (+1.0), Energy similarity (+0.95)

Rooftop Lights - Score: 1.86
Because: Mood match (+1.0), Energy similarity (+0.86)

Storm Runner - Score: 0.99
Because: Energy similarity (+0.99)
```

### Profile 2: Chill Lofi

```text
Library Rain - Score: 3.95
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.95)

Midnight Coding - Score: 3.88
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.88)

Focus Flow - Score: 2.90
Because: Genre match (+2.0), Energy similarity (+0.90)

Spacewalk Thoughts - Score: 1.98
Because: Mood match (+1.0), Energy similarity (+0.98)

Coffee Shop Stories - Score: 0.93
Because: Energy similarity (+0.93)
```

### Profile 3: Intense Rock

```text
Storm Runner - Score: 3.96
Because: Genre match (+2.0), Mood match (+1.0), Energy similarity (+0.96)

Gym Hero - Score: 1.98
Because: Mood match (+1.0), Energy similarity (+0.98)

Electric Dreams - Score: 1.00
Because: Energy similarity (+1.00)

Sunrise City - Score: 0.87
Because: Energy similarity (+0.87)

Rooftop Lights - Score: 0.81
Because: Energy similarity (+0.81)
```

### Evaluation Findings

The three profiles produced different recommendations.

High-Energy Pop preferred Sunrise City, while Chill Lofi preferred Library Rain.

Intense Rock recommended Storm Runner first because it closely matched rock music, an intense mood, and high energy.

This showed that the algorithm responds to different user preferences.

## Experiments You Tried

I experimented with changing the importance of genre and energy.

Original weights:

- Genre: 2 points
- Mood: 1 point
- Energy: up to 1 point

Experimental weights:

- Genre: 1 point
- Mood: 1 point
- Energy: up to 2 points

After making these changes, the scores changed.

For the Intense Rock profile, Storm Runner changed from 3.96 to 3.92 points.

Gym Hero increased from 1.98 to 2.96 points.

For the Chill Lofi profile, Spacewalk Thoughts moved above Focus Flow because energy similarity became more important.

I learned that changing scoring weights can change the ranking and influence which songs are recommended.

After completing the experiment, I restored the original weights.

## Limitations and Risks

My recommendation system has some limitations.

1. The dataset contains only 15 songs, which limits music diversity.
2. Some genres have fewer songs than others.
3. The algorithm gives more importance to genre than mood.
4. It does not consider the user's listening history, likes, or skips.
5. The system may create a filter bubble by recommending similar music repeatedly.

A larger dataset and more user information could improve the recommendations.

## Reflection

During this project, I learned how a music recommendation system turns song data and user preferences into predictions. I learned how to load CSV data, calculate scores, rank songs, and display recommendations using Python.

AI tools helped me understand the code and fix programming errors. I also tested the program myself to confirm that it worked correctly.

One interesting thing I discovered was that changing just a few scoring weights could change the recommendations. This helped me understand how simple algorithms can affect what users see on real music platforms.

In the future, I would like to add more songs, include user listening history, and improve the recommendation system.

For more information about my project, see my [Model Card](model_card.md).