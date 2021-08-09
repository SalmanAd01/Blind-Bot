import discord
import requests
from alive import keep_alive
client=discord.Client()
intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)
key="" #Enter your API Token
dict = {
  'first':'#',
  'second':'#',
  'third':'#'
} #Enter Your alliance's Clan Tag
th9=0
th10=0
th11=0
th12=0
th13=0
th14=0
Total_Members=0
Chat_Language=""
cwl_leagues=""
def find_th(tag):
  try :
    url = "https://api.clashofclans.com/v1/players/%23"+tag
    headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    print(data)
    if data['townHallLevel'] == 9:
      global th9
      th9 = th9 + 1
    if data['townHallLevel'] == 10:
      global th10
      th10 = th10 + 1
    if data['townHallLevel'] == 11:
      global th11
      th11 = th11 + 1
    if data['townHallLevel'] == 12:
      global th12
      th12 = th12 + 1
    if data['townHallLevel'] == 13:
      global th13
      th13 = th13 + 1
    if data['townHallLevel'] == 14:
      global th14
      th14 = th14 + 1
    return 1
  except:
    return "No"
def find_totalplayer(tag):
  try :
    url = "https://api.clashofclans.com/v1/clans/%23"+tag+"/members"
    headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    lenght=len(data['items'])
    for i in range(lenght):
      find_th(data['items'][i]['tag'][1:])
    # print("items",lenght)
    return 1
  except:
    return "No"
def clan_name(tag):
  try :
    url = "https://api.clashofclans.com/v1/clans/%23"+tag
    headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    print(data)
    global Total_Members
    Total_Members+=data['members']
    global cwl_leagues
    cwl_leagues = cwl_leagues + data['warLeague']['name']+"\n"
    # print(data)
    return data['name']
  except:
    return "No"
def clan_location(tag):
  try :
    url = "https://api.clashofclans.com/v1/clans/%23"+tag
    headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    global Chat_Language
    Chat_Language=data['chatLanguage']['name']
    # print(data)
    return data['location']['name']
  except:
    return "No"
def iterate(temp):
  str1=""
  for item_1 in dict.values():
    print(item_1)
    if temp == 1:
      find_totalplayer(item_1[1:])
    elif temp == 2:
      str1=str1+(clan_name(item_1[1:]))
      str1= str1+ "  "
      # print("lol",str1)

  return str1
def fe_family():
  try:
    # print("ITE",iterate(2))
    myembed=discord.Embed(title=iterate(2)+"\n"+"("+dict['first']+")   "+"("+dict['second']+")      "+"("+dict['third']+")",discription="YO",color=0x00ff00)
    iterate(1)
    myembed.add_field(name=":globe_with_meridians:Locations",value=clan_location(dict['first'][1:]),inline=True)
    myembed.add_field(name=":two_men_holding_hands:Total Members",value=Total_Members,inline=True)
    guild=client.get_guild(742468234099556422)
    # myembed.set_thumbnail(url=guild.icon_url)
    myembed.set_author(name="First Edition Family",icon_url=guild.icon_url)
    myembed.add_field(name=":speaking_head:Chat Language",value=Chat_Language,inline=True)
    myembed.add_field(name=":crossed_swords:Clan Wal Leagues",value=cwl_leagues,inline=False)
    myembed.add_field(name=":muscle:ThCompo",value="<:emoji_1:794487347408011264>  "+str(th9)+"    <:emoji_2:794486388187070464>  "+str(th10)+"    <:emoji_3:794487037343563777>  "+str(th11)+"    <:emoji_4:794488552720826388>  "+str(th12)+"    <:emoji_5:794489021899341834>  "+str(th13)+"    <:emoji_6:835046641845141514>  "+str(th14),inline=False)

    # myembed.add_field(value="<:emoji_1:794487347408011264>  "+str(th9),name="** **",inline=True)
    # myembed.add_field(value="<:emoji_2:794486388187070464>  "+str(th10),name="** **",inline=True)
    # myembed.add_field(value="<:emoji_3:794487037343563777>  "+str(th11),name="** **",inline=True)
    # myembed.add_field(value="<:emoji_4:794488552720826388>  "+str(th12),name="** **",inline=True)
    # myembed.add_field(value="<:emoji_5:794489021899341834>  "+str(th13),name="** **",inline=True)
    # myembed.add_field(value="<:emoji_6:835046641845141514>  "+str(th14),name="** **",inline=True)
    return (myembed)
  except:
    myembed=discord.Embed(title="Error",discription="yo",color=0x00ff00)
    return (myembed)
def find_name(tag):
  try :
    url = "https://api.clashofclans.com/v1/clanwarleagues/wars/%23"+tag
    headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    # print(data)
    try:
      if data['clan']['name']=="+FirstEdition+":
        return 1
      elif data['opponent']['name']=="+FirstEdition+":
        return 1
      else:
        return -1
    except:
      return -1
  except:
    return -1
def get_wartag(round_no):
  try :
    url ="https://api.clashofclans.com/v1/clans/%23YVP0VQ2/currentwar/leaguegroup"
    headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    # print(data)
    lenght=len(data['rounds'])
    print("\n\n\nYes\n\n\n",lenght)
    # print("Ro",round_no)
    # print("data",data['rounds'][int(round_no)-1]['warTags'][2])
    if int(round_no)<=lenght:
      for i in range(4):
        if find_name((data['rounds'][int(round_no)-1]['warTags'][i])[1:])==1:
          return (data['rounds'][int(round_no)-1]['warTags'][i])
    # print(data)
    else :
      return "NO"
  except:
    return "No"
@client.event
async def on_ready():
  print("We have Logged in as {0.user}".format(client))
def shoutout(tag) :
  try :
    url = "https://api.clashofclans.com/v1/clanwarleagues/wars/%23"+tag
    headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    # print(data)
    if data['clan']['name'] =="+FirstEdition+":
      str3="clan"
      str4="opponent"
    else:
      str3="opponent"
      str4="clan"
    myembed=discord.Embed(title=":globe_with_meridians:War Shoutouts",description=data[str3]['name']+"  Vs  "+data[str4]['name'],color=0x33C1FF)
    lenght=len(data[str3]['members'])
    # print("len",lenght)
    # print(data[str3]['members'][0]['attacks'][0]['stars'])
    for i in range (lenght):
      try:
        if data[str3]['members'][i]['attacks'][0]['stars']==3:
          myembed.add_field(name=data[str3]['members'][i]['name'],value=":cookie::milk:(:three:)",inline= True)
      except:
        continue

    # print(data['clan']['members'])
    # print(lenght)
    return (myembed)
  except:
    myembed=discord.Embed(title="War Shoutout",description="#"+tag,color=0xFFA833)
    myembed.add_field(name="Not Found",value="Error...",inline=True)
    return (myembed)
def player_tag(tag):
  try:
    url="https://api.clashofclans.com/v1/players/%23"+tag
    headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    print(data)
    try:
      if data['reason']=='inMaintenance':
        myembed=discord.Embed(title="Player Info",description="Maintenance break",color=0x00ff00)
    except:
      i=0
      lenght=len(data['heroes'])
      myembed=discord.Embed(title="Player Info",description="#"+tag,color=0x00ff00)
      myembed.add_field(name=":sunglasses:Player Name",value=data['name'],inline=True)
      myembed.add_field(name="<:lvl20:871711001534418984> Clan Name",value=data['clan']['name'],inline=True)
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
    myembed.add_field(name="Not Found",value="Enter The Right Tag",inline=True)
    return (myembed)
def clan_tag(tag):
  try :
      url = "https://api.clashofclans.com/v1/clans?name=%23"+tag
      headers = {"Accept": "application/json","authorization": "Bearer %s" % key}
      response = requests.request("GET", url, headers=headers)
      data = response.json()
      print(data)
      try:
        myembed=discord.Embed(title=":globe_with_meridians:Locations",description=data['items'][0]['location']['name'],color=0xFFA833)
      except:
        myembed=discord.Embed(title=":globe_with_meridians:Locations",description='none',color=0xFFA833)

      myembed.set_author(name=data['items'][0]['name']+"("+tag+")",icon_url=data['items'][0]['badgeUrls']['small'])
      # myembed.add_field(name="<:lvl20:871711001534418984> Clan Name",value=data['items'][0]['name'],inline=True)
      # myembed.add_field(name=":globe_with_meridians:Locations",value=data['items'][0]['location']['name'],inline=True)
      myembed.add_field(name=":100:Clan Level",value=str(data['items'][0]['clanLevel']),inline=True)
      myembed.add_field(name=":muscle:War Win Streak",value=str(data['items'][0]['warWinStreak']) ,inline=True)
      myembed.add_field(name="<:ChampionLeagueI:774314462693949490>War League",value=data['items'][0]['warLeague']['name'],inline=True)
      myembed.add_field(name=":two_men_holding_hands:Total Members",value=str(data['items'][0]['members']),inline=False)
      try:
        myembed.add_field(name=":speaking_head:Chat Language",value=data['items'][0]['chatLanguage']['name'],inline=True)
      except:
        myembed.add_field(name=":speaking_head:Chat Language",value="Not Set",inline=True)
      myembed.add_field(name=":no_entry_sign:Required TownHall",value=str(data['items'][0]['requiredTownhallLevel']),inline=True)
      return (myembed)
  except:
      myembed=discord.Embed(title="Clan Info",description="#"+tag,color=0xFFA833)
      myembed.add_field(name="Not Found",value="Enter The Right Tag",inline=True)
      return (myembed)
@client.event
async def on_member_join(member):
  guild=client.get_guild(742468234099556422)
  channel = guild.get_channel(872862720469397564)
  embed=discord.Embed(title=f"Welcome {member.name}", description=f" #rol Thanks for joining {member.guild.name}!") # F-Strings!
  embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
  await channel.send(embed=embed)
  # await channel.send("Welcome to the sever")
  await member.send("Welcome to the sever")

@client.event
async def on_message(message):
  if message.author == client.user:
    return 
  if message.content.startswith('+clan'):
    tag=message.content.split('+clan ',1)[1]
    print(tag)
    if(tag == 'fe'):
      await message.channel.send(embed=clan_tag(dict['first'][1:]))
    elif (tag == 'ts'):
      await message.channel.send(embed=clan_tag(dict['second'][1:]))
    elif (tag == 'se'):
      await message.channel.send(embed=clan_tag('2YYQPVPGJ'))
    else:
      await message.channel.send(embed=clan_tag(tag[1:]))
  if message.content.startswith('+help'):
    myembed=discord.Embed(title='Commands',description='Bot Version 1.0',color=0x00ff00)
    myembed.set_thumbnail(url="https://cdn.discordapp.com/emojis/874253502505959425.png?v=1")
    myembed.add_field(name="+player",value="To Get The Basic Player Info",inline=False)
    myembed.add_field(name="+clan",value="To Get The Basic Clan Info",inline=False)
    myembed.add_field(name="+shoutout",value="To Shoutout the one who got the 3 star",inline=False)
    myembed.add_field(name="+fefamily",value="To get the basic info about the FEfamily",inline=False)
    await message.channel.send(embed=myembed)
  if message.content.startswith('+player'):
    tag=message.content.split('+player ',1)[1]
    await message.channel.send(embed=player_tag(tag[1:]))
  if message.content.startswith('+fefamily'):
    global Total_Members
    Total_Members = 0
    global th9
    th9=0
    global th10
    th10=0
    global th11
    th11=0
    global th12
    th12=0
    global th13
    th13=0
    global th14
    th14=0
    global cwl_leagues
    cwl_leagues=""
    await message.channel.send(embed=fe_family())
  if message.content.startswith('+shoutout'):
    guild=client.get_guild()#Enter the server id(server settings -> Widget -> Copy server Id)
    channel = guild.get_channel()#Enter Channel Id 
    round_no=message.content.split("+shoutout ", 1)[1]
    # print("number",round_no)
    # print("ROg",get_wartag(round_no))
    str1=get_wartag(round_no)
    # print(str1)
    if str1 == 'NO':
      await channel.send("```Make Sure The Clan is in war and the battel day for particular round is started```")
    else:
      str2=str1[1:]
      await channel.send(embed=shoutout(str2))
  
keep_alive()
client.run ('')#Enter Your bot token
