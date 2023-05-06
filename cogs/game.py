import random
import disnake
from disnake.ext import commands

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_playing = False
        self.health = 100
        self.score = 0
        self.player_position = (0, 0)
        self.monster_positions = set()
        self.treasure_positions = set()
        self.current_player = None
        self.game_message = None
        self.move_count = 0  # Счетчик ходов игрока

    def generate_map(self):
        # Generate a 10x10 map
        self.monster_positions = set()
        self.treasure_positions = set()

        for _ in range(10):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            self.monster_positions.add((x, y))

        for _ in range(5):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            self.treasure_positions.add((x, y))

    def can_move_up(self):
        return self.player_position[0] > 0

    def can_move_down(self):
        return self.player_position[0] < 9

    def can_move_left(self):
        return self.player_position[1] > 0

    def can_move_right(self):
        return self.player_position[1] < 9

    async def move_monsters(self):
        for monster_position in self.monster_positions.copy():
            x, y = monster_position
            directions = ["up", "down", "left", "right"]
            direction = random.choice(directions)

            if direction == "up" and y > 0:
                self.monster_positions.remove(monster_position)
                self.monster_positions.add((x, y - 1))
            elif direction == "down" and y < 9:
                self.monster_positions.remove(monster_position)
                self.monster_positions.add((x, y + 1))
            elif direction == "left" and x > 0:
                self.monster_positions.remove(monster_position)
                self.monster_positions.add((x - 1, y))
            elif direction == "right" and x < 9:
                self.monster_positions.remove(monster_position)
                self.monster_positions.add((x + 1, y))

    async def move(self, direction):
        if direction == "up" and self.can_move_up():
            self.player_position = (self.player_position[0], self.player_position[1] - 1)
        elif direction == "down" and self.can_move_down():
            self.player_position = (self.player_position[0], self.player_position[1] + 1)
        elif direction == "left" and self.can_move_left():
            self.player_position = (self.player_position[0] - 1, self.player_position[1])
        elif direction == "right" and self.can_move_right():
            self.player_position = (self.player_position[0] + 1, self.player_position[1])



    # Rest of the code remains the same
    
        self.move_count += 1

        if self.move_count % 3 == 0:
            self.generate_treasure()
            
        # Проверка выхода за пределы карты
        if self.player_position[0] < 0:
            self.player_position = (0, self.player_position[1])
        elif self.player_position[0] > 9:
            self.player_position = (9, self.player_position[1])
        elif self.player_position[1] < 0:
            self.player_position = (self.player_position[0], 0)
        elif self.player_position[1] > 9:
            self.player_position = (self.player_position[0], 9)

        await self.move_monsters()

        if self.player_position in self.monster_positions:
            damage = random.randint(10, 20)
            self.health -= damage
            if self.health <= 0:
                await self.game_message.edit(content="Вы проиграли! Игра окончена.")
                self.is_playing = False
            else:
                                await self.update_game_message()
        elif self.player_position in self.treasure_positions:
            score_gain = random.randint(10, 20)
            self.score += score_gain
            self.treasure_positions.remove(self.player_position)
            if self.score >= 100:
                await self.game_message.edit(content="Вы победили! Игра окончена.")
                self.is_playing = False
            else:
                await self.update_game_message()
        else:
            await self.update_game_message()

    def generate_treasure(self):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        self.treasure_positions.add((x, y))
    
    async def update_game_message(self):
        # Update the message with buttons and the game map
        game_text = f"Здоровье: {self.health}\nОчки: {self.score}\n\n"

        for y in range(10):
            for x in range(10):
                if (x, y) == self.player_position:
                    game_text += "👤"
                elif (x, y) in self.monster_positions:
                    game_text += "👾"
                elif (x, y) in self.treasure_positions:
                    game_text += "💰"
                else:
                    game_text += "⬛️"
            game_text += "\n"

        embed = disnake.Embed(title="Игра", description=game_text, color=disnake.Color.green())

        await self.game_message.edit(embed=embed)

    @commands.command()
    async def start(self, ctx):
        if self.is_playing:
            await ctx.send("Игра уже запущена.")
        else:
            self.is_playing = True
            self.health = 100
            self.score = 0
            self.player_position = (0, 0)
            self.generate_map()

            game_text = f"Здоровье: {self.health}\nОчки: {self.score}\n\n"

            for y in range(10):
                for x in range(10):
                    if (x, y) == self.player_position:
                        game_text += "👤"
                    elif (x, y) in self.monster_positions:
                        game_text += "👾"
                    elif (x, y) in self.treasure_positions:
                        game_text += "💰"
                    else:
                        game_text += "⬛️"
                game_text += "\n"

            embed = disnake.Embed(title="Игра", description=game_text, color=disnake.Color.green())
            self.game_message = await ctx.send(embed=embed)

            # Добавление кнопок
            buttons = ["⬅️", "⬆️", "⬇️", "➡️"]
            for button in buttons:
                await self.game_message.add_reaction(button)

            self.current_player = ctx.author

    @commands.command()
    async def stop(self, ctx):
        if not self.is_playing:
            await ctx.send("Игра не запущена.")
        else:
            self.is_playing = False
            await self.game_message.delete()
            await ctx.send("Игра остановлена.")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.current_player and self.is_playing and reaction.message == self.game_message:
            direction = None

            if str(reaction.emoji) == "⬅️":
                direction = "left"
            elif str(reaction.emoji) == "⬆️":
                direction = "up"
            elif str(reaction.emoji) == "⬇️":
                direction = "down"
            elif str(reaction.emoji) == "➡️":
                direction = "right"

            if direction:
                await self.move(direction)

                # Remove user's reaction
                await self.game_message.remove_reaction(reaction, user)

    @commands.Cog.listener()
    async def move_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Ошибка! Пожалуйста, укажите направление хода (up/down/left/right).")

def setup(bot):
    bot.add_cog(Game(bot))

