import sys
input = sys.stdin.readline

N = int(input())
books = []
books_set = set()

for _ in range(N):
    book = input().rstrip()
    # 책이 없는 경우
    if book not in books_set:
        books.append([1, book])
        books_set.add(book)
    # 책이 있는 경우
    else:
        for i in range(len(books)):
            if books[i][1] == book:
                books[i][0] += 1
                break

books.sort(key=lambda x: (-x[0], x[1]))

print(books[0][1])