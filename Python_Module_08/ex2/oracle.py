import os
from dotenv import load_dotenv


def load_configuration() -> None:
    load_dotenv()

    mode = os.getenv("MATRIX_MODE")
    url = os.getenv("DATABASE_URL")
    key = os.getenv("API_KEY")
    level = os.getenv("LOG_LEVEL")
    endpoint = os.getenv("ZION_ENDPOINT")

    # print("MATRIX_MODE:", mode)
    # print("DATABASE_URL:", url)
    # print("API_KEY:", key)
    # print("LOG_LEVEL:", level)
    # print("ZION_ENDPOINT:", endpoint)

    missing = 0
    if mode:
        print(f"Mode: {mode}")
    else:
        missing = 1
        print("Mode: ", mode)

    if url:
        print("Database: Connected to local instance")
    else:
        missing = 1
        print("Database: ", url)

    if key:
        print("API Access: Authenticated")
    else:
        missing = 1
        print("API Access: ", key)

    if level:
        print(f"Log Level: {level}")
    else:
        missing = 1
        print("Log Level: ", level)

    if endpoint:
        print("Zion Network: Online")
    else:
        missing = 1
        print("Zion Network: ", endpoint)

    if missing:
        print("[ERROR] missing configuration")
    print("")


def hardcoded_check() -> bool:
    # hardcoded secrets check
    with open(__file__) as file:
        for line in file:
            line = line.strip()

            if line.startswith("API_KEY ="):
                print("[ERROR] Hardcoded secrets detected")
                return False

            if line.startswith("DATABASE_URL ="):
                print("[ERROR] Hardcoded secrets detected")
                return False

    print("[OK] No hardcoded secrets detected")
    return True


def env_check() -> bool:
    if os.path.exists(".env"):
        required = ["MATRIX_MODE",
                    "DATABASE_URL",
                    "API_KEY",
                    "LOG_LEVEL",
                    "ZION_ENDPOINT"]
        for name in required:
            if not os.getenv(name):
                print("[ERROR] .env file exist but not properly configured")
                return False
        print("[OK] .env file properly configured")
        return True
    else:
        print("[ERROR] .env file not found")
        return False


def override_check() -> bool:
    if "MATRIX_MODE" in os.environ:
        print("[OK] Production overrides available")
        return True

    print("[ERROR] Production overrides unavailable")
    return False


if __name__ == "__main__":
    # cp .env.example .env
    print("\nORACLE STATUS: Reading the Matrix...\n")

    load_configuration()

    print("Environment security check:")
    hardcoded_check()
    env_check()
    override_check()

    print("\nThe Oracle sees all configurations.")
