import random
def ChatBot(input):
    replist=['Emmmmmm','Really?!','And then?','Awesome!']
    return replist[random.randrange(0,4,1)]

if __name__ == "__main__":
    print('Greeting,my lord,what can I do for you?')
    while 1==1:
        shit = input()
        print(ChatBot(shit))
