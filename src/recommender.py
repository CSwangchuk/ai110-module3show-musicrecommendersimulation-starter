import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        """Scores a song against the user using genre, mood, and energy closeness."""
        score = 0.0
        reasons: List[str] = []

        if song.genre == user.favorite_genre:
            score += 2.0
            reasons.append('genre match (+2.0)')

        if song.mood == user.favorite_mood:
            score += 1.0
            reasons.append('mood match (+1.0)')

        energy_points = 2.0 * (1 - abs(song.energy - user.target_energy))
        score += energy_points
        reasons.append(f'energy closeness (+{energy_points:.2f})')

        return (score, reasons)

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = [(song, self._score(user, song)[0]) for song in self.songs]
        ranked = sorted(scored, key=lambda item: item[1], reverse=True)
        return [song for song, _ in ranked[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = self._score(user, song)
        return ', '.join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Reads songs.csv and returns a list of song dictionaries with numeric fields converted to floats."""

    float_fields = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a song against user preferences using genre, mood, and energy closeness, returning the score and reasons."""
    score = 0.0
    reasons: List[str] = []

    if song['genre'] == user_prefs['favorite_genre']:
        score += 2.0
        reasons.append('genre match (+2.0)')
  
    if song['mood'] == user_prefs['favorite_mood']:
        score += 1.0
        reasons.append('mood match (+1.0)')
    

    energy_points = 2.0 * (1 - abs(song['energy'] - user_prefs['target_energy']))
    score += energy_points
    reasons.append(f'energy closeness (+{energy_points:.2f})')

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores every song against user preferences and returns the top k as (song, score, reasons) tuples, ranked highest first."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, reasons))

    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    return ranked[:k]
