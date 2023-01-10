# GooCounter
Google Search Result Number Counter

# What it does
Takes a list of words and respective word occurence numbers in a corpus as input data

Searches for word on Google and reads the number of results

Outputs a file with a list of words, respective word occurences, and number of search results

Has some primitive forms of anti-bot protection, such as delays, custom user agent, etc

Integrates a paid anti-captcha service nopecha, but also allows for manual captcha solving

# How to use it
Edit settings in main.py, then run it

# Todo
Switch to a more reliable anti-captcha service

Forward data to Maja Hočevar for in-depth socio-linguistic analysis

# Far Todo
If lists need to be generated faster, employ parallelism and proxies
