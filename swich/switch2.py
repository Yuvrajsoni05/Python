lang = input("Enter Language ")

def switch(lang):
    if lang == 'js':
        return "You Can do JS "
    elif lang == 'python':
        return "You Can do  Python "
    else:
        return "Why ?"



print(switch(lang))