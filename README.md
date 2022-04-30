# advent-of-code-2020
My solutions for advent of code 2020

I've used Python3 to solve the problems. As a previous non-pythonista, there might be a lot of improvement on the code or it might not be very idiomatic.

All solutions should run relatively fast (in a few seconds) with the exceptions of some days listed below (I list the times taken on my machine). I also list some observations / considerations I had used in some days:
- 14 - part 2 uses the fact that the number of bits is small (there is a harder input)
- 15 - part 2 takes about 40s (bad choice of python for 3e7 operations)
- 19 - part 1 takes about 25s, part 2 takes about 33s, had to remove quotes from "a" and "b" in input
- 23 - part 2 takes about 30s (1e7 operations)

CPU info
Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz

## running

I've run the codes using `Python 3.6.1`, usually the output is the problem answer (no extra work or observation is necessary) e.g.

`python3 part_one.py`
