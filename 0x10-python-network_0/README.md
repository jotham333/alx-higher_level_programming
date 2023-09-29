## Script 1: Get Body Size of HTTP Response
Description: This Bash script takes a URL as input, sends a request to that URL using curl, and displays the size of the body of the response in bytes.
Usage: Ensure you have curl installed and use the script as follows:
./get_body_size.sh [URL]

## Script 2: Display Body of 200 Response
Description: This Bash script takes a URL as input, sends a GET request using curl, and displays the body of the response if the HTTP status code is 200 (OK).
Usage: Make sure you have curl installed and run the script as follows:
./get_200_response_body.sh [URL]

## Script 3: Send DELETE Request and Display Response
Description: This Bash script sends a DELETE request to a specified URL using curl and displays the body of the response.
Usage: Ensure you have curl installed and use the script as follows:
./send_delete_request.sh [URL]

## Script 4: Display Accepted HTTP Methods
Description: This Bash script takes a URL as input and uses curl to display all HTTP methods accepted by the server.
Usage: Make sure you have curl installed and run the script as follows:
./display_accepted_methods.sh [URL]

## Script 5: Send GET Request with Custom Header
Description: This Bash script sends a GET request to a specified URL using curl and includes a custom header variable X-School-User-Id with the value 98.
Usage: Ensure you have curl installed and use the script as follows:
./send_get_request_with_header.sh [URL]

## Script 6: Send POST Request with Data
Description: This Bash script sends a POST request to a specified URL using curl and includes variables email and subject with specific values in the request body.
Usage: Make sure you have curl installed and run the script as follows:
./send_post_request_with_data.sh [URL]

## Function 7: Find a Peak in a List
Description: This Python function, implemented in 6-peak.py, finds a peak in a list of unsorted integers. It has a low time complexity, and there may be more than one peak in the list.
Usage: You can use the find_peak function by importing it into your Python script and passing a list of integers as an argument

## Script 8: Display Response Status Code
Description: This Bash script sends a request to a specified URL using curl and displays only the status code of the response, without using pipes or redirection.
Usage: Ensure you have curl installed and use the script as follows:
./display_response_status_code.sh [URL]

## Script 9: Send JSON POST Request
Description: This Bash script sends a JSON POST request to a specified URL and displays the body of the response. It sends the contents of a file as the request body.
Usage: Make sure you have curl installed and run the script as follows:
./send_json_post_request.sh [URL] [file.json]

## Script 10: Catch Me If You Can
Description: This Bash script makes a request to 0.0.0.0:5000/catch_me using curl, causing the server to respond with the message "You got me!" in the body of the response.
Usage: Ensure you have curl installed and use the script as follows:
./catch_me_if_you_can.sh
