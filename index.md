# CS4641_Project


Group 8

Abstract:
	The problem we are addressing is that there are no chess AI that play intuitively human moves. Current chess engines have been created to help find the best moves in any given position. The top chess AI’s in the world can easily beat any human player, but these chess AI often play counter-intuitive “engine moves” which are based on logic that doesn’t come naturally to humans playing the game. The effect of these moves can only be understood much later in the game. Our somewhat unique approach is to create and train a chess AI on chess grandmaster games so that our engine will play more intuitive “human moves.”

Introduction/Background:
	Current chess engines such as AlphaZero, Stockfish, and Leela Zero are far stronger than any human. These chess AI’s also play very counterintuitive moves and openings such as the Reti Opening and the Queen’s Indian Defense. These two factors paired together make training through playing these chess AI’s very difficult. Creating a strong chess AI that will play moves similar to that of a human would be vastly beneficial for people trying to learn chess, practice, and improve their skills. There have also been recent attempts at this with the introduction of the Maia Chess AI which is designed to specifically play “human moves.” 

Problem Definition:
Our training data (our inputs) will be a large amount of grandmaster games in the “PGN” file format and our output will be who won the game. This is not a MDP as there are multiple agents and multiple states. It is best modeled by a Markov game. Our problem cannot be defined as a deterministic MDP as the opponents of our engine can make any legal move in any given position. If we were to model chess as an MDP and use reinforcement learning, we would end up with an engine similar to AlphaZero or Leela Chess. Our testing data inputs will be human made moves against our engine, and the outputs will be the top 2 or three moves in a position from our engine. 

Methods:
The baseline we will be somewhat following is utilizing Markov games as a framework for reinforcement learning; however, we will not be training our engine against itself, but rather on training data consisting of a large amount of grandmaster games. We will have somewhat novel data as we will be selecting solely grandmaster (FIDE rating > 2500) games from the last 30 years. This is different from training on games from any online chess player greater than a certain rating, that may not be FIDE certified. This is also different from having the engine train against itself.

Metrics:
	We have a couple ideas for the metrics for our chess AI. Our first idea is to use k-fold cross validation where we test our algorithm on a part of our dataset that we didn’t use for training. However, we believe that this will be semi-accurate because it is not guaranteed that the move that a grandmaster makes is the correct move that our algorithm should make. Therefore, there might be some problems with accuracy. Another potential metric would be using Elo and comparing the AI against other players until we determine an accurate Elo rating for our chess AI. This would be accurate because we would have a good idea of how our algorithm compares against human people in the world. All of the respected chess AI’s are measured based on Elo and how they compare against professional chess players 

Potential Results:
	We expect our chess AI to reach a fairly strong ELO rating, however we don’t expect it to reach the level of other chess AI. We do expect our chess AI to play moves that are more intuitive to humans due to the training data we will be using. 

Conclusion:
	At the end of this project, we hope to gain knowledge in the power of chess AI to imitate human playing styles, and the power of AI in general to make human-like decisions. Additionally, we expect to learn how effective training a machine against human data is at fostering human-like decisions in AI. 

References: 

Littman, M. L. (2007). Markov games as a framework for multi-agent reinforcement learning. Brown University / Bellcore, 94. https://www2.cs.duke.edu/courses/spring07/cps296.3/littman94markov.pdf
Silver, D.,  Hubert, T., Schrittwieser, J., Antonoglou, I., Lai, M., Guez, A., Lanctot, M., Sifre, L., Kumaran, D., Graepel, T., Lillicrap, T., Simonyan, K., & Hassabis, D. (2017). Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm. arXiv:1712.01815v1. https://arxiv.org/abs/1712.01815

Schrittwieser, J., Antonoglou, I., Hubert, T., Simonyan, K., Sifre, L., Schmitt, S., Guez, A., Lockhart, E., Hassabis, D., Graepel, T., Lillicrap, T., & Silver, D. (2020). Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model. arXiv:1911.08265v2. https://arxiv.org/pdf/1911.08265.pdf

McIlroy-Young, Reid, et al. “Aligning Superhuman AI with Human Behavior.” Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery &amp; Data Mining, 2020, doi:10.1145/3394486.3403219. 
