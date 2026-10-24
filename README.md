# 🎵 Music Recommender Simulation

## Project Summary

I built a simple music recommendation system in Python. It compares songs with a user's favorite genre, favorite mood, and preferred energy level. The program scores all 15 songs in a CSV file, recommends the top five, and explains why each song was selected. I tested different user profiles to see how recommendations changed and experimented with the scoring weights.

## How The System Works

The system uses **content-based filtering**: it compares a user's stated preferences with song features, rather than using the listening habits of other users. Each song has information including genre, mood, energy, tempo, valence, danceability, and acousticness. This version scores songs using three features:

- **Genre match:** +2.0 points
- **Mood match:** +1.0 point
- **Energy similarity:** up to +1.0 point, calculated from how close a song's energy is to the preferred energy

The highest possible score is 4.0. The program loads the catalog, scores each song, sorts the results from highest to lowest, and displays the top five with explanations. It may over-favor genre because genre has the largest weight.

## Getting Started

From the project folder, create and activate a virtual environment on a Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the program:

```bash
python -m src.main
```

### Running Tests

```bash
python -m pytest -v
```

When I tested the project, both automated tests passed.

## Sample Recommendation Output

For a user who likes pop, happy music, and energy level 0.8, my program produced:

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

I tested three sets of preferences and compared their top five results.

### High-Energy Pop

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

### Chill Lofi

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

### Intense Rock

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

The results changed with the user preferences. High-Energy Pop ranked **Sunrise City** first, Chill Lofi ranked **Library Rain** first, and Intense Rock ranked **Storm Runner** first. High-Energy Pop and Intense Rock both prefer strong energy, but their different genres and moods led to different top recommendations. Chill Lofi favored gentler songs instead.

## Experiments You Tried

I changed the scoring weights to see what would happen when energy mattered more than genre:

| Feature | Original weight | Experimental weight |
| --- | ---: | ---: |
| Genre match | 2.0 | 1.0 |
| Mood match | 1.0 | 1.0 |
| Energy similarity | Up to 1.0 | Up to 2.0 |

For the **Intense Rock** profile, Storm Runner changed from **3.96** to **3.92**, Gym Hero from **1.98** to **2.96**, and Electric Dreams from **1.00** to **2.00**. The top three songs stayed in the same order, but the scores changed. For **Chill Lofi**, Spacewalk Thoughts moved above Focus Flow when energy became more important. This showed that changing feature weights can change rankings. I restored the original weights after the experiment.

## Limitations and Risks

The catalog has only 15 songs, so it cannot represent every genre or listening preference. Some genres have fewer songs than others. Because genre is worth more than mood, the system may create a **filter bubble** and overlook songs from other genres that a listener might enjoy. It does not use user listening history, likes, skips, lyrics, or all the available numerical song features. A larger, more balanced catalog and more user feedback could make the recommendations better.

## Reflection

I learned how recommender systems turn data and preferences into scores and ranked suggestions. I practiced reading a CSV file, writing Python functions, explaining scores, and testing results. AI tools helped me understand code and troubleshoot errors, but I ran the program and checked the recommendations myself.

What surprised me most was how changing a few scoring weights affected the results. I now understand better how music apps can influence what listeners discover, and why recommendation systems should consider bias and diversity. If I improved this project, I would add more songs and use feedback such as likes and skips.

Read the full [Model Card](model_card.md) for more details about the system, its evaluation, and its limitations.
