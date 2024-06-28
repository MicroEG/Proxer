# Proxer

Proxer is a Python tool designed to help you collect and filter proxies from various free proxy list websites. This tool has two main features: collecting proxies from specified sources and checking the validity of proxies from a given list.

## Features

1. **Collect Proxies**: Fetch proxies from multiple free proxy list websites.
2. **Check Proxies**: Validate proxies from a given list to filter out the working ones.

## Installation

### Prerequisites

- Python 3.6 or higher

### Install Required Libraries

You need to install the required libraries using pip:

```bash
pip install requests beautifulsoup4 colorama
```

## Usage

### Running the Script

To run the script, simply execute it using Python:

```bash
python proxerproxy.py
```

### Options

1. **Get Proxies**: Collect proxies from specified sources.

   - You will be prompted to select the source(s) for collecting proxies.
   - Options:
     - `sslproxies`
     - `freeproxylist`
     - `ALL`: Collect proxies from all available sources.

2. **Check Proxies**: Validate proxies from a given list.
   - You will be prompted to provide the path to the proxy file.

### Example Usage

#### Collecting Proxies

1. Run the script:

   ```bash
   python proxerproxy.py
   ```

2. Select the option to get proxies:

   ```
   Select What you need <3
   1- Get Proxies
   2- Check Proxies
   >> 1
   ```

3. Choose the proxy source:

   ```
   Select The Source
   1- sslproxies
   2- freeproxylist
   3- ALL
   >> 3
   ```

4. The collected proxies will be saved in a file named with the current timestamp in the `ProxerProxies` directory.

#### Checking Proxies

1. Run the script:

   ```bash
   python proxerproxy.py
   ```

2. Select the option to check proxies:

   ```
   Select What you need <3
   1- Get Proxies
   2- Check Proxies
   >> 2
   ```

3. Provide the path to the proxy file:

   ```
   Enter the path to the proxy file: ProxerProxies/2024-6-28-9-31-48PM.txt
   ```

4. The working proxies will be saved in a file named with the current timestamp in the `ProxerProxies` directory.

## Proxy Sources

The tool fetches proxies from the following sources:

1. [sslproxies](https://www.sslproxies.org/)
2. [freeproxylist](https://free-proxy-list.net/)
3. [usproxy](https://www.us-proxy.org/)
4. [socksproxy](https://www.socks-proxy.net/)
5. [spysme](https://spys.me/proxy.txt)
6. [proxydaily](https://proxy-daily.com/)



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue on GitHub.

## Acknowledgements

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for HTML parsing.
- [Requests](https://docs.python-requests.org/en/latest/) for making HTTP requests.
- [Colorama](https://pypi.org/project/colorama/) for colored terminal output.

---

_Note: This tool is for educational purposes only. Use it responsibly and ensure you comply with the terms of service of the websites you are accessing._
