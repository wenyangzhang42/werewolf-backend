# werewolf-backend

### Introduction
    An open source app to host a board game called werewolf.
    coded by me (wenyangzhang42@github) and I have all copy-rights.
    free to download for study and personal uses. No commertial uses.


### How to run locally:
  in root directory, run `sh start.sh`

### Notes:
* This project is **NOT FINISHED**, still in development.
* Cupid's Alignment will be:  
  * werewolf if lovers are 2 werewolves. 
  * lover if 1 good 1 bad.
  * god if two good lovers
* Does not support uncommon game sets for now. 
  e.g: 7 hunters 3 werewolves


### Known bugs:  
- checking

### Todos:
* re-initialize and restart logic, check if game on going.
  maybe if game on going, ask user to confirm, then reset game.
* Exception Handling, different level handlers
  Use api_exception and HTTPexception template


### future improvements:
* Add support to role: Thief
* Host more than one games at the same time
* Support uncommon game sets
* Add security feature, token, auth, etc.
* Cache, maybe multi layer Cache
* Should I support re-seat? will need to figure out how to do role assignment.

    
