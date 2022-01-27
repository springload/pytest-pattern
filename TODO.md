# TODO

* [ ] Test repr methods
* [ ] Make `contains`, `startswith`, `endwith` methods into classes to support clearer reprs.
* [ ] A `match_type` matcher which returns True if type matches.
* [ ] Add CompoundMatch class which tests child matches, and implement `&`, `|` and `!` 
  for all matcher classes.
* [ ] Add function based matcher - given a function, return a matcher that can be used 
  to wrap any type, then call the function at comparison time.
