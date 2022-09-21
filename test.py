import Pengine as pengine

my_object = pengine.create_object(
    name = "Hello",
    size = "250x100",
    color = "green"
)

my_object2 = pengine.create_object(
    name = "Bye",
    size = "21x18",
    color = "blue"
)

pengine.store_object(my_object)
pengine.store_object(my_object2)