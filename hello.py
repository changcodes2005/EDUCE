import random
import math

banner_text = "Welcome to my website! "

rand_num = str(random.randint(1, 100))

operations = ["+", "-", "*", "/"]
rand_operation = random.choice(operations)

expression = rand_num + " " + rand_operation + " " + str(random.randint(1, 100))

result = round(eval(expression), 2)

quotes = ["“Life is like a camera, if things don't work out, take another shot.”",
          "“I have not failed. I've just found 10,000 ways that won't work.”",
          "“The only way to do great work is to love what you do.”",
          "“Success is not final, failure is not fatal: It is the courage to continue that counts.”"]

rand_quote = random.choice(quotes)

banner_text += expression + " = " + str(result) + "  " + rand_quote

print(banner_text)





