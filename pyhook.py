import requests, time, os
from pystyle import Colors, Colorate, Center, System

ascii_art = ''' 
$$$$$$╗ $$╗   $$╗$$╗  $$╗ $$$$$$╗  $$$$$$╗ $$╗  $$╗
$$╔══$$╗╚$$╗ $$╔╝$$║  $$║$$╔═══$$╗$$╔═══$$╗$$║ $$╔╝
$$$$$$╔╝ ╚$$$$╔╝ $$$$$$$║$$║   $$║$$║   $$║$$$$$╔╝ 
$$╔═══╝   ╚$$╔╝  $$╔══$$║$$║   $$║$$║   $$║$$╔═$$╗ 
$$║        $$║   $$║  $$║╚$$$$$$╔╝╚$$$$$$╔╝$$║  $$╗
╚═╝        ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                           
'''

System.Title("pyhook")
os.system('cls' if os.name == 'nt' else 'clear')

banner = Colorate.Vertical
print(banner(Colors.cyan_to_blue, Center.XCenter(ascii_art)))

gradient = Colorate.Vertical

def log(message):
    print(gradient(Colors.blue_to_cyan, message))

def get_input(prompt):
    return input('\n' + gradient(Colors.blue_to_cyan, prompt + ' >>') + ' ')

def validate_webhook(url):
    try:
        return requests.get(url).status_code == 200
    except:
        return False

def change_webhook_name(url):
    name = get_input("enter new webhook name")
    res = requests.patch(url, json={"name": name})
    if res.status_code == 200:
        log("    changed name successfully")
    else:
        log("    failed...")

def spam_webhook(url):
    msg = get_input("    enter message to spam")
    try:
        delay = float(get_input("delay in ms? ")) / 1000
    except:
        log("invalid delay")
        return
    log("spam started ; ctrl+c to stop")
    try:
        while True:
            requests.post(url, json={"content": msg})
            time.sleep(delay)
    except KeyboardInterrupt:
        log("\nspamming stopped")

def delete_webhook(url):
    confirm = get_input("are you sure (y/n)")
    if confirm.lower() == "y":
        res = requests.delete(url)
        if res.status_code == 204:
            log("deleted")
        else:
            log("failed")
        input(gradient(Colors.cyan_to_blue, "\nenter to exit"))

def about_page():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(gradient(Colors.cyan_to_blue, Center.XCenter(ascii_art)))
    log("pyhook ; simple webhook manager")
    log("features: rename, spam, delete")
    log("coded by aphid with pystyle and request modules")
    input(gradient(Colors.blue_to_green, "\npress enter to return"))

def menu(url):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(gradient(Colors.cyan_to_blue, Center.XCenter(ascii_art)))
        print(gradient(Colors.cyan_to_blue, """
    [1] change name
    [2] spam
    [3] delete
    [4] about
    [5] exit
"""))
        choice = get_input("choose an option")
        if choice == '1':
            change_webhook_name(url)
        elif choice == '2':
            spam_webhook(url)
        elif choice == '3':
            delete_webhook(url)
            break
        elif choice == '4':
            about_page()
        elif choice == '5':
            break
        else:
            log("invalid choice")
        input(gradient(Colors.cyan_to_blue, "\nenter to re-choose"))

def main():
    webhook = get_input("webhook url")
    if validate_webhook(webhook):
        log("valid webhook")
        menu(webhook)
    else:
        log("invalid webhook")

if __name__ == "__main__":
    main()
