# Django Newsletter Signup Box

A responsive newsletter subscription component built using Django 5, Python, HTML, and CSS.

## Features
- Newsletter email subscription form
- Email validation using Django Forms
- Duplicate subscription prevention
- Success and error messages
- Token-based unsubscribe functionality
- Django Admin integration
- Export subscriber records to CSV
- Responsive design for desktop, tablet, and mobile

## Technologies Used
- Python 3.12
- Django 5
- SQLite
- HTML5
- CSS3
- django-environ
- WhiteNoise

## Installation and Setup

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the required packages using `pip install -r requirements.txt`.
4. Configure the `.env` file with your own Django secret key, debug setting, and allowed hosts.
5. Run database migrations using `python manage.py migrate`.
6. Start the development server using `python manage.py runserver`.
7. Open `http://127.0.0.1:8000/subscribe/` in your browser.

## Admin Panel

Visit `/admin/` to manage subscribers and export selected subscriber records as a CSV file.

## Note
This project currently demonstrates subscription and unsubscribe functionality. It does not send newsletter emails.
