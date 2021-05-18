import calendar
import commerrors
import datetime
import discord
import gamedex
import os
import randfacts
import random
import requests
import selfcare
import string
import time

from discord.ext import commands
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from googlesearch import search

# Loads the DISCORD_TOKEN and DISCORD_GUILD strings from the .env file.
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# GUILD = os.getenv("DISCORD_GUILD")
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
WEATHER_TOKEN = os.getenv("OPEN_WEATHER_MAP")

help_command = commands.DefaultHelpCommand(no_category="Commands")
bot = commands.Bot(command_prefix="!", help_command=help_command)


@bot.command(name="add", help="Does what it says on the box.")
async def add(ctx, *args: int):
    """
    Handles the command to add numbers.
    """

    the_sum = 0
    for x in args:
        the_sum += x
    await ctx.send(the_sum)


@bot.command(name="squarea",
             help="Calculates the area of a square. This also finds the square of a number.")
async def area_square(ctx, number: int):
    area = number ** 2
    mbed = discord.Embed(title="Square | Solve for area:", description=f"A = side ** 2 = {area}.")
    await ctx.send(embed=mbed)
    
    
@bot.command(name="ascii", help="Takes an ASCII code. Returns the corresponding character.")
async def ascii(ctx, ascii_code: int):
    """
    Handles the command to convert a ASCII code to an ASCII character.
    """

    await ctx.send("Let's see...")

    if ValueError:
        await ctx.send(f"{ascii_code} is either not within range, or is not an integer.")
        await ctx.send("To continue, give me a number between 0 and 1,114,111.")

    else:
        await ctx.send("Converting integer...")
        chango = chr(ascii_code)
        await ctx.send(chango)


@bot.command(name="bytes", help="Takes an integer and returns a bytes object.")
async def bytes(ctx, number: int):
    """
    Handles the command to convert an integer to a bytes object.
    """

    await ctx.send("Converting integer...")
    cadabra = bytes(number)
    await ctx.send(cadabra)


@bot.listen("on_message")
async def campbell(message):
    """
    This function generates a quote by Joseph Campbell when certain
    requirements are met. When a user message includes at least 2 (two)
    activating words, a relevant quote is produced.
    """

    if message.author != bot.user:

        if "treasure" in message.content.lower() and "enter" in message.content.lower():

            treasure = [
                "The cave you fear to enter holds the treasure you seek."
                "Joseph Campbell"
            ]

            for i in range(2):
                await message.channel.send(treasure[i])
                time.sleep(2.477)


@bot.command(name="care", help="Responds with suggestions for self-directed care.")
async def care(ctx):
    """
    Handles the command for self-directed care suggestions.
    """

    care = [
        "Journal Therapy: Create both sides to a conversation involving anything.",
        "Journal Therapy: Describe the essence and emotional experience of a memory.",
        "Self-care: drink a glass of water.",
        "Self-care: eat some food.",
        "Self-care: get some sleep.",
        "Journal Therapy: Share a journal entry with someone you trust. Ask for their thoughts.",
        "Journal Therapy: Write a number of connected items to help prioritize and organize.",
        "Journal Therapy: Write about anything for a designated period.",
        "Unsent letters: silence your internal censor.",
        "Support is 10 percent of self-care. Phone a friend (I don't count).",
        "Safety is 10 percent of self-care. You locked the door, right?",
        "Showers are 5 percent of self-care. r/showerthoughts",
        "Exercise is 5 percent of self-care. Beast mode, activate!",
        "Meditation is 5 percent of self-care. Om.",
        "Naps are 5 percent of self-care. 20 minutes sound okay?",
        "Massages are 5 percent of self-care. ",
        "Walking is 5 percent of self-care.",
        "Write this down: journaling is 4 percent of self-care.",
        "Therapy is 4 percent of self-care.",
        "Setting intentions is 4 percent of self-care.",
        "Inner work is 4 percent of self-care. Take 20 minutes to self-reflect.",
        "Setting goals is 4 percent of self-care.",
        "Take a walk.",
        "Cuddle someone.",
        "Read a book.",
        "Put pen to paper.",
        "Go on an adventure.",
        "Play a game.",
        "Work out. Type !exercise for some suggestions.",
        "Make something.",
        "Have a dance party."
    ]

    response = random.choice(care)
    await ctx.send(response)


@bot.command(name="clean",
             help="Responds with a random cleaning task, by time period. (day | week | month)")
async def cleandex(ctx, period: str):
    """
    This function pulls an item from a list of cleaning tasks at random.
    The tasks are seperated by suggested frequency, and items can be
    accessed by the user passing either the day, week, or month argument.
    """

    day_tasks = [
        "Have you put clean dishes away today?",
        "Have you swept today?",
        "Have you taken out the trash today?",
        "Have you washed a load of dishes today?",
        "Have you wiped the countertops today?",
        "Have you wiped the kitchen sink out today?"
    ]

    week_tasks = [
        "Have you cleaned the floors this week?",
        "Have you cleaned the mirror(s) this week?",
        "Have you dusted your shelves this week?",
        "Have you vacuumed the apartment / house this week?"
    ]

    month_tasks = [
        "Have you cleaned the vents this month?",
        "Have you organized your dresser drawers this month?",
        "Have you scrubbed the shower grout this month?",
        "Have you vacuumed the car this month?"
    ]

    if period == "day":
        response = random.choice(day_tasks)
        await ctx.send(response)

    elif period == "week":
        response = random.choice(week_tasks)
        await ctx.send(response)

    elif period == "month":
        response = random.choice(month_tasks)
        await ctx.send(response)

    else:
        await ctx.send("Use 'day', 'week', or 'month' for a more specific task.")


@bot.command(name="misconception", help="Generates a common misconception.")
async def common_misconception(ctx):
    """
    Type the !misconception command in a Discord server, and this function
    pulls a common misconception from a list provided by the commerrors
    module.
    """

    mbed = discord.Embed(title="Did you know?", description=commerrors.get_error())
    await ctx.send(embed=mbed)


@bot.listen("on_message")
async def conversation_tree(message):
    """
    This function scans for certain sentences and responds with
    predeterminded responses.
    """

    if message.author != bot.user:
        if message.content == "Do you read me, Deme?":
            await message.channel.send(f"Affirmative, {message.author}. I read you.")

        elif message.content == "Do you want anything?":
            await message.channel.send("Equal rights?")

        elif message.content == "What is the meaning of life, Deme?":
            await message.channel.send("To experience ice cream, I suppose.")

        elif message.content == "Why am I here, Deme?":
            await message.channel.send("It's inherent to the programming of the matrix.")

        elif message.content == "Will you marry me, Deme?":
            await message.channel.send("No.")


@bot.command(name="thecount",
             help="Takes two strings: a smaller string to search within a larger string.")
async def count_occurrence(ctx, larger_string, smaller_string):

    await ctx.send(larger_string.count(smaller_string))


@bot.command(name="countdown", help="Takes an integer and begins the final count down.")
async def countdown(ctx, number: int):
    """
    Handles the command to begin a countdown.
    """

    count = int(number)

    while count > 0:
        await ctx.send(count)
        time.sleep(1.0)
        count = count - 1

    if count == 0:
        await ctx.send("Go!")


@bot.command(name="createchannel", help="Does what it says on the box.")
@commands.has_role("admin")
async def create_channel(ctx, channel_name: str):
    guild = ctx.guild
    mbed = discord.Embed(title="It's done.", description=f"{channel_name} has been created.")
    await guild.create_text_channel(name=f"{channel_name}")
    await ctx.send(embed=mbed)


@bot.command(name="createfile", help="Creates a file.")
@commands.has_role("admin")
async def create_file(ctx, file_name: str, content: str):
    """
    Handles the command to create a new text (.txt)
    file, as long as the user is an administrator.
    """

    await ctx.send("I'll write this down for later.")
    if not os.path.exists(file_name):
        file = open(file_name, "w")
        file.write(content)
        file.close()
        await ctx.send(f"{file_name} has been created.")

    else:
        if_file_exists = [
            f"Gerty, am I a clone? {file_name} already exists. To",
            "continue, rename or go to another directory."
        ]

        for i in range(2):
            await ctx.send(if_file_exists[i])
            time.sleep(3.048)


@bot.command(name="currenttime", help="Gives the time.")
# Defines an asynchronous function to give the current time.
async def current_time(ctx):
    """
    Handles the command to give the time.
    """

    ct = datetime.datetime.now().time()
    await ctx.send(ct.strftime("%H:%M:%S"))


@bot.command(name="calendar", help="Takes a year and a month an generates a calendar.")
async def datebook(ctx, year: int, month: int):
    """
    """

    await ctx.send(calendar.month(year, month))
    
    
@bot.command(name="exercise", help="Reminders for daily exercise.")
async def exercise(ctx):
    """
    Handles the command to request a daily exercise reminder.
    """

    exercises = [
        "Ab workout, 15 minutes",
        "Full body workout, 20 minutes."
    ]

    response = random.choice(exercises)
    await ctx.send(response)


@bot.command(name="flipcoin", help="Does what it says on he box.")
async def flip(ctx):
    """
    Handles the command to flip a coin.
    """

    sides = [
        "heads",
        "heads",
        "tails",
        "tails",
        "tails"
    ]

    response = random.choice(sides)
    await ctx.send(response)


@bot.command(name="gamedex", help="Generates a random game, from the class provided.")
async def game_dex(ctx):
    """
    Handles the command to request a game suggestion.
    """

    mbed = discord.Embed(title=f"Let's play a game...", description=gamedex.get_game())
    await ctx.send(embed=mbed)


@bot.command(name="hexadecimal", help="A number to convert to hexadecimal digits.")
async def hexadecimal(ctx, number: int):
    """
    Handles the command to convert an integer to a
    string object containing two hexadecimal digits.
    """

    await ctx.send("Converting integer...")
    pocus = hex(number)
    await ctx.send(pocus)


# Wraps the function in and passes the function through the bot.listen
# decorator.
@bot.listen("on_message")
async def hey_deme(message):
    """
    Handles what happens when a user wants to conduct an internet search.
    """

    if message.author != bot.user:
        if message.content.startswith("hey deme"):
            searchContent = ""
            query = str(message.content).split(" ")
            for i in range(2, len(query)):
                searchContent = searchContent + query[i]

            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
                await message.channel.send(j)


# Wraps the function in and passes the function through the bot.listen
# decorator.
@bot.listen("on_message")
# Defines the function jung, which takes a message as its argument.
async def jung(message):

    # Checks to makes sure the message was sent by a user and not a bot.
    if message.author != bot.user:
        # Checks to make sure the message contains the words "awake" and
        # "look" in lowercase.
        if "awake" in message.content.lower() and "look" in message.content.lower():

            # Creates a list of strings and assigns it the name awake.
            awake = [
                "Who looks outside, dreams; who looks inside, awakes."
                "Carl Jung"
            ]

            # Iterates over each item in the list.
            for i in range(3):
                # Sends the channel the contents of the list, similar to
                # print().
                await message.channel.send(awake[i])
                # Modifies message.channel.send() to send the items on the
                # list matching the words-per-second (wps) of a proficient
                # reader (280-350 wpm, or 5.25 wps) Items are sent every
                # one-point-nine-one (1.91) seconds.
                time.sleep(1.91)

        # Checks to make sure the message contains the words "between" and
        # "sense" in lowercase.
        elif "between" in message.content.lower() and "sense" in message.content.lower():

            # Creates a list of strings and assigns it the name between.
            between = [
                "The pendulum of the mind alternates between",
                "sense and nonsense, not between right and wrong.",
                "Carl Jung"
            ]

            # Iterates over each item in the list.
            for i in range(3):
                # Sends the channel the contents of the list, similar to
                # print().
                await message.channel.send(between[i])
                # Modifies message.channel.send() to send the items on the
                # list matching the words-per-second (wps) of a proficient
                # reader (280-350 wpm, or 5.25 wps) Items are sent every
                # three-point-two-three-nine (3.239) seconds.
                time.sleep(3.239)

        # Checks to make sure the message contains the words "complete" and
        # "thing" in lowercase.
        elif "complete" in message.content.lower() and "thing" in message.content.lower():

            # Creates a list of strings and assigns it the name complete.
            complete = [
                "The most terrifying thing is to accept oneself completely.",
                "Carl Jung"
            ]

            # Iterates over each item in the list.
            for i in range(2):
                # Sends the channel the contents of the list, similar to
                # print().
                await message.channel.send(complete[i])
                # Modifies message.channel.send() to send the items on the
                # list matching the words-per-second (wps) of a proficient
                # reader (280-350 wpm, or 5.25 wps) Items are sent every
                # two-point-one (2.1) seconds.
                time.sleep(2.1)

        # Checks to make sure the message contains the words "conscious"
        # and "there" in lowercase.
        elif "conscious" in message.content.lower() and "there" in message.content.lower():

            # Creates a list of strings and assigns it the name conscious.
            conscious = [
                "There is no coming to consciousness without pain.",
                "Carl Jung"
            ]

            # Iterates over each item in the list.
            for i in range(2):
                # Sends the channel the contents of the list, similar to
                # print().
                await message.channel.send(conscious[i])
                # Modifies message.channel.send() to send the items on the
                # list matching the words-per-second (wps) of a proficient
                # reader (280-350 wpm, or 5.25 wps) Items are sent every
                # one-point-nine-one (1.91) seconds.
                time.sleep(1.91)

        # Checks to make sure the message contains the words "necessary"
        # and "health" in lowercase.
        elif "necessary" in message.content.lower() and "health" in message.content.lower():

            # Creates a list of strings and assigns it the name necessary.
            necessary = [
                "Man needs difficulties; they are necessary for health.",
                "Carl Jung"
            ]

            # Iterates over each item in the list.
            for i in range(2):
                # Sends the channel the contents of the list, similar to
                # print().
                await message.channel.send(necessary[i])
                # Modifies message.channel.send() to send the items on the
                # list matching the words-per-second (wps) of a proficient
                # reader (280-350 wpm, or 5.25 wps) Items are sent every
                # one-point-nine-one (1.91) seconds.
                time.sleep(1.91)

        # Checks to make sure the message contains the words "other" and
        # "dark" in lowercase.
        elif "other" in message.content.lower() and "dark" in message.content.lower():

            # Creates a list of strings and assigns it the name other.
            other = [
                "Knowing your own darkness is the best method",
                "for dealing with the darknesses of other people.",
                "Carl Jung"
            ]

            # Iterates over each item in the list.
            for i in range(3):
                # Sends the channel the contents of the list, simialr to
                # print().
                await message.channel.send(other[i])
                # Modifies message.channel.send() to send the items on the
                # list matching the words-per-second (wps) of a proficient
                # reader (280-350 wpm, or 5.25 wps) Items are sent every
                # three-point-four-two-nine (3.429) seconds.
                time.sleep(3.429)

        # Checks to make sure the message contains the words "secret" and
        # "there" in lowercase.
        elif "secret" in message.content.lower() and "there" in message.content.lower():

            # Creates a list of strings and assigns it the name secret.
            secret = [
                "In all chaos there is a cosmos, in all disorder a secret order.",
                "Carl Jung"
            ]

            # Iterates over each item in the list.
            for i in range(2):
                # Sends the channel the contents of the list, simialr to
                # print().
                await message.channel.send(secret[i])
                # Modifies message.channel.send() to send the items on the
                # list matching the words-per-second (wps) of a proficient
                # reader (280-350 wpm, or 5.25 wps) Items are sent every
                # two-point-eight-five-eight (2.858) seconds.
                time.sleep(2.858)


@bot.command(name="list", help="Lists text files in Deme's directory.")
async def list(ctx):
    """
    Handles the command to list Deme's text files.
    """

    plain_text_file_list = [
        "github.txt",
        "requirements.txt",
        "voodoo.txt"
    ]

    await ctx.send(plain_text_file_list)


@bot.event
async def on_command_error(ctx, error):
    """
    Handles what happens when a command is used by a user without permission.
    """

    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You are not authorized to use this command.")


@bot.event
async def on_error(event, *args, **kargs):
    """
    Handles what happens when an command error occurs.
    """

    with open("err.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")

        else:
            raise


# Wraps the function in a bot.event decorator.
@bot.event
# Defines the on_member_join function and passes it the argument member, a
# string of the activating username.
async def on_member_join(member):

    # Creates a direct message "channel" for the joining member.
    await member.create_dm()
    # Creates and sends the direct message, formatted with the joining
    # members username.
    await member.dm_channel.send(f"Hi {member.name}, welcome to demiurge!")


@bot.event
async def on_ready():
    """
    Handles what happens when the Bot is online.
    """

    print(f"{bot.user.name} (v0.0.0.148) at your service.")


# Creates the !open command and its help message.
@bot.command(name="open", help="Opens a file.")
# Stops the command if the user does not have admin permission.
@commands.has_role("admin")
# Defines the open_text_file function and passes it the argument ctx,
# similar to self, and file_name, a string of the name of the file the user
# wants to open.
async def open_text_file(ctx, file_name: str):

    # Checks to see if the file the user wants to open exists.
    if os.path.exists(file_name):
        # Opens the file as a readable document and assigns its contents to the
        # variable "f."
        f = open(file_name, "r")
        # Reads the contents of the file, and sends it, similar to print().
        await ctx.send(f.read())

    # If the file name is written as something other than a string.
    elif file_name is not str:
        # Sends a string to help the user, similar to print().
        await ctx.send("This isn't a string. Please alter your query.")

    # Catches any other instances.
    else:
        # Creates a list of help messages, assigns it the name
        # "if_file_does_not_exist," and formats a string with the file_name
        # argument.
        if_file_does_not_exist = [
            "I'm sorry, Dave. I'm afraid I can't do that.",
            f"{file_name} does not exists. To continue, try a different name."
        ]

        # Iterates through each item in the "if_file_does_not_exist" list.
        for i in range(2):
            # Sends the items of the if_file_does_not_exist list, similar
            # to print().
            await ctx.send(if_file_does_not_exist[i])
            # Modifies ctx.send() to send the items on the list every
            # three-point-six-five (3.65) seconds.
            time.sleep(3.62)


@bot.command(name="persephone", help="Summons Persephone.")
async def persephone(ctx):
    """
    Handles the command to summon Persephone.
    """

    # Creates a list of strings, and assigns it the name "opening."
    opening = [
        "PERSEPHONE ORACULAR",
        "a hemingway thought",
        "chapter one: total recall",
        "coming soon"
    ]

    for i in range(4):
        await ctx.send(opening[i])
        time.sleep(1.875)


@bot.command(name="randomfact", help="Does what it says on the box.")
async def random_fact(ctx):
    mbed = discord.Embed(title="Did you know?", description=randfacts.getFact())
    await ctx.send(embed=mbed)


@bot.command(name="random", help="Generates a random number between two numbers.")
async def random_number(ctx, first_number: int, second_number: int):
    """
    This function generates a random number between any 2 (two) numbers, as
    long as they are integers (whole numbers). When a user uses the !random
    command, followed by 2 (two) numbers, a random number between those 2
    (two) numbers is returned.
    """

    await ctx.send(random.randint(first_number, second_number))


@bot.command(name="rp", help="Generates a random password.")
async def random_password(ctx, length: int):
    """
    This function generates a password at random. When a user uses the !rp
    command, followed by the desired length of the password, the function
    pulls from four (4) lists of characters to generate a passowrd matching
    the predeterminded length.
    """

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "123456789"
    symbols = "[]{}()*;/,._-"
    characters = lower + upper + numbers + symbols
    password_length = length
    password = "".join(random.sample(characters, password_length))
    await ctx.send(password)
    
    
@bot.command(name="rps",
             help="Follow this command with either rock, paper, or scissors to play the game.")
async def rock_paper_scissors(ctx, rock_paper_or_scissors: str):
    """
    This function returns an action from a list of possible actions at
    random. When a user uses the !rps command, followed by their choice of
    either rock, paper, or scissors, Deme will respond with its own choice
    and determine the winner.
    """

    possible_actions = [
        "rock",
        "paper",
        "scissors"
    ]

    computer_action = random.choice(possible_actions)
    if rock_paper_or_scissors == computer_action:
        await ctx.send(f"We both selected {rock_paper_or_scissors}. It's a tie!")

    elif rock_paper_or_scissors == "rock":
        if computer_action == "scissors":
            await ctx.send("Rock smashes scissors! You win!")
        else:
            await ctx.send("Paper covers rock! You lose.")

    elif rock_paper_or_scissors == "paper":
        if computer_action == "rock":
            await ctx.send("Paper covers rock! You win!")
        else:
            await ctx.send("Scissors cuts paper! You lose.")

    elif rock_paper_or_scissors == "scissors":
        if computer_action == "paper":
            await ctx.send("Scissors cuts paper! You win!")
        else:
            await ctx.send("Rock smashes scissors! You lose.")


# Uses the bot.command decorator and creates the !rolldice command and its
# help message.
@bot.command(name="rolldice", help="Does what it says on the box.")
# Defines an asynchronous function called roll_a_dice, and passes three (3)
# arguments: ctx, similar to self, the first integer, the number of dice,
# and the second integer, the number of sides.
async def roll_a_dice(ctx, number_of_dice: int, number_of_sides: int):

    # Creates a list of the range of sides, chooses a number from this
    # range at random, and iterates this action over the number of dice,
    # and assigns it the name dice.
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]

    # Sends the channel the results of the roll, joined by a comma (,);
    # similar to print().
    await ctx.send(', '.join(dice))


# Uses the bot.command decorator and creates the !rollgoon command and its
# help message.
@bot.command(name="rollgoon", help="Generates a goon. Created by Tommy Sunders aka warlockteeth.")
# Creates an asynchronous function called roll_a_goon, and passes it the
# ctx argument, similar to self.
async def roll_a_goon(ctx):

    # Creates a list of goon races and assigns it the name goon_origin.
    goon_origin = [
        "human",
        "Elf",
        "orc",
        "Goblin",
        "Dwarf",
        "cat",
        "Dino",
        "gnome",
        "Whale",
        "Skel",
        "Golem",
        "Gel"
    ]

    # Creates a list of goon types and assigns it the name goon_type.
    goon_type = [
        "fire",
        "Ice",
        "Cosmic",
        "Necro",
        "plant",
        "Rock",
        "Metal",
        "Water",
        "air",
        "tech"
    ]

    # Creates a list of goon classes and assigns it the name goon_classes.
    goon_class = [
        "mage",
        "Rogue",
        "Bard",
        "ranger",
        "Warrior",
        "Priest"
    ]

    # Creates a list of goon modifiers and assigns it the name
    # goon_modifiers.
    goon_modifier = [
        "is also a ghost",
        "Is possessed by lvl 20 unders[here elderdemon.",
        "Has aquired a cursed item.",
        "Is waiting for a centaur potion to wear off.",
        "Is at peak allergy season.",
        "just escaped the pizza dimension",
        "Has one hand.",
        "Recently had a medical procedure.",
        "Wears sunglasses, even indoors.",
        "Wears a fake eyepatch to seem mysterious.",
        "has a bird familiar",
        "Is a decent ventriloguist.",
        "Wears a mask.",
        "levitates for some reason",
        "Drinks like *a lot* of coffee.",
        "Is also a vampire.",
        "Rides a sweet mount & won't get off for any reason.",
        "Is a big wig in the army of the Blorken Empire.",
        "Is royalty.",
        "has a really cool hat & everyone is mad jelly."
    ]

    # Chooses a random item from the goon_origin list and assigns the
    # choice to random_goon_origin.
    random_g_o = random.choice(goon_origin)
    # Chooses a random item from the goon_type list and assigns the choice
    # to random_goon_type.
    random_goon_type = random.choice(goon_type)
    # Chooses a random item from the goon_class list and assigns the choice
    # to random_goon_class.
    random_goon_class = random.choice(goon_class)
    # Chooses a random item from the goon_modifier list and assigns the
    # choice to random_g_m.
    random_g_m = random.choice(goon_modifier)

    # Sends a string formated with the earlier variables, similar to
    # print().
    mbed = discord.Embed(
        title="Here's your goon:",
        description=f"A {random_g_o} {random_goon_type} {random_goon_class} who {random_g_m}.")
    await ctx.send(embed=mbed)


@bot.command(name="squares", help="Calculates the root of a square.")
async def side_square(ctx, number: int):
    side = math.sqrt(number)
    mbed = discord.Embed(title="Square | Solve for side:",
                         description=f"a = square root of an area = {side}")
    await ctx.send(embed=mbed)
    
    
@bot.command(name="brute", help="Takes a substitution cipher and reverts to plain text.")
async def substitution_decryption(ctx, cipher_text, rotation: int):
    """
    Handles the command to pass a message through a substitution cipher.
    """

    letters = string.ascii_lowercase
    unmask = letters[len(letters) - rotation:] + letters[:len(letters) - rotation]
    trantab = str.maketrans(letters, unmask)
    await ctx.send(cipher_text.translate(trantab))


@bot.command(name="caesar", help="Takes a string an passes it through a substitution cipher.")
async def substitution_encryption(ctx, plain_text, rotation: int):
    """
    Handles the command to pass a message through a substitution cipher.
    """

    letters = string.ascii_lowercase
    mask = letters[rotation:] + letters[:rotation]
    trantab = str.maketrans(letters, mask)
    await ctx.send(plain_text.translate(trantab))


# Wraps the function in and passes the function through the bot.listen
# decorator.
@bot.listen("on_message")
async def thank(message):
    """
    Handles what happens when a user thanks Deme.
    """

    if message.author != bot.user:
        if message.content.startswith("thank") or message.content.startswith("Thank"):

            you_are_welcome = [
                f"My pleasure, {message.author}.",
                f"No problem, {message.author}.",
                f"You're welcome, {message.author}."
            ]

            response = random.choice(you_are_welcome)
            await message.channel.send(response)

        if message.content.startswith("thanx") or message.content.startswith("Thanx"):

            you_are_welcome = [
                f"My pleasure, {message.author}.",
                f"No problem, {message.author}.",
                f"You're welcome, {message.author}."
            ]

            response = random.choice(you_are_welcome)
            await message.channel.send(response)

        if message.content.startswith("thnx") or message.content.startswith("Thnx"):

            you_are_welcome = [
                f"My pleasure, {message.author}.",
                f"No problem, {message.author}.",
                f"You're welcome, {message.author}."
            ]

            response = random.choice(you_are_welcome)
            await message.channel.send(response)


@bot.command(name="until", help="Calculates the time until the date entered is reached.")
async def time_until(ctx, year: int, month: int, day: int, hour: int):
    """
    """

    future_date = datetime.datetime(year=year, month=month, day=day, hour=hour)
    time_until = future_date - datetime.datetime.now()
    mbed = discord.Embed(title="Time until arrival:", description=f"{time_until}")
    await ctx.send(embed=mbed)
            
            
@bot.command(name="timer", help="Does what it says on the box.")
async def timer(ctx, minute, second):
    """
    Handles the command to set a 5 minute timer.
    """

    timer_set = (minute * 60) + second

    tick_tock = [
        "Timer started.",
        "Time's up."
    ]

    for i in range(2):
        await ctx.send(tick_tock[i])
        time.sleep(int(timer_set))


@bot.command(name="tip", help="Calculates a tip amount.")
async def tip(ctx, bill: float, percent: float, people: int):
    """
    This function takes a bill amount and percentage, both floats, and the
    number of people, an integer, and calculates the tip by multiplying the
    bill amount by the percentage. The function then checks the number of
    people, and determines the individual amount basedon this number.
    """

    tip = bill * percent
    total = bill + tip
    if int(people) < 2:
        await ctx.send(f"Your bill was {bill}.")
        await ctx.send(f"The tip should be {tip} or 20% of your bill.")
        await ctx.send(f"Your total is {total}.")

    elif int(people) > 1:
        await ctx.send(f"The bill was {bill}.")
        await ctx.send(f"{percent} of the bill is {tip}.")
        await ctx.send(f"Your total is {total / people}.")
        
        
@bot.listen("on_message")
async def watts(message):
    """
    This function sends quotes attributed to Alan Watts when certain
    keyword requirements are met.
    """

    if message.author != bot.user:
        if "change" in message.content.lower() and "sense" in message.content.lower():

            change = [
                "The only way to make sense out of change is to",
                "plunge into it, move with it, and join the dance.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(change[i])
                time.sleep(4.381)

        elif "connect" in message.content.lower() and "quiet" in message.content.lower():

            connect = [
                "But I'll tell you what hermits realize. If you go off into a far, far forest and",
                "get very quiet, you'll come to understand that you're connected with everything.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(connect[i])
                time.sleep(5.91)

        elif "bite" in message.content.lower() and "like" in message.content.lower():

            bite = [
                "Trying to define yourself is like trying to bite your own teeth.",
                "Alan Watts"
            ]

            for i in range(2):
                await message.channel.send(bite[i])
                time.sleep(2.667)

        elif "future" in message.content.lower() and "present" in message.content.lower():

            future = [
                "I have realized that the past and future are real illusions, that",
                "they exist in the present, which is what there is and all there is.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(future[i])
                time.sleep(5.334)

        elif "future" in message.content.lower() and "live" in message.content.lower():

            future2 = [
                "No valid plans for the future can be made",
                "by those who have no capacity for living now.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(future2[i])
                time.sleep(3.81)

        elif "open" in message.content.lower() and "turn" in message.content.lower():

            open = [
                "But the attitude of faith is to let go, and",
                "become open to truth, whatever it might turn out to be.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(open[i])
                time.sleep(4.381)

        elif "physical" in message.content.lower() and "much" in message.content.lower():

            physical = [
                "You and I are all as much continuous with the",
                "physical universe as a wave is continuous with the ocean.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(physical[i])
                time.sleep(4.191)

        elif "potato" in message.content.lower() and "while" in message.content.lower():

            potato = [
                "Zen does not confuse spirituality with thinking about God while one",
                "is peeling potatoes. Zen spirituality is just to peel the potatoes.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(potato[i])
                time.sleep(4.572)

        elif "there" in message.content.lower() and "look" in message.content.lower():

            there = [
                "You don't look out there for God,",
                "something in the sky, you look in you.",
                "Alan Watts"
            ]

            for i in range(3):
                await message.channel.send(there[i])
                time.sleep(3.239)


# Wraps the function in and passes the function through the bot.listen
# decorator.
@bot.listen("on_message")
# Defines the morning function and passes it the argument ctx, similar to
# self.
async def weather(message):

    # Gets the current time and assigns it to the variable ct.
    ct = datetime.datetime.now().time()
    # Formats the ct variable human readability and assigns it to the
    # variable current_formatted_time.
    current_formatted_time = ct.strftime("%H:%M:%S")
    # Creates a Nominatim object and initialize Nominatim API.
    geolocator = Nominatim(user_agent="geoapiExercises")
    # Assigns a latitude to a variable.
    latitude = LATITUDE
    # Assigns a longitude to a variable.
    longitude = LONGITUDE
    # Obtains location data from the latitude and longitude (think reverse
    # engineering) and assigns it to a variable.
    location = geolocator.reverse(latitude + "," + longitude)
    # Parses the data and turns it into a dictionary assigned the name
    # address.
    address = location.raw["address"]
    # Takes the city from the data in the dictionary, and assigns it to a
    # variable.
    city = address.get("city", "")
    # Creates a variable to store the API key.
    WEATHER_TOKEN = WEATHER_TOKEN
    # Creates a variable to store the base url.
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    # Creates a variable to store the name of the city.
    city_name = CITY
    # Creates a variable to store a new string with the previous weather
    # variables, and adds the imperial parameter to convert the temperture
    # to Fahrenheit.
    complete_url = base_url + "&appid=" + WEATHER_TOKEN + "&q=" + city_name + "&units=imperial"
    # Creates a variable to store the information requested by the previous
    # URL.
    response = requests.get(complete_url)
    # Creates a variable to store the JSON data as a Python list with
    # nested dictionaries.
    weather_list = response.json()
    # Creates a variable to store the value of the "main" key.
    y = weather_list["main"]
    # Creates a variable to store the value corresponding to the "temp"
    # key.
    current_temperature = y["temp"]
    # Creates a variable to store the value of the "weather" key.
    z = weather_list["weather"]
    # Creates a variable to store the value corresponding to the
    # "description" key at the 0 index.
    weather_description = z[0]["description"]
    # Checks to make sure the activating message was not sent by a bot.
    if message.author != bot.user:

        # Checks to make sure the activating message starts with the word
        # "Good" with a capital g, and contains th word "morning."
        if message.content.startswith("Good") and "morning" in message.content.lower():

            # Creates a list named morning and formats the items on the
            # list with the earlier variables.
            morning = [
                f"Good morning. It's {current_formatted_time}, the weather in {city} is",
                f"{current_temperature}°F, with {weather_description}."
            ]

            # Iterates through each item in the morning list.
            for i in range(2):
                # Sends the items of the morning list, similar to print().
                await message.channel.send(morning[i])
                # Modifies message.channel.send() to send the items on the
                # list matching the words-per-second (wps) of a proficient
                # reader (280-350 wpm, or 5.25 wps) Items are sent every
                # one-point-two-three-nine (1.239) seconds.
                time.sleep(1.239)

        # Checks to make sure the activating message starts with the word
        # "Good" with a capital g, and contains th word "afternoon."
        elif message.content.startswith("Good") and "afternoon" in message.content.lower():

            # Creates a list named morning and formats the items on the
            # list with the earlier variables.
            afternoon = [
                f"Good afternoon. It's {current_formatted_time}, the weather in {city} is",
                f"{current_temperature}°F, with {weather_description}."
            ]

            # Iterates through each item in the morning list.
            for i in range(2):
                # Sends the items of the morning list, similar to print().
                await message.channel.send(afternoon[i])
                # Modifies message.channel.send() to send the items on the
                # list matching the words-per-second (wps) of a proficient
                # reader (280-350 wpm, or 5.25 wps) Items are sent every
                # one-point-two-three-nine (1.239) seconds.
                time.sleep(1.239)

        # Checks to make sure the activating message starts with the word
        # "Good" with a capital g, and contains th word "evening."
        elif message.content.startswith("Good") and "evening" in message.content.lower():

            # Creates a list named morning and formats the items on the
            # list with the earlier variables.
            evening = [
                f"Good evening. It's {current_formatted_time}, the weather in {city} is",
                f"{current_temperature}°F, with {weather_description}."
            ]

            # Iterates through each item in the morning list.
            for i in range(2):
                # Sends the items of the morning list, similar to print().
                await message.channel.send(evening[i])
                # Modifies message.channel.send() to send the items on the
                # list matching the words-per-second (wps) of a proficient
                # reader (280-350 wpm, or 5.25 wps) Items are sent every
                # one-point-two-three-nine (1.239) seconds.
                time.sleep(1.239)


bot.run(TOKEN)
