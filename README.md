# MuckRack-User-Downloader

This is a simple little python list that loops through muck rack and downloads a user's information.
This specifically was used to scrape one person's account. It will likely not work on other users but the code is simple such that someone with little experience in python and beautiful soup can pick it up.

## Caveats

* If you want to specifically get the html page from the user, then the script can very easily be modified to just get the whole webpage
* It doesn't work on any other users profile.
* It doesn't have any builtin `sleep` or `cfscrape`
* It requires a bit of effort on the user.
  * You must scroll down all the way on the user's muckrack page and then copy paste the html into `file.html`


## Execution

`python scrape.py`
