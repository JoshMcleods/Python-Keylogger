This project is intended for educational purposes only, to improve not only my coding skills but also see how a common threat like keylogging operates. Unauthorized use of keyloggers is illegal and unethical. Always get explicit permission before running this software on any system.

This is a basic Python keylogger that captures keystrokes and logs them to a file. It uses the pynput library to monitor keyboard input in real-time. and then with open to append those keyboard inputs into a txt file.

Important:
By default, operating systems like Windows Defender and macOS Gatekeeper/Firewall are designed to block or alert you to programs that perform key capturing—as they should. For this script to function correctly during testing, you may need to manually allow the script through your system’s firewall or security prompts. 

Possible improvements for advanced version:
- Bypassing firewalls
- Sending keylog to remote server instead of local file
- Cryptography
- Sending Automatic Emails with phishing links to download file