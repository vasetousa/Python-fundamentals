class Party:
    def __init__(self):
        self.people = []


party = Party()

line = input()
while not line == "End":
    party.people.append(line)
    line = input()

total_people_going = len(party.people)
print(f"Going: {', '.join(party.people)}")
print(f"Total: {total_people_going}")
