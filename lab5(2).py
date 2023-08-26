def access_element(data_list, index):
    try:
        element = data_list[index]
        return element
    except IndexError:
        print("Error: Index out of range.")
        return None

my_list = [1, 2, 3, 4, 5]
index_to_access = 6
result = access_element(my_list, index_to_access)
if result is not None:
    print(f"Element at index {index_to_access}: {result}")
