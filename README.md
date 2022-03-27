# Wiki follower
Follows the first link of a random wiki page until it hits a loop.

## Exclusions
The script excludes the following:
- Links that go to the same page
- Disambiguation links
- Meta wiki links, eg. Help and User pages.

## Interpretation
The data is dumped to the specififed file as a list of all loops, which each have their corresponding pages in. Each page is a link and the name of the page.
There is an interpreter in the repository that outputs the length of the longest list, the length of the shortest, the average length, the most common pages, the most common first pages (If there are any reapeats) and the most common ending pages.
