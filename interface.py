from equipes.py import Team, Participants
from tableau.py import Tableau
print("###[Gestionnaire de tournoi de pétanque]###")
all_participants = Participants()


print("### Phase 1 : Inscription")
choix = 0
while not choix == 3 : 
	menu = """1) Ajouter une équipe
2) Voir la liste des équipes
3) Clôturer la phase d'inscription"""
	choix = int(input(menu))
	if choix == 1 : 
		nom_equipe = str(input("Nom de l'équipe : "))
		nom_j1 = str(input("Nom du joueur 1 "))
		nom_j2 = str(input("Nom du joueur 2 "))
		all_participants.add(Team(nom_equipe,nom_j1,nom_j2))
	if choix == 2 : 
		data = all_participants.getAllTeams()
		for teamsraw in data : 
			print(f"# Equipe : {teamsraw['name']}")
			print(f"Joueur 1 : {teamsraw['p1']}")
			print(f"Joueur 2 : {teamsraw['p2']}")
			print()

print("### Phase 2 : Tournoi")
tournament = Tableau()
tournament.addTurn(all_participants.data,randomize = True)

while 1: 
	qualified_teams = Participants()
	for match in tournament.data[-1] : 
		print(f"# Match : {match[0].name} VS {match[1].name}")
		input("Appuyez sur une touche pour terminer le match")
		result0 = int(input(f"Score de {match[0].name} : "))
		result1 = int(input(f"Score de {match[1].name} : "))
		if result0>result1 : 
			winner = match[0]
			score_winner = result0
			loser = match[1]
			score_loser = result1
		else : 
			winner = match[1]
			score_winner = result1
			loser = match[0]
			score_loser = result0
		qualified_teams.add(winner)
		all_participants.saveMatch(winner,loser,score_winner,score_loser)
	if len(qualified_teams.data) == 1 : 
		print("## Tournoi terminé")
		print(f"# Gagnant : {qualified_teams.data[0].name}")
		break
	else : 
		tournament.addTurn(qualified_teams.data)


print("### Phase 3 : Résultats")
menu = """1) Afficher les statistiques des équipes
2) afficher un classement des équipes
0) Quitter
"""
choix = -1
while not choix == 0 :
	choix = int(input(menu))
	if choix == 1 : 
		for teamsraw in all_participants.getAllTeams() :
			print(f"# Equipe : {teamsraw['name']}")
			print(f"Joueur 1 : {teamsraw['p1']}")
			print(f"Joueur 2 : {teamsraw['p2']}")
			print(f"Nombre de points marqués par match : {teamsraw['avgpts']}")
			print(f"Taux de victoire : {teamsraw['winrate']}")
			print(f"Nombre de matchs gagnés : {teamsraw['n_win']}")
	if choix == 2 :
		all_teams = all_participants.getAllTeams()
		all_teams.sort(lambda x : x['n_win'])






