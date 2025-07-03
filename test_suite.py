from tests.test_login import test_valid_login
from tests.test_register import test_register_user

def run_suite():
    test_valid_login()
    test_register_user()
    print("Selected tests ran successfully.")

if __name__ == "__main__":
    run_suite()