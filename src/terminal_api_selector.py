import requests


def display_menu():
    print("\nSelect an API to use:")
    print("1. OpenAI API")
    print("2. Hugging Face API")
    print("3. Custom API")
    print("4. Exit")


def get_user_choice():
    try:
        choice = int(input("\nEnter your choice (1-4): "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError
        return choice
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 4.")
        return None


def fetch_api_details(choice):
    if choice == 1:
        return "https://api.openai.com/v1/engines"
    elif choice == 2:
        return "https://api-inference.huggingface.co/models"
    elif choice == 3:
        return input("Enter the custom API URL: ")
    else:
        return None


def validate_api(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print("\nAPI is valid and reachable.")
            return True
        else:
            print(f"\nAPI returned status code {response.status_code}.\n"
                  "Please check the URL.")
            return False
    except requests.exceptions.RequestException as e:
        print(f"\nError connecting to the API: {e}")
        return False


def main():
    while True:
        display_menu()
        choice = get_user_choice()
        if choice is None:
            continue
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break

        api_url = fetch_api_details(choice)
        if api_url:
            print(f"\nSelected API: {api_url}")
            if validate_api(api_url):
                print("\nAPI selection successful.\n"
                      "You can now use this API in your system.")
            else:
                print("\nAPI validation failed. Please try again.")


if __name__ == "__main__":
    main()
