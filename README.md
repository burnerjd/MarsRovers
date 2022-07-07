# MarsRovers
Requires Python3.6 or above

Usage Example:
```
python3 MarsRovers.py MarsInput.txt
```

Can also be fed multiple input files

```
python3 MarsRovers.py MarsInput.txt MarsInput2.txt
```


## Short design decision justifications

- Task said an MxN grid, this is technically an (M+1)x(N+1) grid
  - Task also gave an example where robots were at 0 and at N without being lost
- Task didn't ask for multiple file support
  - It was a fairly simple add, and it allowed me to test a few more files a little easier
- Regex is a little confusing in code
  - It's also the best tool for the job here
- File input, not stdin
  - The example input looked a bit more like a file than an stdin
