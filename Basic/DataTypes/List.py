# List: Danh sách có thể thay đổi, lưu nhiều phần tử.
print("~~~List~~~")
cars = ["BMW", "Mercedes", "Audi", "Toyota"]
print("List cars:", cars)

## List method
print("~~~List method~~~")
print("Index of first item:" ,cars[0])

print("List had length: ", len(cars))
print("List type:", type(cars))

cars.append("Honda")
print("Added item into list:", cars)

cars.remove("BMW")
print("Removed item from list:", cars)

cars.insert(0, "BMW")
print(cars)
print("--------------------")