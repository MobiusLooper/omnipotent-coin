# omnipotent-coin

__Can you define an event, using solely the randomness of tosses of a fair coin, that has probability of `1/3`?__

I thought of this question a few months ago, and after a few days of the question being in the back of my mind, I came up with a solution. This code tries to generalise that solution for any probability that can be expressed as a fraction, `n/d`, where `d <= 1024`. This condition is merely to keep computations tractable. Parallelisation of the code could indeed unlock efficiency gains, but this is an early prototype.

Run by using installing requirements with
```bash
pip install -r requirements.txt
```
```bash
python run.py -n 1 -d 3 -e 100000
```
where `-n 1` denotes a numerator of 1, `-d 3` denotes a denominator of 3, and `-e 100000` instructs the code to run 100000 _episodes_. This last argument is optional and defaults to 10000.

After executing, you should see a `tqdm` progress bar showing progress of episodes, and then you should see something like
```
Result: 0.33535 from 100,000 episodes
```
