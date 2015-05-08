# random-giphy

Select randomly a gif on giphy, then copy the link in your clipboard.
For OSX only.

### Usage

```
usage: giphy.py [-h] [-r {y,g,pg,pg-13,r}] keywords [keywords ...]

Randomly find a gif that match the given keywords. See:
https://github.com/Giphy/GiphyAPI#translate-endpoint

positional arguments:
  keywords              The keyword(s) to translate into a gif.

optional arguments:
  -h, --help            show this help message and exit
  -r {y,g,pg,pg-13,r}, --rating {y,g,pg,pg-13,r}
                        Restrict the results to the given rating.
```

### Requirements

No requirement, but Python in v2.7
