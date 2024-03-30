from selenium import webdriver
from selenium.webdriver.common.by import By
import matplotlib.pyplot as plt
import time

def get_submission_counts(username):
    try:
        # Initialize the Selenium webdriver (make sure to have chromedriver or geckodriver installed)
        driver = webdriver.Chrome()  # You can use other web drivers like Firefox by changing this line

        # Open Codeforces website
        driver.get(f"https://codeforces.com/submissions/{username}")

        # Wait for the page to load
        time.sleep(5)

        # Find all the rows in the submissions table
        submission_rows = driver.find_elements(By.CSS_SELECTOR, ".status-frame-datatable tr")

        # Initialize counters
        accepted_count = 0
        not_accepted_count = 0

        # Loop through the rows to count submissions
        for row in submission_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 6:  # Ensure that the row contains the necessary information
                verdict = cells[5].text
                if verdict == "Accepted":
                    accepted_count += 1
                else:
                    not_accepted_count += 1

        # Close the webdriver
        driver.quit()

        return accepted_count, not_accepted_count

    except Exception as e:
        print("An error occurred:", e)
        return 0, 0

# mExample usage:
def plot_submission_counts(username):
    accepted_count, not_accepted_count = get_submission_counts(username)

    # Plot the results
    plt.figure(figsize=(6, 4))
    plt.bar(["Accepted", "Not Accepted"], [accepted_count, not_accepted_count])
    plt.xlabel('Verdict')
    plt.ylabel('Submission Count')
    plt.title('Submission Counts by Verdict')
    plt.show()

username = input("Enter your Codeforces username: ")
plot_submission_counts(username)
