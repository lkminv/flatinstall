import requests
import os

try:
    query = input("Search for: ")
    url = f"https://flathub.org/api/v1/apps/search/{query}"
    
    response = requests.get(url)
    all_apps = response.json()
    
    shown = 0
    per_page = 20
    
    while shown < len(all_apps):
        #show 20 apps
        for i in range(shown, min(shown + per_page, len(all_apps))):
            print(f"{i + 1}. {all_apps[i]['name']}")
        
        shown += per_page
        
        if shown < len(all_apps):
            choice = input(f"\nChoose number or press Enter to load more ({len(all_apps) - shown} apps left): ")
        else:
            choice = input("\nChoose number (no more apps): ")
        
        #enter to show more
        if choice == "":
            continue
        else:
            selected = all_apps[int(choice) - 1]
            print(f"\nYou chose: {selected['name']}")
            #install app
            os.system(f"flatpak install {selected['flatpakAppId']}")
            break

except KeyboardInterrupt:
    print("\n\nexit")
    exit(0)