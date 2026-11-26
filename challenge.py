import json
def average_from_json(text):
    try:
        nums = json.loads(text)
    except json.JSONDecodeError:
        return 0
    return sum(nums) / len(nums)

print(average_from_json("[80,90]"))
print(average_from_json("[oops]"))