from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa
import time

#connect to yahoo api

sc =OAuth2(None, None, from_file='c:\proj\yahoo\oauth2.json')

#get game object
gm = yfa.Game(sc, 'nba')

leagues = gm.league_ids()

print(leagues)

#get the league object 
lg = gm.to_league('418.l.69932')

#get the team key
teamkey = lg.team_key()

#get the team object
team = lg.to_team(teamkey)

#get team roster
roster = team.roster()

print("=== MY TEAM ===")

for r in roster:
    print(r)

fa = lg.free_agents("G")

print("=== FREE AGENTS ===")

for p in fa:
    print(p)

# Drop Player
#team.drop_player(6619)

# Add Player
#team.add_player(6169)