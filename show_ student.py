# ສ້າງ list ເກັບຂໍ້ມູນນັກສຶກສາ 5 ຄົນ
students = []

# ຮັບຂໍ້ມູນ 5 ຄົນ
for i in range(5):
    print(f"ນັກສຶກສາຄົນທີ່ {i+1}")
    name = input("ຊື່: ")
    age = input("ອາຍຸ: ")
    major = input("ສາຂາ: ")
    print("---------------")
    
    # ເກັບເປັນ dictionary ແລ້ວໃສ່ໃນ list
    students.append({
        "name": name,
        "age": age,
        "major": major
    })

# ສະແດງຂໍ້ມູນນັກສຶກສາທັງ 5 ຄົນ
print("\n------ ຂໍ້ມູນນັກສຶກສາ ------")
for i, stu in enumerate(students, start=1):
    print(f"ນັກສຶກສາຄົນທີ່ {i}")
    print("ຊື່:", stu["name"])
    print("ອາຍຸ:", stu["age"])
    print("ສາຂາ:", stu["major"])
    print("----------------------")