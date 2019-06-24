# sort an array in ascending order
# time: O(n^2)
# space: O(1
def selection_sort(lst):
    for i in range(len(lst) - 1):
        global_min = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[global_min]:
                global_min = j
        lst[i], lst[global_min] = lst[global_min], lst[i]

# Given an array stored in stack 1, sort the number by using additional
# two stacks
def simulate_selection_sort(stack):
    stack_1 = [x for x in stack]
    stack_2 = []
    stack_3 = []
    while stack_1:
        global_min = float('inf')
        for _ in range(len(stack_1)):
            stack_2.append(stack_1.pop())
            if stack_2[-1] < global_min:
                global_min = stack_2[-1]
        for _ in range(len(stack_2)):
            num = stack_2.pop()
            if num == global_min:
                stack_3.append(num)
            else:
                stack_1.append(num)
    return stack_3



if __name__ == '__main__':
    lst = [2, 4, -1, -3, 7]
    res = simulate_selection_sort(lst)
    selection_sort(lst)
    assert res == lst
    print(lst)
