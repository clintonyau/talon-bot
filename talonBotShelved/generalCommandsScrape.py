# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 07:39:22 2021

"""

import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from .webscraper import WebScraper
import nest_asyncio
import asyncio
import random
nest_asyncio.apply()

class GeneralCommands(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.command(name = 'conq', aliases = ['conqueror']) #add rune images + explanations later
    async def displayConq(self,ctx):
        file = discord.File('images/conq.png', filename = 'conq.png')
        await ctx.send(file=file)
        await ctx.send('\'Standard\' runes are unboxed. Runes with yellow boxes are alternative choices.')
        
    @commands.command(name = 'elec', aliases = ['electrocute'])
    async def displayElec(self,ctx):
        file = discord.File('images/elec.png', filename = 'elec.png')
        await ctx.send(file=file)
        await ctx.send('\'Standard\' runes are unboxed. Runes with yellow boxes are alternative choices.')
        
    @commands.command(name = 'lethality', aliases = ['leth','assassin'])
    async def displayLethality(self,ctx):
        embed1 = discord.Embed(
            title = 'Lethality items',
            description = 'A pool of lethality items you should buy on lethality Talon. Note that items from this list and the bruiser list can both be in the same build and that there is no definitive order to build them.',
            color = discord.Color.blue()
        )
        embed1.add_field(name = '★Prowler’s Claw', 
                         value = 'Its dash allows you to gapclose and gives a 15% damage increase against targets. Ideally, you use the active before you proc your passive.\
 This item should be bought if you\'re dealing with mobility targets or want extra damage in one-shotting. It is also a good item to build from behind.',
                         inline = False)
        embed1.add_field(name = '★Duskblade of Draktharr', 
                         value = 'Gives bonus damage and a slow on AA and invisiblity. Equal in stats to Prowler\'s, its active is not as good but gives you higher potential for multi-kills.\
 Generally, you want to utilize the invisibility from the item to reposition. Use FOG to your advantage if you can. Currently Prowler\'s serves as a much better option.',
                         inline = False)
        embed1.add_field(name = '★Eclipse', 
                         value = 'A mythic that allows you to duel better. Its passive and shield makes it ideal to take against bruisers and tanks. Overall, it is still sub-par to Prowler\'s\
 due to its poorer waveclear. You can use the movespeed you get from its active to dodge abilities or reposition. Build it if you want\
 lethality while also having good dueling.',
                         inline = False)
        embed1.set_footer(text = 'Page 1 of 3')
        
        embed2 = discord.Embed(
            title = 'Lethality items',
            color = discord.Color.blue()
        )
        embed2.add_field(name = 'Edge of Night', 
                         value = 'Grants a reusable spell shield that\'s good against teams with CC or TF/Nocturne. Build this if you want damage, surviability, or want to deal with CC.',
                         inline = False)
        embed2.add_field(name = 'Serpent’s Fang', 
                         value = 'Anti-shield item, AA + abilities apply 50% shield debuff on all affected targets for 3 seconds. Effective against all shields except magic shields like Morgana’s.\
 Due to its low cost, it\'s one of the best lethality items to rush even if there are no shields on the enemy team.' ,
                         inline = False)
        embed2.add_field(name = 'Umbral Glaive', 
                         value = 'Disables and reveals wards nearby you, deal 3x damage to wards. Cheap and grants decent lethality. Build this if you want vision control, though Serpent\'s and oracle lenses is usually a better alternative.',
                         inline = False)
        embed2.add_field(name = 'Youmuu’s Ghostblade', 
                         value = 'Grants lethality, 20% movement speed buff active, and out-of-combat movement speed. It is not a very good item due to its cost; however, you can build this if you want faster rotations or to gapclose faster.',
                         inline = False)
        embed2.set_footer(text = 'Page 2 of 3')
        
        embed3 = discord.Embed(
                title = 'Lethality items',
                color = discord.Color.blue()
        )
        embed3.add_field(name = 'Serylda’s Grudge', 
                         value = 'Grants +30% armor pen and haste. Abilities apply 30% slow on all enemies for 1 second. Provides strong pen and gap close against mobility targets. Build this if you\'re dealing with enemies stacking armor.',
                         inline = False)
        embed3.add_field(name = 'Lord Dominiks\' Regards', 
                         value = 'Grants +35% armor pen and bonus (0-15)% physical damage based upon maximum health difference.\
 Build this if the enemy has a substantial health difference over you, you need armor pen, and you don\'t need the haste of Serylda\'s.', 
                         inline = False)
        embed3.add_field(name = 'Black Cleaver', 
                         value = 'Applies %armor reduction and grants bonus movement speed when dealing damage. Build this if you want AH, survivability, and damage or if you\'re dealing with armor stacking teams since the armor shred helps your team as well.',
                         inline = False)
        embed3.add_field(name = 'Executioner’s Calling', 
                         value = 'Grants grievous wounds. Build this when dealing with healing champions like Sylas, Yuumi, or Soraka. This is usually bought after your mythic or second item, depending on how impactful\
 the enemy healing is.',
                         inline = False)
        embed3.add_field(name = 'Maw of Malmortius',
                         value = 'Grants AD and MR. Gives a lifeline against magic damage. Generally inefficient for what it does, this is only really an acceptable option into 3+ heavy ap damage champs.',
                         inline = False)
        embed3.set_footer(text = 'Page 3 of 3')
        
        contents = [embed1, embed2, embed3]
        cur_page = 1
        message = await ctx.send(embed = contents[cur_page - 1])
        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')
        await message.add_reaction('\U0001F5D1')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in {'1️⃣', '2️⃣', '3️⃣', '\U0001F5D1'} and reaction.message.id == message.id
            # Only the sender can interact with the message. Also checks that the message is the same one being reacted on
        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=300, check=check) 
                #waits for a reaction, first argument is the reaction and second is the user, times out after 5 minutes
                if str(reaction.emoji) == '1️⃣' and cur_page != 1:
                    cur_page = 1
                    await message.edit(embed = contents[cur_page - 1])
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == '2️⃣' and cur_page != 2:
                    cur_page = 2
                    await message.edit(embed = contents[cur_page - 1])
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == '3️⃣' and cur_page != 3:
                    cur_page = 3
                    await message.edit(embed = contents[cur_page - 1])
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == '\U0001F5D1':
                    await message.delete()
                    break
                else:
                    await message.remove_reaction(reaction, user)
                    
            except asyncio.TimeoutError:
                await message.clear_reactions()
                break
        
    @commands.command(name = 'bruiser')
    async def displayBruiser(self,ctx):
        embed1 = discord.Embed(
            title = 'Bruiser items',
            description = 'A pool of bruiser mythic items you should buy on bruiser Talon. Note that items from this list and the bruiser list can both be in the same build and that there is no definitive order to build them.',
            color = discord.Color.blue()
        )
        embed1.add_field(name = '★Goredrinker', 
                         value = 'The go-to mythic for bruiser Talon. It gives you CDR, damage, HP, and waveclear. ALWAYS build ironspike whip first for the waveclear. This gives all the essential stats for bruiser Talon.', 
                         inline = False)
        embed1.add_field(name = '★Prowler’s Claw', 
                         value = 'Its dash allows you to gapclose and gives a 15% damage increase against targets. However,\
 it has worse waveclear than Goredrinker. Ideally, use the active before you proc your passive. Build this mythic if you\'re against a squishy team or you want higher one-shot potential.',
                         inline = False)
        embed1.add_field(name = '★Eclipse', 
                         value = 'A mythic that allows you to duel better. Its passive and shield makes it ideal to take against bruisers and tanks. Overall, it is sub-par to Prowler\'s\
 due to its poorer waveclear. You can use the movespeed you get from its active to dodge abilities or reposition. Build it if you want\
 lethality while also having good dueling. Note that your waveclear is even worse than if you bought Eclipse on lethality Talon.',
                         inline = False)
        embed1.set_footer(text = 'Page 1 of 3')
        
        embed2 = discord.Embed(
            title = 'Bruiser items',
            color = discord.Color.blue()
        )
        embed2.add_field(name = 'Black Cleaver', 
                         value = 'Applies %armor reduction and grants bonus movement speed when dealing damage. Build this if you want AH, survivability, and damage or if you\'re dealing with armor stacking teams since the armor shred helps your team as well.', 
                         inline = False)
        embed2.add_field(name = 'Sterak\'s Gage', 
                         value = 'Grants %max health healing and %health shield. Build this if you want\
 higher survivability in teamfights. It\'s a decent item to buy if you\'re fed since it\'ll be much harder to kill you.', 
                         inline = False)
        embed2.add_field(name = 'Bramble Vest',
                         value = 'Grants 30 armor and grievous wounds. It is not optimal to finish into Thornmail. Build this if you\'re against healing champs, usually after Goredrinker. If you chose a lethality mythic, build execution\'s calling\
 instead.', inline = False)
        embed2.add_field(name = 'Death\'s Dance', 
                         value = 'Delays 35% of all physical damage over 3 seconds into true damage. Build this if you\'re against\
 a lot of AD champions or need to deal with AD burst.', 
                         inline = False)
        embed2.add_field(name = 'Ravenous Hydra',
                         value = 'Grants AD and Omnivamp. Gives a cleave passive that’s unparalleled in it’s waveclear power. Build this if you want stronger splitting power or sustain.', 
                         inline = False)
        embed2.set_footer(text = 'Page 2 of 3')
        
        embed3 = discord.Embed(
                title = 'Bruiser items',
                color = discord.Color.blue()
        )
        embed3.add_field(name = 'Serylda\'s Grudge', 
                         value = 'Grants +30% armor pen and haste. Abilities apply 30% slow on all enemies for 1 second. Provides\
 strong pen and gap close against mobility targets. Build this if you\'re dealing with enemies stacking armor.',inline = False)
        embed3.add_field(name = 'Lord Dominiks\' Regards', 
                         value = 'Grants +35% armor pen and bonus (0-15)% physical damage based upon maximum health difference.\
 Build this if the enemy has a substantial health difference over you, you need armor pen, and you don\'t need the haste of Serylda\'s.', inline = False)
        embed3.add_field(name = 'Maw of Malmortius',
                         value = 'Grants AD and MR. Gives a lifeline against magic damage. Generally inefficient for what it does, this is only really an acceptable option into 3+ heavy ap damage champs.',
                         inline = False)
        embed3.add_field(name = 'Edge of Night', 
                         value = 'Grants a reusable spell shield that\'s good against teams with CC or TF/Nocturne. Build this if you want damage, surviability, or want to deal with CC.',inline = False)
        embed3.add_field(name = 'Serpent’s Fang', 
                         value = 'Anti-shield item, AA + abilities apply 50% shield debuff on all affected targets for 3 seconds. Effective against all shields except magic shields like Morgana’s.\
 Due to its low cost, it\'s one of the best lethality items to rush even if there are no shields on the enemy team.', inline = False)
        embed3.set_footer(text = 'Page 3 of 3')
        
        contents = [embed1, embed2, embed3]
        cur_page = 1
        message = await ctx.send(embed = contents[cur_page - 1])
        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')
        await message.add_reaction('\U0001F5D1')
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in {'1️⃣', '2️⃣', '3️⃣', '\U0001F5D1'} and reaction.message.id == message.id
            # Only the sender can interact with the message. Also checks that the message is the same one being reacted on
        while True:
            try:
                reaction, user = await self.client.wait_for("reaction_add", timeout=300, check=check) 
                #waits for a reaction, first argument is the reaction and second is the user, times out after 5 minutes
                if str(reaction.emoji) == '1️⃣' and cur_page != 1:
                    cur_page = 1
                    await message.edit(embed = contents[cur_page - 1])
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == '2️⃣' and cur_page != 2:
                    cur_page = 2
                    await message.edit(embed = contents[cur_page - 1])
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == '3️⃣' and cur_page != 3:
                    cur_page = 3
                    await message.edit(embed = contents[cur_page - 1])
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == '\U0001F5D1':
                    await message.delete()
                    break
                else:
                    await message.remove_reaction(reaction, user)
                    
            except asyncio.TimeoutError:
                await message.clear_reactions()
                break
        
    @commands.command(name = 'combos', aliases = ['combo'])
    async def displayCombos(self,ctx):
        await ctx.send('<https://www.youtube.com/watch?v=7zAKXeVIAGI&ab_channel=Staxl>')
        
    @commands.command(name = 'skills', aliases = ['ability','skill'])
    async def displayAbility(self,ctx):
        await ctx.send('With Elec and Conq, you should always be going W max into Q max. 3 in W and then Q max is also viable for Conq.')
        
    @commands.command(name = 'starter', aliases = ['starting','start','starts'])
    async def displayStart(self,ctx):
        embed = discord.Embed(
                title = 'Starting items',
                color = discord.Color.blue()
        )
        embed.add_field(name = 'Longsword + refillable',
                        value = 'The gold standard. This works against every matchup.',
                        inline = False)
        embed.add_field(name = 'Doran\'s Blade + red pot',
                        value = 'This is very good start for bruiser Talon. It is good against melee matchups as well as poke matchups. Less damage than LS but more sustain.',
                        inline = False)
        embed.add_field(name = 'Doran\'s Shield + red pot',
                        value = 'Start this if you expect the poke to be very heavy. Examples being ADC matchups like Quinn or Lucian.',
                        inline = False)
        embed.add_field(name = 'Corrupting pot',
                        value = 'Viable, but less so than the above mentioned. Generally you would start this if you expect to use a lot of mana and to be poked a lot.',
                        inline = False)
        await ctx.send(embed = embed)
        
    @commands.command(name = 'quote', aliases = ['quotes'])
    async def quote(self,ctx):
        quoteList = ['Live and die by the blade.','Pathetic!','There\'s nowhere to hide.','Let\'s finish this quickly.',
                     'Don\'t cross me.','On the razor\'s edge.','Your allegiances mean nothing to me.','I never compromise.',
                     'Only fools pledge life to honor.','They won\'t survive.']
        await ctx.send(random.choice(quoteList))
        
    @commands.command(name = 'boots', aliases = ['boot','shoe','shoes'])
    async def displayBoots(self,ctx):
        embed = discord.Embed(
                title = 'Boots',
                color = discord.Color.blue()
        )
        embed.add_field(name = 'Plated Steelcaps',
                        value = 'Provides armor. Build this if you\'re against an AD comp or need more armor against AD champs.',
                        inline = False)
        embed.add_field(name = 'Mercury’s Treads',
                        value = 'Provides tenacity and MR. Build this if you\'re against burst mages and need the extra surviability or if you\'re against CC comps.',
                        inline = False)
        embed.add_field(name = 'Ionian Boots of Lucidity',
                        value = 'Almost always built on lethality because they don’t require resistances. You build Ionian Boots on bruiser if neither Steelcaps or Treads are applicable in the current match.',
                        inline = False)
        await ctx.send(embed = embed)
        
    '''
    BucketType.default for a global basis.
    BucketType.user for a per-user basis.
    BucketType.guild for a per-server basis.
    BucketType.channel for a per-channel basis.
    '''
    
    @commands.cooldown(1,5,commands.BucketType.guild) #1 use per 5 seconds at all times <-- prevents multiple requests a second
    @commands.command(name = 'stats', aliases = ['winrate','pickrate','banrate'])
    async def statsv2(self,ctx,*,args = ''):
        if not args:
            webScrape = WebScraper('https://u.gg/lol/champions/talon/build')
            await ctx.send(webScrape.parse())
            return
        args = args.lower()
        argsList = args.split()
        
        rankSet = {'plat','platinum','dia','diamond'}
        regionSet = {'kr','na','eu','euw','br','eune','eun','jp','lan','las',
                                   'oce','ru','tr'}
        roleSet = {'top','jg','jungle','mid','middle','bot','adc','supp','support'}
        
        '''
        Permutations: 3 options to pick: Rank, region, role; Order matters
        If 1 argument -> 3 pick 1 = 3 possibilities 
        If 2 arguments -> 3 pick 2 = 6 possibilities
        If 3 arguments -> 3 pick 3 = 6 possibilities
        '''
        
        if len(argsList) == 1: #1 argument
            if argsList[0] in rankSet: #only argument is a rank, then we return the plat+ or diamond+ of the site
                if argsList[0] in {'plat','platinum'}:
                    webScrape = WebScraper('https://u.gg/lol/champions/talon/build')
                else:
                    webScrape = WebScraper('https://u.gg/lol/champions/talon/build?rank=diamond_plus','Diamond+')
            elif argsList[0] in regionSet: #only argument is a region, then we return that region for plat+
                region = regionUrl(argsList[0])
                webScrape = WebScraper(region,'',argsList[0])
            elif argsList[0] in roleSet: #only argument is a role, then we return that role for plat+
                role = roleUrl(argsList[0])
                webScrape = WebScraper('https://u.gg/lol/champions/talon/build' + '?' + role,'','',argsList[0])
            else:
                return
                
        elif len(argsList) == 2: #2 arguments
            
            if argsList[0] in rankSet and argsList[1] in regionSet:
                region = regionUrl(argsList[1])
                if argsList[0] in {'plat','platinum'}:
                    webScrape = WebScraper(region,'',argsList[1])
                elif argsList[0] in {'dia','diamond'}:
                    webScrape = WebScraper(region + '&rank=diamond_plus','Diamond+',argsList[1])
    
            elif argsList[0] in rankSet and argsList[1] in roleSet: #@Talon Bot stats diamond top
                role = roleUrl(argsList[1])
                if argsList[0] in {'plat','platinum'}:
                    webScrape = WebScraper('https://u.gg/lol/champions/talon/build' + '?' + role,'','',argsList[1])
                else:
                    webScrape = WebScraper('https://u.gg/lol/champions/talon/build' + '?' + role + '&rank=diamond_plus','Diamond+','',argsList[1])
                    
            elif argsList[0] in regionSet and argsList[1] in rankSet:
                region = regionUrl(argsList[0])
                if argsList[1] in {'plat','platinum'}:
                    webScrape = WebScraper(region,'',argsList[0])
                else:
                    webScrape = WebScraper(region + '&rank=diamond_plus','Diamond+',argsList[0])
                    
            elif argsList[0] in regionSet and argsList[1] in roleSet: #@Talon Bot stats na top
                region = regionUrl(argsList[0])
                role = roleUrl(argsList[1])
                webScrape = WebScraper(region + '&' + role,'',argsList[0],argsList[1])
                
            elif argsList[0] in roleSet and argsList[1] in regionSet:
                region = regionUrl(argsList[1])
                role = roleUrl(argsList[0])
                webScrape = WebScraper(region + '&' + role,'',argsList[1],argsList[0])
                
            elif argsList[0] in roleSet and argsList[1] in rankSet:
                role = roleUrl(argsList[0])
                if argsList[1] in {'plat','platinum'}:
                    webScrape = WebScraper('https://u.gg/lol/champions/talon/build' + '?' + role,'','',argsList[0])
                else:
                    webScrape = WebScraper('https://u.gg/lol/champions/talon/build' + '?' + role + '&rank=diamond_plus','Diamond+','',argsList[0])
            
            else:
                return
                    
        elif len(argsList) == 3: #3 arguments
            if argsList[0] in rankSet and argsList[1] in regionSet and argsList[2] in roleSet:
                role = roleUrl(argsList[2])
                region = regionUrl(argsList[1])
                if argsList[0] in {'plat','platinum'}:
                    webScrape = WebScraper(region + '&' + role,'',argsList[1],argsList[2])
                else:
                    webScrape = WebScraper(region + '&' + role + '&rank=diamond_plus','Diamond+',argsList[1],argsList[2])
                    
            elif argsList[0] in rankSet and argsList[1] in roleSet and argsList[2] in regionSet:
                role = roleUrl(argsList[1])
                region = regionUrl(argsList[2])
                if argsList[0] in {'plat','platinum'}:
                    webScrape = WebScraper(region + '&' + role,'',argsList[2],argsList[1])
                else:
                    webScrape = WebScraper(region + '&' + role + '&rank=diamond_plus','Diamond+',argsList[2],argsList[1])
                    
            elif argsList[0] in regionSet and argsList[1] in rankSet and argsList[2] in roleSet:
                role = roleUrl(argsList[2])
                region = regionUrl(argsList[0])
                if argsList[1] in {'plat','platinum'}:
                    webScrape = WebScraper(region + '&' + role,'',argsList[0],argsList[2])
                else:
                    webScrape = WebScraper(region + '&' + role + '&rank=diamond_plus','Diamond+',argsList[0],argsList[2])
                    
            elif argsList[0] in regionSet and argsList[1] in roleSet and argsList[2] in rankSet:
                role = roleUrl(argsList[1])
                region = regionUrl(argsList[0])
                if argsList[2] in {'plat','platinum'}:
                    webScrape = WebScraper(region + '&' + role,'',argsList[0],argsList[1])
                else:
                    webScrape = WebScraper(region + '&' + role + '&rank=diamond_plus','Diamond+',argsList[0],argsList[1])
                    
            elif argsList[0] in roleSet and argsList[1] in rankSet and argsList[2] in regionSet:
                role = roleUrl(argsList[0])
                region = regionUrl(argsList[2])
                if argsList[1] in {'plat','platinum'}:
                    webScrape = WebScraper(region + '&' + role,'',argsList[2],argsList[0])
                else:
                    webScrape = WebScraper(region + '&' + role + '&rank=diamond_plus','Diamond+',argsList[2],argsList[0])
                    
            elif argsList[0] in roleSet and argsList[1] in regionSet and argsList[2] in rankSet:
                role = roleUrl(argsList[0])
                region = regionUrl(argsList[1])
                if argsList[2] in {'plat','platinum'}:
                    webScrape = WebScraper(region + '&' + role,'',argsList[1],argsList[0])
                else:
                    webScrape = WebScraper(region + '&' + role + '&rank=diamond_plus','Diamond+',argsList[1],argsList[0])
            
            else: #argument not in a set
                return    
                
        else: #too many arguments
            return
        await ctx.send(webScrape.parse())

#functions here
def regionUrl(args):
    if args == 'kr':
        return 'https://u.gg/lol/champions/talon/build?region=kr'
    elif args == 'na':
        return 'https://u.gg/lol/champions/talon/build?region=na1'
    elif args in {'eu','euw'}:
        return 'https://u.gg/lol/champions/talon/build?region=euw1'
    elif args == 'br':
        return 'https://u.gg/lol/champions/talon/build?region=br1'
    elif args in {'eune','eun'}:
        return 'https://u.gg/lol/champions/talon/build?region=eun1'
    elif args == 'jp':
        return 'https://u.gg/lol/champions/talon/build?region=jp1'
    elif args == 'lan':
        return 'https://u.gg/lol/champions/talon/build?region=la1'
    elif args == 'las':
        return 'https://u.gg/lol/champions/talon/build?region=la2'
    elif args == 'oce':
        return 'https://u.gg/lol/champions/talon/build?region=oc1'
    elif args == 'ru':
        return 'https://u.gg/lol/champions/talon/build?region=ru'
    elif args == 'tr':
        return 'https://u.gg/lol/champions/talon/build?region=tr1'
    
def roleUrl(args):
    if args == 'top':
        return 'role=top'
    elif args in {'jg','jungle'}:
        return 'role=jungle'
    elif args in {'mid','middle'}:
        return 'role=middle'
    elif args in {'adc','bot'}:
        return 'role=adc'
    elif args in {'supp','support'}:
        return 'role=support'
    
def setup(client):
    client.add_cog(GeneralCommands(client))