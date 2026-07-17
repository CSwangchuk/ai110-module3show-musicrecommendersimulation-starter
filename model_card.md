# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0** 
MusicTaster v1 

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

MusicTaster v1 is a simple music recommendation system designed to recommend songs based on a user's preferences. It is intended for classroom exploration to demonstrate how recommender systems work rather than for real-world music streaming services.

The model assumes that users know their preferred genres, moods, and energy levels. It recommends songs that most closely match those preferences using information stored about each song.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The recommender compares a user's preferences with the genre, mood, and energy of every song in the catalog. Each user profile stores a favorite genre, a favorite mood, and a target energy level (a number between 0.0 and 1.0).
The model scores each song by adding points: a song earns +2.0 points if its genre matches the user's favorite genre, and +1.0 point if its mood matches the user's favorite mood. Energy isn't a simple yes/no match — instead, the closer a song's energy is to the user's target, the more points it earns, up to a maximum of 2.0. This means a song doesn't need to match every feature perfectly to score well; a song with the right energy but the wrong genre can still rank reasonably high.
Compared to the starter version, I weighted genre and energy equally (2.0 points each), with mood weighted lower (1.0 point), since I felt genre and overall "vibe" (energy) matter more to how a recommendation feels right than mood alone.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset contains 20 songs. It originally started with 10 songs, and I expanded it by adding 10 more songs to increase the variety of recommendations.
The songs represent a range of genres, including pop, indie pop, rock, hip-hop, jazz, classical, lo-fi, ambient, synthwave, metal, soul, and indie folk. The dataset also includes different moods such as happy, chill, energetic, relaxed, intense, melancholic, aggressive, and romantic.
I added 10 new songs to expand the dataset but did not remove any existing songs.
Although the dataset covers several genres and moods, it is still limited compared to real music libraries. It cannot capture things like a listener's favorite artists, lyrics, cultural background, listening history, or songs that fit into multiple genres. For example, because genres are stored as exact text labels, a song labeled "indie pop" is treated differently from "pop," even though they are closely related. This limitation can cause the recommender to miss songs that a person would probably enjoy.
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  
A limitation appeared during the Deep Intense Rock test. Gym Hero (pop, intense, 0.93 energy) became the #2 recommendation, ranking above all other songs except Storm Runner, even though it did not match the rock genre.

This result was caused by a tradeoff in the model design: genre and energy were intentionally given equal importance because some users may care more about a song’s vibe than its exact genre label. However, this means highly energetic songs from different genres can sometimes outrank songs that better match the requested genre.

A possible improvement would be adding a diversity or mismatch penalty so the model can still consider energy while preventing songs with major genre differences from dominating recommendations.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I evaluated the recommender by testing three different user profiles: High-Energy Pop, Chill Lofi, and Deep Intense Rock. I checked whether the top recommendations matched the user's selected genre, mood, and energy preferences.

The results showed that the system performed well when songs matched all three features. For example, Sunrise City, Library Rain, and Storm Runner ranked highly because they closely matched their intended profiles. However, I also discovered an unexpected result with Gym Hero, which ranked #2 in the Deep Intense Rock test despite being a pop song.

To investigate this result, I ran an additional experiment by removing mood from the scoring system. Gym Hero's score decreased, but it still ranked above other non-matching songs. This showed that energy was the biggest factor allowing it to score highly, revealing the tradeoff between recommending songs based on overall vibe versus exact genre preference
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  
In the future, I would improve the recommender by using additional song features such as valence, danceability, and acousticness to capture more details about a user's musical preferences and better distinguish between songs with similar genres.

I would also improve the explanation system by making the recommendation reasons easier to understand. Instead of only showing scores like "energy closeness (+1.98)," the system could explain it in plain language, such as "this song's energy level is very close to what you requested."

Another improvement would be adding a diversity or mismatch penalty to prevent songs that only match one feature, such as energy, from ranking too highly when they do not fit the user's preferred genre. This would create a better balance between matching a user's vibe and their specific preferences.

Finally, I would make genre matching more flexible by using partial or fuzzy matching instead of exact matches. For example, "indie pop" and "pop" could receive partial credit rather than being treated as completely different genres. This would better reflect how people naturally group and experience music.
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

Working on this project helped me understand that even a simple recommendation system involves many design decisions and tradeoffs. My biggest learning moment was seeing how changing the scoring weights could affect recommendations in unexpected ways. The Gym Hero result showed me that a song can rank highly by matching a user's energy and mood, even if it does not match the exact genre they requested.

AI tools helped me brainstorm ideas, debug problems, and think through improvements, but I still had to verify the results myself. For example, I had to catch issues like missing imports and make sure the scoring behavior matched my intended design instead of assuming the model was working correctly.

I was surprised that a relatively simple algorithm could still produce recommendations that felt personalized. Matching just a few features like genre, mood, and energy was enough to create noticeable differences between user profiles. This showed me that recommendation systems are not only about complex models but also about choosing the right features and balancing different preferences.

If I continued this project, I would experiment with more advanced matching methods, larger datasets, and user feedback to make recommendations more accurate and personalized.
