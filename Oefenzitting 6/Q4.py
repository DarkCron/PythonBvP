f = open("survey.txt","r")
allTeams = {"Bel","Eng","Ger","Fra","Ita","Spa","Cam"}
allTeamsByPlayers = set()
fansWhoLikeBelGer = 0
fansWhoLikeTheSameClubs = 0
fanCombo = set()
for line in f.readlines():
    line = line.strip()
    fansOf = line.split(" ")
    for club in fansOf:
        if not club in allTeamsByPlayers:
            allTeamsByPlayers.add(club)
    if "Ger" in fansOf and "Bel" in fansOf:
        fansWhoLikeBelGer+=1
    combo = ""
    for club in allTeams:
        if club in fansOf:
            combo+=club
    if combo in fanCombo:
        fansWhoLikeTheSameClubs+=1
    else:
        fanCombo.add(combo)


f.close()
print("Clubs nobody likes: ")
for club in allTeams:
    if not club in allTeamsByPlayers:
        print(club,end=", ")
print()
print("Fans that like Bel and Ger: ",fansWhoLikeBelGer)
print("Fans that like the same club: ",fansWhoLikeTheSameClubs)