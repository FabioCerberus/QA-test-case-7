import time
from playwright.sync_api import sync_playwright, expect


def create_account(page, username, email, password):
    # Navigate to Automation Exercise
    page.goto("https://automationexercise.com/")

    # Verify home page loaded
    expect(page).to_have_title("Automation Exercise")

    # Click Signup / Login
    page.get_by_role("link", name="Signup / Login").click()

    # Verify New User Signup is visible
    expect(page.get_by_text("New User Signup!")).to_be_visible()

    # Enter name and email
    page.locator('[data-qa="signup-name"]').fill(username)
    page.locator('[data-qa="signup-email"]').fill(email)

    # Click Signup button
    page.locator('[data-qa="signup-button"]').click()

    # Verify account information page
    expect(page.get_by_text("Enter Account Information")).to_be_visible()

    # Fill account details
    page.locator("#id_gender1").check()
    page.locator('[data-qa="password"]').fill(password)

    page.locator('[data-qa="days"]').select_option("10")
    page.locator('[data-qa="months"]').select_option("5")
    page.locator('[data-qa="years"]').select_option("1995")

    page.locator("#newsletter").check()
    page.locator("#optin").check()

    # Fill address information
    page.locator('[data-qa="first_name"]').fill("Fabio")
    page.locator('[data-qa="last_name"]').fill("Lacerda")
    page.locator('[data-qa="company"]').fill("QA Study")
    page.locator('[data-qa="address"]').fill("123 Test Street")
    page.locator('[data-qa="address2"]').fill("Apartment 45")

    page.locator('[data-qa="country"]').select_option("United States")
    page.locator('[data-qa="state"]').fill("California")
    page.locator('[data-qa="city"]').fill("Los Angeles")
    page.locator('[data-qa="zipcode"]').fill("90001")
    page.locator('[data-qa="mobile_number"]').fill("1234567890")

    # Create account
    page.locator('[data-qa="create-account"]').click()

    # Verify account was created
    expect(page.get_by_text("Account Created!")).to_be_visible()

    # Continue to logged-in area
    page.locator('[data-qa="continue-button"]').click()

    # Verify user is logged in
    expect(page.get_by_text(f"Logged in as {username}")).to_be_visible()

    # Logout so Test Case 2 can test login
    page.get_by_role("link", name="Logout").click()

    # Verify login page is visible after logout
    expect(page.get_by_text("Login to your account")).to_be_visible()


def test_login_user_with_correct_email_and_password():
    username = "Fabio Test"
    password = "Password123!"
    email = f"fabio_login_test_{int(time.time())}@example.com"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Create account first
        create_account(page, username, email, password)

        page.goto("https://automationexercise.com/")
        expect(page).to_have_title("Automation Exercise")
        page.get_by_role("link", name="Signup / Login").click()
        expect(page.get_by_text("Login to your account")).to_be_visible()
        page.locator('[data-qa="login-email"]').fill(email)
        page.locator('[data-qa="login-password"]').fill(password)
        page.locator('[data-qa="login-button"]').click()
        expect(page.get_by_text(f"Logged in as {username}")).to_be_visible()
        page.get_by_role("link", name="Logout").click()
        expect(page).to_have_title("Automation Exercise - Signup / Login")

def test_register_user_with_existing_email():
    username = "Fabio Test"
    password = "Password123!"
    email = f"fabio_login_test_{int(time.time())}@example.com"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        create_account(page, username, email, password)

        page.goto("https://automationexercise.com/")
        expect(page).to_have_title("Automation Exercise")
        page.get_by_role("link", name="Signup / Login").click()
        expect(page.get_by_text("New User Signup!")).to_be_visible()
        page.locator('[data-qa="signup-name"]').fill(username)
        page.locator('[data-qa="signup-email"]').fill(email)
        page.locator('[data-qa="signup-button"]').click()
        expect(page.get_by_text("Email Address already exist!")).to_be_visible()



        browser.close()