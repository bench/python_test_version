
def main():
    original_string = "HelloWorld"
    prefix = "Hello"
    suffix = "World"

    try:
        # Remove the prefix
        without_prefix = original_string.removeprefix(prefix)
        print(f"Original: '{original_string}', without prefix: '{without_prefix}'")

        # Remove the suffix
        without_suffix = original_string.removesuffix(suffix)
        print(f"Original: '{original_string}', without suffix: '{without_suffix}'")
    except AttributeError:
        print("str.removeprefix() and str.removesuffix() are not available in your Python version. They require Python 3.10 or newer.")


if __name__ == '__main__':
   main()