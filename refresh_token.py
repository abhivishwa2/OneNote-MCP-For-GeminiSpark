import requests
import time

# 1. Insert your Azure Client ID here
CLIENT_ID = "Azure Client ID"
TENANT_ID = "common"

# Endpoints
DEVICE_CODE_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/devicecode"
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

SCOPES = "https://graph.microsoft.com/Notes.Read https://graph.microsoft.com/Notes.ReadWrite https://graph.microsoft.com/User.Read offline_access"

def get_token_via_rest():
    # Step 1: Request Device Code
    response = requests.post(DEVICE_CODE_URL, data={
        "client_id": CLIENT_ID,
        "scope": SCOPES
    })
    
    if response.status_code != 200:
        print("❌ Failed to initiate device code flow:", response.text)
        return

    data = response.json()
    device_code = data.get("device_code")
    user_code = data.get("user_code")
    verification_uri = data.get("verification_uri")
    interval = data.get("interval", 5)
    expires_in = data.get("expires_in", 900)

    print("\n" + "="*50)
    print(f"1. Open this link in your browser: {verification_uri}")
    print(f"2. Enter this exact code: {user_code}")
    print("="*50 + "\n")
    print("Waiting for you to log in (polling Microsoft servers)...")

    # Step 2: Poll for the token
    start_time = time.time()
    while time.time() - start_time < expires_in:
        time.sleep(interval)
        
        token_response = requests.post(TOKEN_URL, data={
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "client_id": CLIENT_ID,
            "device_code": device_code
        })
        
        token_data = token_response.json()
        
        if "refresh_token" in token_data:
            print("\n✅ SUCCESS! Here is your Refresh Token for Google Cloud Run:\n")
            print(token_data["refresh_token"])
            print("\n" + "="*50)
            return
        elif token_data.get("error") == "authorization_pending":
            continue
        elif token_data.get("error") == "slow_down":
            interval += 2
            continue
        else:
            print("\n❌ Error during token poll:", token_data.get("error_description", token_data))
            return

    print("\n❌ Timed out waiting for login.")

if __name__ == "__main__":
    get_token_via_rest()
