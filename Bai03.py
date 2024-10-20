#Khởi tạo dictionary
words = {
    "banana": "trái chuối",
    "apple": "trái táo",
    "rose apple": "trái mận"
}
#In từ điển
def display():
    for k,w in words.items():
        print(f"{k} -> {w}")
#Thêm từ vào từ điển
def add_word(key, mean):
    if key not in words:
        words[key] = mean
def count_word():


if __name__ == '__main__':
    display()