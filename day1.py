from typing import List

def detect_calibration_value(lst: List[str]) -> int:
    final_value = 0
    for entry in lst:
        first_entry = -1
        last_entry = -1
        for char in entry:
            if char >= '0' and char <= '9':
                first_entry = int(char)
                break
        for char in entry[::-1]:
            if char >= '0' and char <= '9':
                last_entry = int(char)
                break
        
        number = first_entry * 10 + last_entry
        final_value += number
    return final_value

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six":6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis":6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
    "net": 10,
}

def detect_calibration_value_with_alpha(lst: List[str]) -> int:
    final_value = 0
    for entry in lst:
        first_entry = -1
        last_entry = -1
        for index, char in enumerate(entry):
            if char >= '0' and char <= '9':
                first_entry = int(char)
                break
            elif entry[index:index+3] in nums:
                first_entry = nums[entry[index:index+3]]
                break
            elif entry[index:index+4] in nums:
                first_entry = nums[entry[index:index+4]]
                break
            elif entry[index:index+5] in nums:
                first_entry = nums[entry[index:index+5]]
                break
        for index, char in enumerate(entry[::-1]):
            if char >= '0' and char <= '9':
                last_entry = int(char)
                break
            elif entry[::-1][index:index+3] in nums:
                last_entry = nums[entry[::-1][index:index+3]]
                break
            elif entry[::-1][index:index+4] in nums:
                last_entry = nums[entry[::-1][index:index+4]]
                break
            elif entry[::-1][index:index+5] in nums:
                last_entry = nums[entry[::-1][index:index+5]]
                break
            print(index, last_entry)
        number = first_entry * 10 + last_entry
        final_value += number
    return final_value 
if __name__ == "__main__":
    with open("day1/input.txt", "r") as f:
        lst = f.readlines()
    print(detect_calibration_value(lst))
    print(detect_calibration_value_with_alpha(lst))
