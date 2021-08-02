import discord
import requests
from keep_alive import keep_alive
client=discord.Client()
key="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImZlNDFhYzViLTQwNTAtNDk1ZS1hMGNkLTZkOGQxNGMzMTg1ZCIsImlhdCI6MTYyNzg5NDY0NCwic3ViIjoiZGV2ZWxvcGVyLzRkYzFkZmY5LTA3YTYtYTlhNy0wYjBjLTFkYWU0YzZmNmI0YSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM1LjE5Mi4xMjMuMjAiXSwidHlwZSI6ImNsaWVudCJ9XX0.4cWeTqtVUJh-jdbL522DvSQgrKTo8RRTRe2VCGPBsgmovtMypLg4RQRq3vUU7yXyv83tUzkh8Va_jcs2F6wpZA"
def playertag(tag):
  try:
    url="https://api.clashofclans.com/v1/players/%23"+tag
    headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    # print(data)
    i=0
    lenght=len(data['heroes'])
    myembed=discord.Embed(title="Player Info",description="#"+tag,color=0x00ff00)
    myembed.add_field(name=":sunglasses:Player Name",value=data['name'],inline=True)
    myembed.add_field(name=":star2:War Stars",value=str(data['warStars']),inline=True)
    myembed.add_field(name=":hugging:Donations",value=str(data['donations']) ,inline=True)
    myembed.add_field(name="<:14:828991721181806623>Town Hall Level",value=str(data['townHallLevel']),inline=True)
    myembed.add_field(name=":level_slider:Xp",value=str(data['expLevel']),inline=True)
    myembed.add_field(name=":yum:Donation Recieve",value=str(data['donationsReceived']),inline=True)
    myembed.add_field(name="<:bb09:759066347811766272>Bilder Hall Level",value=str(data['builderHallLevel']),inline=True)
    myembed.add_field(name="<:LegendLeague:601612163169255436>Trophies",value=str(data['trophies']),inline=True)
    myembed.add_field(name=":trophy:BH Trophies",value=str(data['versusTrophies']),inline=True)
    for i in range(lenght):
      if data['heroes'][i]['name'] == "Barbarian King":
        myembed.add_field(name="<:BarbarianKing2:701626158525054976>"+data['heroes'][i]['name'] ,value=str(data['heroes'][i]['level']),inline=True)
      if data['heroes'][i]['name'] == "Archer Queen":
        myembed.add_field(name="<:ArcherQueen:701626158487175270>"+data['heroes'][i]['name'] ,value=str(data['heroes'][i]['level']),inline=True)
      if data['heroes'][i]['name'] == "Grand Warden":
        myembed.add_field(name="<:GrandWarden:701933765450268672>"+data['heroes'][i]['name'] ,value=str(data['heroes'][i]['level']),inline=True)
      if data['heroes'][i]['name'] == "Battle Machine":
        myembed.add_field(name="<:BattleMachine:701626158705541261>"+data['heroes'][i]['name'] ,value=str(data['heroes'][i]['level']),inline=True)
      if data['heroes'][i]['name'] == "Royal Champion":
        myembed.add_field(name="<:RoyalChampion:701933810648088606>"+data['heroes'][i]['name'] ,value=str(data['heroes'][i]['level']),inline=True)
    return (myembed)
  except:
    myembed=discord.Embed(title="Player Info",description="#"+tag,color=0x00ff00)
    myembed.add_field(name="Not Found",value="Enter The Right The Tag",inline=True)
    return (myembed)
def clantag(tag) :
    try :
        url = "https://api.clashofclans.com/v1/clans?name=%23"+tag
        headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
        response = requests.request("GET", url, headers=headers)
        data = response.json()
        myembed=discord.Embed(title="<:clancastle:840872083671220225>Clan Info",description="#"+tag,color=0xFFA833)
        myembed.add_field(name="<:clanbadgelv18:601613767582679051>Clan Name",value=data['items'][0]['name'],inline=True)
        myembed.add_field(name=":globe_with_meridians:Locations",value=data['items'][0]['location']['name'],inline=True)
        myembed.add_field(name=":100:Clan Level",value=str(data['items'][0]['clanLevel']),inline=True)
        myembed.add_field(name=":muscle:War Win Streak",value=str(data['items'][0]['warWinStreak']) ,inline=True)
        myembed.add_field(name="War League",value=data['items'][0]['warLeague']['name'],inline=True)
        myembed.add_field(name=":two_men_holding_hands:Total Members",value=str(data['items'][0]['members']),inline=False)
        myembed.add_field(name=":speaking_head:Chat Language",value=data['items'][0]['chatLanguage']['name'],inline=True)
        myembed.add_field(name=":no_entry_sign:Required TownHall",value=str(data['items'][0]['requiredTownhallLevel']),inline=True)
        return (myembed)
    except:
        myembed=discord.Embed(title="Clan Info",description="#"+tag,color=0xFFA833)
        myembed.add_field(name="Not Found",value="Enter The Right The Tag",inline=True)
        return (myembed)
def get_th(tag):
  try:
    url="https://api.clashofclans.com/v1/players/%23"+tag
    headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    str1=""+str(data['townHallLevel']).zfill(2)
    # print(str1)
    i=0
    try:
      lenght=len(data['heroes'])
    except:
      lenght=0
    # print(lenght)
    count=0
    for i in range(lenght):
      if data['heroes'][i]['name'] == "Barbarian King":
        str1= str1 +"    "+str(data['heroes'][i]['level']).zfill(2)
        count += 1
      if data['heroes'][i]['name'] == "Archer Queen":
        str1= str1 +"    "+str(data['heroes'][i]['level']).zfill(2)
        count += 1
      if data['heroes'][i]['name'] == "Grand Warden":
        str1= str1 +"    "+str(data['heroes'][i]['level']).zfill(2)
        count += 1
      if data['heroes'][i]['name'] == "Royal Champion":
        str1= str1 +"    "+str(data['heroes'][i]['level']).zfill(2)
        count += 1
    for i in range(4-count):
      str1=str1+"    "+"00"
    # print("Final",str1)
    return (str1)
  except:
    str2="Not Found"
    return (str2)
def members(tag):
  try :
      url = "https://api.clashofclans.com/v1/clans/%23"+tag
      headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
      response = requests.request("GET", url, headers=headers)
      data = response.json()
      i=0
      lenght=len(data['memberList'])
      str1="TH    "+"BK    "+"AQ    "+"GW    "+" RC    "+"Name" + "\n"
      for i in range(lenght):
        str3=""
        str3=data['memberList'][i]['tag']
        str4=str3[1:]
        # print(str4)
        str1 = str1 + str(get_th(str4)) +"    "+ data['memberList'][i]['name']+"\n"
      return (str1)
  except:
      str2="Not Found"
      return (str2) 
def current_war(tag): 
  try :
      url = "https://api.clashofclans.com/v1/clans/%23"+tag+"/currentwar"
      headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
      response = requests.request("GET", url, headers=headers)
      data = response.json() 
      str1="`"+data['clan']['name']+"Vs".rjust(10," ")+data['opponent']['name'].rjust(20," ")+"`\n"
      # str1=str1+"#".ljust(5)+"BK".ljust(5)+"AQ".ljust(5)+"GW".ljust(5)+"RC".ljust(25)+"BK".ljust(5)+"AQ".ljust(5)+"GW".ljust(5)+"RC".ljust(5)
      # lenght=data['clan']['members']
      # for i in range(lenght):
      #   str1=str1+
      return (str1)
  except:
      str2="Not Found"
      return (str2)      
@client.event
async def on_ready():
  print("We have Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('+playertag'):
    tag=message.content.split("+playertag ", 1)[1]
    new_tag=tag[1:]
    await message.channel.send(embed=playertag(new_tag))
  if message.content.startswith('+clantag'):
    tag=message.content.split("+clantag ", 1)[1]
    new_tag=tag[1:]
    str1=clantag(new_tag)
    await message.channel.send(embed=clantag(new_tag))
  if message.content.startswith('+members'):
    tag=message.content.split("+members ", 1)[1]
    new_tag=tag[1:]
    str1=members(new_tag)
    await message.channel.send("**```yaml\n"+str1+"```**")
  if message.content.startswith('+currentwar'):
    tag=message.content.split("+currentwar ", 1)[1]
    new_tag=tag[1:]
    str1=current_war(new_tag)
    await message.channel.send("**```yaml\n"+str1+"```**")
  if message.content.startswith('+help'):
    myembed=discord.Embed(title="Commands",description="Bot Version is 1.0",color=0x33C1FF)
    myembed.add_field(name="+playertag",value="Basic Info Of A Player",inline=False)
    myembed.add_field(name="+clantag",value="Basic Info Of A Clan",inline=False)
    myembed.add_field(name="+members",value="Basic Info Of A Clan Members",inline=False)
    myembed.add_field(name="+currentwar",value="Basic Info Of A Current Clan War",inline=False)
    await message.channel.send(embed=myembed)

keep_alive()
client.run('ODcxMjM0NzE5MTg5MTg4NzAw.YQYWjw.lmwfmHDqizqXU_QCPnwg_YdAy5U')
