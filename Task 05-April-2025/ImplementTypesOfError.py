def demonstrate_exceptions():
    try:
        # 1. ZeroDivisionError
        result = 10 / 0

        # 2. ValueError
        num = int("abc")

        # 3. TypeError
        result = "text" + 5

        # 4. IndexError
        my_list = [1, 2, 3]
        item = my_list[5]

        # 5. KeyError
        my_dict = {"name": "Hema"}
        value = my_dict["age"]

        # 6. FileNotFoundError
        with open("non_existing_file.txt", "r") as file:
            content = file.read()

    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero.")

    except ValueError:
        print("ValueError: Invalid conversion from string to integer.")

    except TypeError:
        print("TypeError: Incompatible data types used together.")

    except IndexError:
        print("IndexError: List index is out of range.")

    except KeyError:
        print("KeyError: The specified key does not exist in the dictionary.")

    except FileNotFoundError:
        print("FileNotFoundError: File not found.")

    except Exception as e:
        print(f"Unexpected Error: {e}")

demonstrate_exceptions()
