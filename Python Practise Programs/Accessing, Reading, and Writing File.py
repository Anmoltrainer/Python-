# Accessing, Reading, and Writing Files in Python:

# Opening a file for reading
file = open("example.txt", "r")

# Opening a file for writing (creates a new file or truncates an existing one)
file = open("output.txt", "w")


# Reading from a File: You can read the contents of a file using methods like read(), readline(), or by iterating through lines.

# Reading the entire file content
content = file.read()

# Reading one line at a time
line = file.readline()


# Writing to a File: You can write data to a file using methods like write() or by iterating and writing lines.

# Writing data to a file
file.write("Hello, World!\n")

# Writing multiple lines
lines = ["Line 1", "Line 2", "Line 3"]
file.writelines(lines)


# Closing a File: After you're done with a file, it's essential to close it using the close() method to release resources.

file.close()


# Using pickle for Object Serialization:

# Storing Objects with pickle:

import pickle

data = {"name": "Alice", "age": 30}

# Serialize and save the object to a file
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

# Retrieving Objects with pickle:

import pickle

# Deserialize and load the object from a file
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)
# Output: {'name': 'Alice', 'age': 30}


