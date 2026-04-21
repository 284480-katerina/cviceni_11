class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def fencing_cost(self, price_per_meter):
        return self.perimeter() * price_per_meter

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self,index):

        score = self.get_by_index(index)

        if 90 <= score:
            return "A"

        elif 80 <= score:
            return "B"

        elif 70 <= score:
            return "C"

        elif 60 <= score:
            return "D"

        else:
            return "F"

    def find(self, hodnota):

        indexy = []

        for i in range(len(self.scores)):
            if self.scores[i] == hodnota:
                indexy.append(i)

        return indexy

    def get_sorted(self):

        scores = self.scores.copy()
        n = len(scores)

        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores




def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())          # 9
    print(results.get_by_index(2))  # 91
    print(results.scores) # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    print(results.get_grade(3))
    print(results.find(100))

    print(results.get_sorted())
    print(results.scores)

    for i in range(results.count()):
        print (f"Student {i}: {results.get_by_index(i)} points - {results.get_grade(i)}")


if __name__ == '__main__':
    main()

