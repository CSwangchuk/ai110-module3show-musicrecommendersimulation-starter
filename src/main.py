"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Example profiles to test
    high_energy_pop = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.8}
    chill_lofi = {"favorite_genre": "lofi", "favorite_mood": "chill", "target_energy": 0.2}
    deep_intense_rock = {"favorite_genre": "rock", "favorite_mood": "intense", "target_energy": 0.9}

    profiles = {
        "High-Energy Pop": high_energy_pop,
        "Chill Lofi": chill_lofi,
        "Deep Intense Rock": deep_intense_rock,
    }

    for name, profile in profiles.items():
        print(f"\n=== {name} ===\n")
        recommendations = recommend_songs(profile, songs, k=5)
        for rec in recommendations:
            # You decide the structure of each returned item.
            # A common pattern is: (song, score, explanation)
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {', '.join(explanation)}")
            print()


if __name__ == "__main__":
    main()
