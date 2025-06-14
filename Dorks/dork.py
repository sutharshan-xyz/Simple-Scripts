import webbrowser
import time
import random
import re

# List of Google Dork queries
dorks = [
    "site:{url} ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv",
    "site:{url} intitle:index.of",
    "site:{url} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env",
    "site:{url} ext:sql | ext:dbf | ext:mdb",
    "site:{url} ext:log",
    "site:{url} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
    "site:{url} ext:pdf 'CONFIDENTIAL'",
    "site:{url} ext:pdf 'STRICTLY CONFIDENTIAL' ",
    "site:{url} ext:pdf 'HIGHLY CONFIDENTIAL' ",
    "site:{url} ext:pdf 'PRIVATE' ",
    "site:{url} ext:pdf 'PRIVATE AND CONFIDENTIAL' ",
    "site:{url} ext:pdf 'PRIVATE AND SENSITIVE'",
    "site:{url} ext:pdf 'TRADE SECRET' ",
    "site:{url} ext:pdf 'NOT FOR DISTRIBUTION' ",
    "site:{url} ext:pdf 'NOT FOR PUBLIC RELEASE' ",
    "site:{url} ext:pdf 'EMPLOYEE ONLY' ",
    "site:{url} ext:pdf 'INTERNAL USE ONLY' ",
    "site:{url} ext:pdf 'COMPANY SENSITIVE'",
    "site:{url} ext:pdf 'INTERNAL ONLY' ",
 #   "site:{url} 'join.slack' (ext:pdf OR ext:doc OR ext:docx OR ext:zip OR ext:bak OR ext:txt OR ext:ppt OR ext:pptx OR ext:xls OR ext:xlsx)",
    "site:{url} (ext:pdf OR ext:doc OR ext:docx OR ext:zip OR ext:bak OR ext:txt OR ext:ppt OR ext:pptx OR ext:xls OR ext:xlsx)",
 #   "site:{url} inurl:app_dev.php | inurl:app_dev |inurl:_profiler | inurl:profiler ",
 #   "site:{url} 'Uncaught Error: Call to undefined function' | 'error in your SQL' | 'WordPress database error:' | 'PHP Fatal' | 'not found in ' | 'Unclosed quotation mark' | 'Error Executing Database Query' | 'mysql_num_rows()' 'error' | 'mysql_fetch_array()' 'error' | 'mysql_query()' 'error' ",
 #   "site:{url} 'set up the administrator user' inurl:pivot ",
 #   "site:{url} inurl:wp-content/uploads/ (ext:xlsx | ext:xls '@gmail.com'| ext:xlsx '@gmail.com' | ext:xls 'date of birth' | ext:xlsx 'date of birth' | ext:xls 'INTERNAL USE ONLY' | ext:xlsx 'INTERNAL USE ONLY') ",
 #   "site:{url} inurl:wp-content/uploads/ ext:pdf ( '@gmail.com' | 'date of birth' | 'INTERNAL USE ONLY' )"
 #   "site:{url} intitle:'index of /' ",
 #   "site:{url} inurl:e1cib | inurl:oid2rp ",
 #   "site:{url} inurl:main ext:php 'Welcome to phpMyAdmin' 'running on' ",
 #   "site:{url}.s3.amazonaws.com ",
 #   "site:{url} inurl:dashboard "
]

def is_valid_url(url):
    # Simple regex to check if the URL is valid
    pattern = re.compile(r'^(https?://)?([a-z0-9.-]+)(:[0-9]{1,5})?(/.*)?$', re.IGNORECASE)
    return pattern.match(url)


def open_dork_tabs(url):
    for dork in dorks:
        # Format the dork with the provided URL
        query = dork.format(url=url)
        # Encode the query for a Google search URL
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

        # Open a new tab in the browser for each search URL
        webbrowser.open_new_tab(search_url)
        print(f"Opened tab for query: {query}")

        # Wait a random number of seconds between 2 and 5 before opening the next tab
        time.sleep(random.uniform(2, 5))


# Example usage
if __name__ == "__main__":
    while True:
        target_url = input("Enter the target URL (e.g., example.com) or type 'exit' to quit: ")
        if target_url.lower() == 'exit':
            print("Exiting the tool.")
            break
        if is_valid_url(target_url):
            open_dork_tabs(target_url)
        else:
            print("Invalid URL format. Please enter a valid URL.")
