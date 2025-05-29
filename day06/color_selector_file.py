import sys
import os

def read_colors_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None

def print_menu(colors):
    print("Available colors:")
    for i, color in enumerate(colors, 1):
        print(f"{i}. {color}")

def get_color_by_index(colors, index):
    if 1 <= index <= len(colors):
        return colors[index - 1]
    return None

def get_color_by_name(colors, name):
    name = name.lower()
    if name in colors:
        return name
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python color_selector_file.py <colors_file> [choice]")
        return

    colors_file = sys.argv[1]
    colors = read_colors_from_file(colors_file)
    if not colors:
        return

    selected_color = None
    if len(sys.argv) >= 3:
        arg = sys.argv[2]
        if arg.isdigit():
            selected_color = get_color_by_index(colors, int(arg))
        else:
            selected_color = get_color_by_name(colors, arg)
        if selected_color is None:
            print(f"Invalid color selection: {arg}")
            return
    else:
        print_menu(colors)
        while True:
            choice = input("Enter number or color name: ").strip()
            if choice.isdigit():
                selected_color = get_color_by_index(colors, int(choice))
            else:
                selected_color = get_color_by_name(colors, choice)

            if selected_color:
                break
            else:
                print("Invalid input. Try again.")

    print(f"You selected: {selected_color}")

if __name__ == "__main__":
    main()
