# Creates templates for starting out a codewar kata
# Author: @shailygupta

# Template Structure

import click


@click.command()
@click.option(
    "--function_name", prompt="Function Name:", 
    help="The name of the primary function"
)
def template_create(function_name):
    print("Creating a new file:", f"{function_name}.py ...")
    newfile = open(f"{function_name}.py", "w+")

    newfile.write(
        "# Author: @shailygupta\n"
        f"# {function_name}\n\n\n"
        f"def {function_name}(inputs):\n"
        "pass\n\n\n"
        "if __name__ == \"__main__\":\n"
        f"print({function_name}(\"\"))\n"
        f"print({function_name}(\"\"))\n"
        f"print({function_name}(\"\"))\n\n"
        "# Test Cases\n"
        f'assert {function_name}(\"\") == "", "Should be ___"\n'
        f'assert {function_name}(\"\") == "", "Should be ___"\n'
        f'assert {function_name}(\"\") == "", "Should be ___"\n'
    )

    newfile.close()

    print("File has now been created")


if __name__ == "__main__":
    template_create()
