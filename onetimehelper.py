def subletter(a, b):
    a = a.lower()
    b = b.lower()

    c = chr(ord(a) - (ord(b) - ord('a') + 1)) 
    if ord(c) < ord('a'):
        c = ord('z') + (ord(c) - ord('a')) + 1
        c = chr(c)
    return c

def addletter(a, b):
    a = a.lower()
    b = b.lower()

    c = chr(ord(a) + ord(b) - ord('a') + 1) 
    if ord(c) > ord('z'):
        c = ord(c) - ord('z') + ord('a') - 1
        c = chr(c)
    return c

class otp:
    def __init__(self):
        self.messages = []
        self.onetimepad = "rhv"

    def addmsg(self, message):
        self.messages.append(message)

    def add_to_pad(self, a):
        self.onetimepad += a.lower()

    def printmsgs(self):
        for msg in self.messages:
            for i in range(0, len(self.onetimepad)):
                print(subletter(msg[i], self.onetimepad[i]), end="")
            print()
        if len(self.onetimepad) < len(self.messages[1]):
            for msg in self.messages:
                print(msg[len(self.onetimepad)])

    def printkey(self):
        print(self.onetimepad)


if __name__ == "__main__":
    solve = otp()
    solve.addmsg("LpaGbbfctNiPvwdbjnPuqolhhtygWhEuafjlirfPxxl")
    solve.addmsg("WdafvnbcDymxeeulWOtpoofnilwngLhblUfecvqAxs")
    solve.addmsg("UijMltDjeumxUnbiKstvdrVhcoDasUlrvDypegublg")
    solve.addmsg("LpaAlrhGmjikgjdmLlcsnnYmIsoPcglaGtKeQcemiu")
    solve.addmsg("LpaDohqcOzVbglebjPdTnoTzbyRbuwGftflTliPiqp")
    solve.printmsgs()
    while True:
        command = input('>: ')
        command = command.split(" ")
        if command[0] == "+":
            print(addletter(command[1], command[2]))
        elif command[0] == "-":
            print(subletter(command[1], command[2]))
        elif command[0] == "add":
            solve.add_to_pad(command[1])
            solve.printmsgs()
        elif command[0] == "print":
            solve.printkey()
        else:
            solve.printmsgs()
