# Talon Bot
A discord bot created for the purpose of answering frequently asked questions about the champion Talon in League of Legends. Advice given by the bot is written by several Diamond ranked Talon mains.

Note: A lot of the code is before JSON was utilized. Legacy code is in the process of being switched over to JSON form.

# Commands
Mention Talon Bot with an @. IE: @Talon Bot \<command\>
- Conq
  - Displays the runes that players running Conqueror Talon should take.
- Elec
  - Displays the runes that players running Electrocute Talon should take.
- Lethality
  - Gives a pool of items for the lethality build and suggestions on when to build them.
- Bruiser
  - Gives a pool of items for the bruiser build and suggestions on when to build them.
- Combo
  - A brief video introduction to the most basic Talon combos.
- Skills
  - The ability level order for Talon.
- Start
  - The starting items for Talon.
- Boots
  - Boots options for Talon.
- Matchups
  - Advice on the most common middle lane matchups for Talon. Included matchups are mentioned in the code.
# Stats command
Accesses data from the site https://u.gg and gets Talon's winrate, pickrate, and banrate. Region, rank, and role can be customized by simply adding it after the command. 
IE: @Talon Bot stats NA diamond jg -> returns the stats for Jungle Talon in NA Diamond+.
### Command temporarily suspended
Due to the page source of the website no longer having the key data for the webscraping script, the requests library can no longer be used to accomplish its task. The Selenium framework has to be used to execute the Javascript necessary to obtain the data. While this does work on its own, due to the large memory usage and time delays when deployed on the cloud, it is not viable to have this command run on a discord bot. As such, the command will be suspended until further notice.

The code for it is in the talonBotShelved folder. Simply replace the original files with the ones in the folder.
