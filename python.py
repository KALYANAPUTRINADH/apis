from appium import webdriver
import time

# Desired capabilities for Android
android_capabilities = {
    "platformName": "Android",
    "platformVersion": "11.0",  # Change as per your emulator/device
    "deviceName": "Android Emulator",
    "app": "/path/to/your/android/app.apk",  # Path to your APK file
    "automationName": "UiAutomator2"
}

# Desired capabilities for iOS
ios_capabilities = {
    "platformName": "iOS",
    "platformVersion": "14.0",  # Change as per your simulator/device
    "deviceName": "iPhone Simulator",
    "app": "/path/to/your/ios/app.app",  # Path to your .app file
    "automationName": "XCUITest"
}

def run_android_test():
    # Start Appium session for Android
    driver = webdriver.Remote("http://localhost:4723/wd/hub", android_capabilities)
    
    # Example test: Find an element and perform actions
    try:
        time.sleep(5)  # Wait for app to load
        element = driver.find_element_by_id("com.example:id/button")  # Replace with your element ID
        element.click()
        
        # Additional assertions can be added here
        print("Android Test Passed")
        
    except Exception as e:
        print(f"Android Test Failed: {e}")
    
    finally:
        driver.quit()

def run_ios_test():
    # Start Appium session for iOS
    driver = webdriver.Remote("http://localhost:4723/wd/hub", ios_capabilities)
    
    # Example test: Find an element and perform actions
    try:
        time.sleep(5)  # Wait for app to load
        element = driver.find_element_by_accessibility_id("Button")  # Replace with your element ID
        element.click()
        
        # Additional assertions can be added here
        print("iOS Test Passed")
        
    except Exception as e:
        print(f"iOS Test Failed: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    run_android_test()
    run_ios_test()