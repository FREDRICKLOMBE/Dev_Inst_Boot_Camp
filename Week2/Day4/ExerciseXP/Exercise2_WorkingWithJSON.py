import json
from pathlib import Path

## 🌟 Exercise 2: Working with JSON
# Access a salary, add an employee's birth date and save the updated JSON.


def main():
    """Parse employee JSON, display the salary and save a birth date; return None."""
    # Close the JSON string with triple quotes to correct the starter code.
    sampleJson = """{
        "company": {
            "employee": {
                "name": "emma",
                "payable": {
                    "salary": 7000,
                    "bonus": 800
                }
            }
        }
    }"""

    """ Load the JSON string into a Python dictionary """
    data = json.loads(sampleJson)

    """ Access and display the nested salary """
    salary = data["company"]["employee"]["payable"]["salary"]
    print(salary)  # 7000

    """ Add a birth date to the employee dictionary """
    # Use an example date because the exercise does not provide Emma's birthday.
    data["company"]["employee"]["birth_date"] = "1998-04-15"

    """ Save the modified dictionary to a JSON file """
    output_file = Path(__file__).resolve().parent / "employee.json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        file.write("\n")

    print(f"Modified JSON saved to {output_file.name}")


if __name__ == "__main__":
    """ Run the JSON exercise """
    main()
