import time
import multiprocessing
import cv2


lst_squares = []
lst_cubes = []
def square_nums(numbers):
    global lst_squares
    numbers = list(numbers)
    for num in numbers:
        time.sleep(3)
        print(f"Square of {num} is {num*num}")
        lst_squares.append(num*num)


def cube_nums(numbers):
    global lst_cubes
    numbers = list(numbers)
    for num in numbers:
        time.sleep(3)
        print(f"Cube of {num} is {num*num*num}")
        lst_cubes.append(num*num*num)

if __name__ == '__main__':
    lst = [1,2,3,4]
    p1 = multiprocessing.Process(target=square_nums, args=(lst,))
    p2 = multiprocessing.Process(target=cube_nums, args=(lst,))
    t1 = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    t2 = time.time()
    print("time taken:", t2-t1)

    print(lst_squares, lst_cubes) # empty because each process has its own memory stack and its copies those list onto its own memory

    img = cv2.imread("MemoryStackProcess.JPG")
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






