class Student:

    def __init__(self, name="", usn="", score=[0, 0, 0, 0]):
        self.name = name
        self.usn = usn
        self.score = score

    def getMarks(self):
        self.name = input("Enter Student Name: ")
        self.usn = int(input("Enter Student USN: "))

        self.score[0] = int(input("Enter marks in Subject 1: "))
        self.score[1] = int(input("Enter marks in Subject 2: "))
        self.score[2] = int(input("Enter marks in Subject 3: "))

        self.score[3] = self.score[0] + self.score[1] + self.score[2]

    def display(self):
        percentage = self.score[3] / 3

        print("=" * 81)
        print("SCORE CARD DETAILS".center(81))
        print("=" * 81)

        print("%-15s %-12s %-8s %-8s %-8s %-8s %-12s" %
              ("NAME", "USN", "MARKS1", "MARKS2", "MARKS3", "TOTAL", "PERCENTAGE"))

        print("=" * 81)

        print("%-15s %-12s %-8d %-8d %-8d %-8d %-12.2f" %
              (self.name, self.usn, self.score[0], self.score[1],
               self.score[2], self.score[3], percentage))

        print("=" * 81)


def main():
    s1 = Student()
    s1.getMarks()
    s1.display()


main()