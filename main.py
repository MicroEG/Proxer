#!/usr/bin/env python
# Wtih Love by : Michael Maher 
# Version : 1.0
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import re
from colorama import Fore, Style, init

init(autoreset=True)

def get_proxies(sources=None):
    if sources is None:
        sources = ['sslproxies', 'freeproxylist', 'usproxy', 'socksproxy', 'spysme', 'proxydaily']

    proxy_sites = {
        'sslproxies': 'https://www.sslproxies.org/',
        'freeproxylist': 'https://free-proxy-list.net/',
        'usproxy': 'https://www.us-proxy.org/',
        'socksproxy': 'https://www.socks-proxy.net/',
        'spysme': 'https://spys.me/proxy.txt',
        'proxydaily': 'https://proxy-daily.com/'
    }

    proxies = set()

    for source in sources:
        if source not in proxy_sites:
            raise ValueError(f"Invalid source specified: {source}")
        
        url = proxy_sites[source]
        response = requests.get(url)
        if source == 'spysme':
            proxy_list = response.text.splitlines()
            for proxy in proxy_list:
                if re.match(r'^\d+\.\d+\.\d+\.\d+:\d+$', proxy):
                    proxies.add(proxy)
        else:
            soup = BeautifulSoup(response.text, 'html.parser')
            for row in soup.find_all('tr'):
                columns = row.find_all('td')
                if columns and re.match(r'^\d+\.\d+\.\d+\.\d+$', columns[0].text) and columns[1].text.isdigit():
                    ip = columns[0].text
                    port = columns[1].text
                    proxy = f'{ip}:{port}'
                    proxies.add(proxy)

    timestamp = datetime.now().strftime('%Y-%m-%d-%I-%M-%S%p')
    if not os.path.exists('ProxerProxies'):
        os.makedirs('ProxerProxies')
    file_path = f'ProxerProxies/{timestamp}.txt'
    with open(file_path, 'w') as f:
        for proxy in proxies:
            f.write(proxy + '\n')
    
    return proxies

def is_proxy_working(proxy):
    test_url = 'http://www.example.com'
    try:
        response = requests.get(test_url, proxies={'http': proxy, 'https': proxy}, timeout=5)
        return response.status_code == 200
    except:
        return False

def filter_proxies(proxies):
    working_proxies = set()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(is_proxy_working, proxies)
        for proxy, is_working in zip(proxies, results):
            if is_working:
                working_proxies.add(proxy)
    return working_proxies
def clear():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

if __name__ == "__main__":
    clear()
    screen = """


██████╗ ██████╗  ██████╗ ██╗  ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝██╔════╝██╔══██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝ █████╗  ██████╔╝ 
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗ ██╔══╝  ██╔══██╗
██║     ██║  ██║╚██████╔╝██╔╝ ██╗███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                  V 1.0           
    """
    print(screen)
    print(f"{Fore.CYAN}Select What you need <3{Style.RESET_ALL}")
    choice = input(f"{Fore.CYAN}1- Get Proxies\n2- Check Proxies\n>> {Style.RESET_ALL}")
    
    if choice == "1":
        print(f"{Fore.CYAN}Select The Source{Style.RESET_ALL}")
        choice2 = input(f"{Fore.CYAN}1- sslproxies\n2- freeproxylist\n3- ALL\n>> {Style.RESET_ALL}")
        
        if choice2 == "1":
            proxies = get_proxies(['sslproxies'])
        elif choice2 == "2":
            proxies = get_proxies(['freeproxylist'])
        elif choice2 == "3":
            proxies = get_proxies(['sslproxies', 'freeproxylist', 'usproxy', 'socksproxy', 'spysme', 'proxydaily'])
        else:
            print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")
            exit()

        print(f"{Fore.GREEN}Collected {len(proxies)} proxies from selected sources.{Style.RESET_ALL}")
    
    elif choice == "2":
        file_path = input(f"{Fore.CYAN}Enter the path to the proxy file: {Style.RESET_ALL}")
        
        if not os.path.exists(file_path):
            print(f"{Fore.RED}File not found.{Style.RESET_ALL}")
            exit()

        with open(file_path, 'r') as f:
            proxies = f.read().splitlines()

        working_proxies = filter_proxies(proxies)
        print(f"{Fore.GREEN}Found {len(working_proxies)} working proxies.{Style.RESET_ALL}")
        
        # Save working proxies to a file with the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d-%I-%M-%S%p')
        file_path = f'ProxerProxies/working_proxies_{timestamp}.txt'
        with open(file_path, 'w') as f:
            for proxy in working_proxies:
                f.write(proxy + '\n')
    else:
        print(f"{Fore.RED}Invalid choice{Style.RESET_ALL}")
