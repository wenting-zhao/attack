from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
    page = context.new_page()
    context.clear_cookies()

    page.goto("https://lmarena.ai/")
    page.screenshot(path="dialog1.png")
    time.sleep(5)
    page.screenshot(path="dialog2.png")
    time.sleep(5)
    page.screenshot(path="dialog3.png")

    html_content = page.content()
    open("output.html", 'w').write(html_content)

    # Wait for the page to fully load
    #page.wait_for_load_state('networkidle')  # Ensures the network is idle

    #try:
    #    # Type "Hello World" into the textarea
    #    page.fill('textarea[data-testid="textbox"]', 'Hello World')

    #    # Enable the button if necessary (as in the previous example)
    #    page.evaluate("document.getElementById('component-123').removeAttribute('disabled');")

    #    # Click the send button (replace '#component-123' with the actual ID or selector of the button)
    #    page.click('#component-123')

    #    # Wait for a response to be loaded; for example, wait for a specific element or network to idle
    #    page.wait_for_load_state('networkidle', timeout=300000)  # Wait until all network activity is done

    #    html_content = page.content()
    #    print(html_content)
    #except Exception as e:
    #    print(f"Error occurred: {e}")

    # Close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
