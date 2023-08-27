from webdriver_manager.chrome import ChromeDriverManager
from utils.threading_controller import FastSearchAlgo
from argparse import ArgumentParser
from os.path import isfile
import sys
print("---------------------------Hi-----------------------------")
x = input("[-] Number of results to scrape. Use -1 for all results: ")

def read_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, "r", encoding=encoding) as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def write_file(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
        print("[+] Keyword added!")

def edit_queries_file():
    file_path = "queries.txt"  # Specify the file name directly

    # Read the existing content of the file
    current_content = read_file(file_path, encoding='iso-8859-1')  # Replace 'iso-8859-1' with the correct encoding

    new_content = input("[-] Enter the keyword: ")

    # Clear the file and write the updated content
    write_file(file_path, new_content)

# Call the function to edit the "queries.txt" file
edit_queries_file()

class GMapsScraper:
    def __init__(self):
        self._args = None

    def arg_parser(self):
        parser = ArgumentParser(description='Command Line Google Map Scraper')

        # Input options
        parser.add_argument('-q', '--query-file', help='Path to query file (default: ./queries.txt)', type=str,
                            default="./queries.txt")
        parser.add_argument('-w', '--threads', help='Number of threads to use (default: 1)', type=int, default=1)
        parser.add_argument('-l', '--limit', help='Number of results to scrape (-1 for all results, default: -1)',
                            type=int, default=x)
        parser.add_argument('-u', '--unavailable-text',
                            help='Replacement text for unavailable information (default: "Not Available")', type=str,
                            default="Not Available")
        parser.add_argument('-bw', '--browser-wait', help='Browser waiting time in seconds (default: 15)', type=int,
                            default=10)
        parser.add_argument('-se', '--suggested-ext',
                            help='Suggested URL extensions to try (can be specified multiple times)', action='append',
                            default=[])
        parser.add_argument('-wb', '--windowed-browser', help='Disable headless mode', action='store_false',
                            default=True)
        parser.add_argument('-v', '--verbose', help='Enable verbose mode', action='store_true')
        parser.add_argument('-o', '--output-folder', help='Output folder to store CSV details (default: ./CSV_FILES)',
                            type=str, default='./data')
        parser.add_argument('-d', '--driver-path',
                            help='Path to Chrome driver (if not provided, it will be downloaded)', type=str,
                            default='./chrome_driver/chromedriver.exe')

        # Custom commands for additional help
        parser.add_argument('--help-query-file', action='store_true', help='Get help for specifying the query file')
        parser.add_argument('--help-limit', action='store_true', help='Get help for specifying the result limit')
        parser.add_argument('--help-driver-path', action='store_true', help='Get help for specifying the driver path')

        self._args = parser.parse_args()

    def check_args(self):
        q = self._args.query_file
        if not isfile(q):
            print(f"[-] File not found at path: {q}")
            sys.exit(1)

    def scrape_maps_data(self):
        self.check_args()

        if self._args.help_query_file:
            self.print_query_file_help()

        if self._args.help_limit:
            self.print_limit_help()

        if self._args.help_driver_path:
            self.print_driver_path_help()

        queries_list = FastSearchAlgo.load_query_file(file_name=self._args.query_file)
        threads_limit = min(self._args.threads, len(queries_list))
        limit_results = None if self._args.limit == -1 else self._args.limit

        driver_path = self._args.driver_path
        if not self._args.driver_path:
            try:
                driver_path = ChromeDriverManager().install()
            except ValueError:
                print("[-] Not able to download the driver which is capable with your browser.")
                print("[INFO] Head to this site (https://chromedriver.chromium.org/downloads)"
                      " and find your version driver and pass it with argument -d.")
                exit()

        algo_obj = FastSearchAlgo(
            unavailable_text=self._args.unavailable_text,
            headless=self._args.windowed_browser,
            wait_time=self._args.browser_wait,
            suggested_ext=self._args.suggested_ext,
            output_path=self._args.output_folder,
            workers=threads_limit,
            result_range=limit_results,
            verbose=self._args.verbose,
            driver_path=driver_path
        )

        algo_obj.fast_search_algorithm(queries_list)


if __name__ == '__main__':
    App = GMapsScraper()
    App.arg_parser()
    App.scrape_maps_data()
