import requests

def check_interesting_fact(number):
    url = f"http://numbersapi.com/{number}/math?json=true"
    response = requests.get(url)
    data = response.json()
    return "Interesting" if data.get("found") else "Boring"

def main():
    numbers = []
    try:
        while True:
            line = input()
            if line.strip() == "":
                break
            numbers.append(int(line.strip()))
    except EOFError:
        pass

    results = [check_interesting_fact(number) for number in numbers]

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
