import numpy as np
from tqdm import tqdm

from itertools import product
from fractions import Fraction

class Experiment:
    def __init__(self, probability: Fraction):
        assert probability.numerator > 0, "Numerator must be positive integer"
        assert (probability.denominator >= probability.numerator), "Denominator must be at least as large as the numerator"
        assert (probability.denominator <= 2**10), f"Denominator must be <= {2**10} so calculations are tractable"
        self._probability = probability
        self._setup_subsequences()

    def _setup_subsequences(self):
        self._subsequence_length = self._calculate_subsequence_length()
        self._generate_all_subsequences()
        self._continuation_subsequences = self._generate_continuation_subsequences()
        self._termination_subsequences = self._generate_termination_subsequences()
        self._success_subsequences = self._generate_success_subsequences()

    def _calculate_subsequence_length(self):
        powers_of_two = [2**n for n in range(100)]
        subsequence_length = 0
        while self._probability.denominator > powers_of_two[subsequence_length]:
            subsequence_length += 1
        return subsequence_length

    def _generate_all_subsequences(self):
        self._subsequences = list(product(*[[1, 0]] * self._subsequence_length))

    def _generate_continuation_subsequences(self):
        return self._subsequences[self._probability.denominator:]

    def _generate_termination_subsequences(self):
        return self._subsequences[:self._probability.denominator]

    def _generate_success_subsequences(self):
        num_success_subsequences = self._probability.numerator
        return self._subsequences[:num_success_subsequences]

    def _run_episode(self):
        self._sequence = []
        self._generate_new_subsequence()
        while tuple(self._sequence[-self._subsequence_length:]) in self._continuation_subsequences:
            self._generate_new_subsequence()
        success = (tuple(self._sequence[-self._subsequence_length:]) in self._success_subsequences)
        return success

    def _generate_new_subsequence(self):
        new_subsequence = np.random.choice([1, 0], size=self._subsequence_length)
        self._sequence.extend(new_subsequence)

    def run_experiment(self, num_episodes=10000):
        assert num_episodes > 0 and isinstance(num_episodes, int), 'You must enter a positive integer for num_episodes'
        results_sequence = []
        for _ in tqdm(range(num_episodes)):
            results_sequence.append(self._run_episode())
        num_successes = sum(results_sequence)
        return num_successes / num_episodes
