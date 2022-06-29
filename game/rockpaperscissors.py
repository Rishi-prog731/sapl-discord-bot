@client.command()
async def rps(ctx,message):
  answer = message.lower()
  choices = ["rock","paper","scissors"]
  computer_answer = random.choice(choices)
  if answer not in choices:
    await ctx.send("That is not a valid option; Pick rock, paper, or scissors.")
    return
  else:
    if computer_answer == answer:
      await ctx.send(f"Tie! We both picked {answer}")
    if computer_answer == "rock":
      if answer == "paper":
        await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}!")
    if computer_answer == "paper":
      if answer == "rock":
        await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}!")
    if computer_answer == "scissors":
      if answer == "rock":
        await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}!")
    if computer_answer == "rock":
      if answer == "scissors":
        await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}!")
    if computer_answer == "paper":
      if answer == "scissors":
        await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}!")
    if computer_answer == "scissors":
      if answer == "paper":
        await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}!")
