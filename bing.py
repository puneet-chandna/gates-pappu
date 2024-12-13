import os
import random
import subprocess
import signal
import sys
from time import sleep

def get_random_search_term(used_terms):
    """Generates a random search term that hasn't been used yet."""
    search_terms = [
        "latest AI research",
        "space exploration news",
        "top programming languages",
        "current weather",
        "quantum mechanics basics",
        "blockchain use cases",
        "emerging tech startups",
        "coding bootcamps",
        "web3 trends",
        "cosmic microwave background",
        "DIY projects for engineers",
        "Ubuntu tips and tricks",
        "best sci-fi movies",
        "machine learning projects",
        "future of electric vehicles"
    ]
    unused_terms = [term for term in search_terms if term not in used_terms]
    if not unused_terms:
        used_terms.clear()  
        unused_terms = search_terms
    return random.choice(unused_terms)

def open_edge_with_bing(search_query):
    """Opens Microsoft Edge and searches for the given query using the search bar."""
    edge_command = "microsoft-edge --new-window https://www.bing.com"
    subprocess.run(edge_command, shell=True)

   
    sleep(7)

 
    subprocess.run("xdotool search --sync --onlyvisible --class microsoft-edge windowactivate --sync", shell=True)
    subprocess.run(f"xdotool type '{search_query}'", shell=True)
    subprocess.run("xdotool key Return", shell=True)

def signal_handler(sig, frame):
    """Handles graceful exit on receiving a termination signal."""
    print("\nExiting the random Bing search bot...")
    sys.exit(0)

def main():
    """Main function to initiate random Bing searches."""
    print("Starting random Bing search bot...")
    used_terms = set()
    log_file = "search_log.txt"

    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while True:
        search_term = get_random_search_term(used_terms)
        used_terms.add(search_term)

        with open(log_file, "a") as log:
            log.write(f"Searching for: {search_term}\n")
        print(f"Searching for: {search_term}")

        open_edge_with_bing(search_term)
        sleep_time = random.randint(30, 120)  

        with open(log_file, "a") as log:
            log.write(f"Waiting for {sleep_time} seconds before the next search...\n")
        print(f"Waiting for {sleep_time} seconds before the next search...")

        sleep(sleep_time)

if __name__ == "__main__":
    main()
