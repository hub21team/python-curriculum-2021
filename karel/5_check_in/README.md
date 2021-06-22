# Concepts
- Comments
- Check-in exercises

# Teaching Tips
- Comments are an essential part of programming. Students should feel comfortable and they should be used to using comments to explain their code.

## Collect Rewards
Karel starts at the left end of the first row. Along her way, there are prizes, at each corner there may be multiple, disguised as beepers. Your job is to move Karel untill the end of the row and pick the prizes along her way.

## Hospital Karel
Karel begins at the left end of the first row. Her job is to build hospitals along her way to the end of the row. 
- Hospitals' starting locations are marked with a beeper. 
- The hospitals consist of six beefers, piled into two columns of three beepers. 
- Karel should complete the program at the end of the row facing East.
- Karel has infinite number of beepers in her bag.

## Build Ephesus
Let's repair thhe famous library in Ephesus, which looks like:
![Columns](ephesus.jpg)

Your program should work on the world shown above, but it should be general enough to handle any world that meets the basic conditions outlined at the end of this problem.

When Karel is done, the missing stones in the columns should be replaced by beepers, so that the final world has straight beepers in the place of columns.

Karel’s final location and the final direction Karel is facing at the end of the run do not matter. Karel may count on the following facts about the world:
- Karel starts at the corner where 1st Avenue and 1st Street meet, facing east, with an infinite number of beepers in Karel’s beeper bag. The first column should be built on 1st Avenue.
- The columns are always exactly four Avenues apart, so they would be built on 1st Avenue, 5th Avenue, 9th Avenue, and so on.
- The final column will always have a wall immediately after it. Although this wall appears after 13th Avenue in the example figure, your program should work for any number of beeper columns.
- The top of a beeper column will always be marked by a wall. However, Karel cannot assume that columns are always five units high, or even that all columns within a given world are the same height.
- In an initial world, some columns may already contain beepers representing stones that are still in place. Your program should not put a second beeper on corners that already have beepers. Avenues that will not have columns will never contain existing beepers.

Build Ephesus is adapted from Code in Place, and CS Bridge.
