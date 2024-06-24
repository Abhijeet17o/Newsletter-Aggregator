# Newsletter-Aggregator

This project is a Python application designed to scrape article data from multiple newsletter websites, organize it based on publication date, and display it on a local website using Flask and Jinja2 templates.

## Project Overview

The core functionality of this project involves:

- **Web Scraping:** Using Selenium to extract article titles, subtitles, links, and publication dates from specified newsletter websites.
- **Data Organization:** Sorting the scraped data based on the date articles were uploaded.
- **Web Application:** Using Flask to create a local web server and Jinja2 templates to display the sorted data in an organized manner.

## Files Included

### 1. `newsletter_scrapping.py`

This Python script performs the web scraping using Selenium. It visits each newsletter website in `nl_list`, extracts relevant article information, cleans and processes the data, and returns a dictionary containing article titles as keys and associated details as values.

### 2. `app.py`

This file utilizes Flask to create a web application. It includes routes and logic to render a web page (`index.html`) where the scraped and sorted data is displayed.

### 3. `templates/index.html`

A basic HTML template file using Jinja2 syntax. It defines the structure of the web page where the scraped article data will be displayed.

## Technologies Used

- **Python**: Programming language used for scripting and backend logic.
- **Selenium**: Web scraping library to automate browser interactions.
- **Flask**: Micro web framework for Python to create the local web server.
- **Jinja2**: Template engine for rendering HTML with Python data.
- **Pandas**: Library for data manipulation and analysis.

## Usage

1. **Clone the Repository:**


2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**

   ```bash
   python app.py
   ```

4. **Access the Local Website:**

   Open a web browser and navigate to `http://127.0.0.1:5000` to view the sorted newsletter articles.

## Notes

- Ensure you have Chrome WebDriver installed and compatible with your Chrome browser version for Selenium to work properly.
- Customize XPATH expressions in `newsletter_scrapping.py` based on the structure of the newsletter websites you are scraping.
- Feel free to expand and enhance the project by adding more newsletter sources or improving the web interface.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions, feedback, or collaboration opportunities, please feel free to contact me:

- **Email**: abhijeetsapar17@gmail.com
- **LinkedIn**: www.linkedin.com/in/abhijeet-sapar-08b8a3282
