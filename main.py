'''
Psydoor Game Pseudocode
by Amadeusz Sanchez
'''
Game begins with a main menu with a start button
If player presses Start Button then game will change screens to a screen with 2 button, Load, and New. New Makes a new game and wipes all previous data in a world, Load allows a player to go back to where they were when they last saved. A new game will lead player to the starting room and will take you to a world already made that is made up of rooms that make up a 25room x 25room world

If player_health reaches 0, player teleports to spawnpoint
If player presses up key then character will move north
If player presses down key then character will move south
If player presses right key then plyer will move east
If player presses left key then player will move west
If player presses the S key then the BOX will open
If player presses the A key the game will save
If player presses the Z key player will use item equipped 
If player presses the X key player will interact

BOX 
The BOX functions as the games inventory. Items that the player picks up go into the BOX, and the BOX can be used to select what item will be used when the Z key is pressed

ITEMS
Item_Sword spawns entity_sword 0 tiles in front of player when player presses Z if item is equipped. Item_Sword cannot be used if entity_sword is spawned
entity_sword travels 1 tile and despawns in 0.5 seconds
entity_sword deals 10 damage on impact with Mob
Item_LongSword spawns entity_Lsword 0 tiles in front of player when player presses Z if item is equipped. Item_LongSword cannot be used if entity_Lsword is spawned
entity_Lsword travels 3 tiles and despawns in 0.7 seconds
entity_Lsword deals 20 damage on impact with Mob
Item_DoorSword spawns entity_Dsword 0 tiles in front of player when player presses Z if item is equipped. Item_DoorSword cannot be used if entity_Dsword is spawned
entity_Dsword travels 5 tiles and despawns in 0.5 seconds
entity_Dsword deals 30 damage on impact with Mob
Item_PsySword spawns entity_Psword 0 tiles in front of player when player presses Z if item is equipped. Item_PsySword cannot be used if entity_Psword is spawned
entity_Psword travels 6 tiles and despawns in 0.4 seconds
entity_Psword deals 40 damage on impact with Mob
Item_Congrips spawns entity_ConGrip 0 tiles in front of player when player presses Z if item is equipped. Item_ConGrips cannot be used if entity_ConGrip is spawned
entity_ConGrips travels 3 tiles and despawns in 0.2 seconds
entity_Congrips deals 35 damage on impact with Mob
Item_Lifesetter sets spawnpoint 1 tile in front of player
Item_FoodCube gives player 15 player_health
Item_FoodCube will not function if player_health is at 150
Item_Dangerstick spawns entity_bullet 1 tiles in front of player when player presses Z if item is equipped. When entity_bullet is spawned Item_Bullet is used. Item_Dangerstick cannot be used if player does not have Item_Bullet in the BOX
entity_bullet travels 15 tiles and despawns in 1 seconds
entity_bullet deals 30 damage on impact with Mob
Item_SuperCube gives player 20 player_health
Item_SuperCube will not function if player health is at 250
Item_Coin is dropped by MOB objects, it is used to buy things at shops, it is put into the BOX when walked over by player
Item_EpicCube gives player 50 player_health
Item_EpicCube will not function if player health is at 400


MOBS
All objects tagged with MOB react the same to Items/entities that use MOB in Code 

MOB_PsyBot moves towards player and deletes 10 player_health on impact. MOB_PsyBot can take 10 damage before dying, MOB_Psybot drops 1 Item_Coin upon death
MOB_Doorman does not move, but faces towards player at all times, MOB_Doorman can take 20 damage before dying 
MOB_Doorman spawns entity_Eball when player is 10 tiles away from it every 3 seconds, MOB_Doorman drops 1 Item_Coin upon death
entity_Eball travels towards player and deletes 5 player_health on impact
entity_Eball despawns after 3 seconds
MOB_Psyelf moves towards player and deletes 15 player health on impact. MOB_Psyelf can take 30 damage before dying, MOB_Psyelf drops 1 Item_Coin
MOB_Doorlord does not move, but faces towards player at all times, MOB_Doorlord can take 30 damage before dying, MOB_Doorlord drops 2 Item_Coin upon death 
MOB_Doorlord spawns entity_Dball when player is 15 tiles away from it every 3 seconds
entity_Dball travels towards player and deletes 5 player_health on impact
entity_Dball despawns after 3 seconds
MOB_Psyrare moves towards player and deletes 20 player_health on impact. MOB_Psyrare can take 200 damage before dying
When MOB_Psyrare dies, Item_LongSword is spawned on the tile MOB_Psyrare died on. Item_LongSword is put into the BOX when player walks over it, MOB_Psyrare drops 30 Item_Coin upon death
MOB_CyberBot moves towards player and deletes 20 player_health on impact. MOB_PsyBot can take 30 damage before dying, MOB_CyberBot drops 3 Item_Coin upon death
MOB_BoomMan moves towards player and deletes 10 player_health on impact. MOB_BoomMan can take 30 damage before dying, MOB_BoomMan drops 2 Item_Coin upon death
MOB_BoomMan spawns entity_Boom when player is 10 tiles away from it every 2 seconds
entity_Boom travels towards player and deletes 7 player_health on impact
entity_Boom despawns after 3 seconds
MOB_Robed spawns entity_magic every 3 seconds in the direction MOB_Robed is facing
MOB_Robed faces in the players direction and moves 3 tiles in a random direction every 2 seconds. MOB_Robed will move a different direction when hitting a Wall
MOB_Robed deletes 15 player_health on impact with player.
MOB_Robed can take 10 damage before dying, MOB_Robed drops 4 Item_Coin upon death
entity_magic deletes 10 player_health on impact with player
entity_magic despawns after touching a Wall or player
MOB_Cyberare moves towards player and deletes 25 player_health on impact. MOB_Cyberare can take 300 damage before dying
MOB_Cyberare spawns entity_Boom every 1 second
When MOB_Cyberare dies, Item_DoorSword is spawned on the tile MOB_Cyberare died on. Item_DoorSword is put into the BOX when player walks over it, MOB_Cyberare drops 50 Item_Coin upon death
MOB_Sicklebot moves towards player and deletes 40 player_health on impact. MOB_Sicklebot can take 20 damage before dying, MOB_Sicklebot drops 6 Item_Coin upon death
MOB_Hammerbot moves towards player and deletes 20 player_health on impact. MOB_Hammerbot can take 70 damage before dying, MOB_Hammerbot drops 8 Item_Coin upon death
MOB_Abok moves towards player and deletes 30 player_health on impact. MOB_Abok can take 60 damage before dying. MOB_Abok spawns entity_Aball every second, MOB_Abok faces player while it moves towards player, MOB_Abok drops 12 Item_Coin upon death
entity_Aball travels in a straight line in the direction it was spawned in until hitting player or Wall, entity_Aball deletes 30 player_health on impact
MOB_Devote spawns entity_wisp every 3 seconds in the direction MOB_Devote is facing
MOB_Devote faces in the players direction and moves 3 tiles in a random direction every 1 second. MOB_Devote will move a different direction when hitting a Wall
MOB_Devote deletes 20 player_health on impact with player.
MOB_Devote can take 50 damage before dying, MOB_Devote drops 10 Item_Coin upon death
entity_Wisp deletes 20 player_health on impact with player
entity_Wisp despawns after touching a Wall or player
MOB_Commiebot moves towards player and deletes 30 player_health on impact, MOB_Commiebot can take 80 damage before dying, MOB_Commiebot spawns entity_wisp every 2 seconds, MOB_Commiebot drops 15 Item_Coin upon death
MOB_Stalinbot moves towards player and deltes 40 player_health on impact, MOB_Stalinbot can take 150 damage before dying, MOB_Stalinbot spawns Item_PsySword on the tile MOB_Stalinbot died on, Item_PsySword is put into the BOX when player walks over it, MOB_Stalinbot drops 50 Item_Coin upon death
MOB_CyberStalin moves towards player and deletes 50 player_health on impact MOB_CyberStalin can take 500 damage before dying, MOB_CyberStalin drops 100 Item_Coin upon death
MOB_CyberStalin spawns entity_Stalball every 5 seconds
entity_Stalball travels towards player and deletes 40 player_health on impact, entity_Stalball despawns when entity_Stalball touches Wall or player

NPC
All objects tagged with NPC react the same to Items/entities that use NPC in Code 
player cannot buy anything from NPC objects without the correct number of Item_Coin
NPC_Joe is stationary, when player interact with NPC_Joe, text appears letting you choose items to buy, items NPC_Joe sells are Item_FoodCube (5 Item_Coin), Item_Lifesetter (5 Item_Coin), Item_Bullet (3 Item_Coin)
NPC_Ligma is stationary, when player interact with NPC_Ligma, text appears letting you choose items to buy, items NPC_Ligma sells are Item_SuperCube (15 Item_Coin), Item_Dangerstick (80 Item Coin, Item_Bullet (3 Item_Coin)
NPC_JCB is stationary, when player interact with NPC_JCB, text appears letting you choose items to buy, items NPC_JCB sells are Item_EpicCube (20 Item_Coin), Item_Dangerstick (80 Item Coin), Item_Bullet (3 Item_Coin), Item_Congrips (80 Item_Coin)
 (Items bought from NPC objects go to the BOX)