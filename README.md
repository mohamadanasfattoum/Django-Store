# Django-Store

Django-Store is an Amazon clone built using Django, Django Rest Framework, and JavaScript. It aims to replicate the core functionalities of the popular e-commerce platform, providing users with a familiar and intuitive shopping experience.

## Tech Stack

The tech stack used in Django-Store includes:

- **Django**: A high-level Python web framework that provides a robust toolkit for building web applications.
- **Django Rest Framework**: A powerful and flexible toolkit for building Web APIs.
- **JavaScript**: A popular programming language used for enhancing the interactivity and functionality of web pages.
- **HTML**: The standard markup language for creating web pages and applications. It structures the content of the web pages and provides the foundation for rendering the user interface.
 - **CSS**: A stylesheet language used for describing the presentation and styling of a document written in HTML. CSS is utilized to customize the appearance and layout of the Django-Store application.
- **SCSS**: A CSS preprocessor that simplifies the process of writing CSS by introducing features like variables, mixins, and nesting. SCSS enhances the maintainability and reusability of the project's stylesheets.
- **Redis**: An open-source in-memory data structure store that is used as a cache to improve the performance of the application.
- **Celery**: A distributed task queue system used for handling asynchronous tasks.
- **Chart.js**: A JavaScript library for creating interactive charts and graphs.
- **Ajax**: A technique for creating asynchronous web applications by sending and receiving data from the server without interfering with the display and behavior of the existing page.




### How to Run

To run the Django-Store project locally, follow these steps:

1. Clone the repository using the following command:

   ````
   git clone https://github.com/mohamadanasfattoum/Django-Store.git
2. Navigate to the project directory:

   ````
   cd Django-Store
3. Set up a virtual environment (optional but recommended) and activate it.

4. Install the required dependencies. It is recommended to use a package manager like pipenv or virtualenv. Run the following command:

   ````
   pip install -r requirements.txt
5. Perform the initial database migration:

   ````
   python manage.py migrate
6. Create a superuser account:

   ````
   python manage.py createsuperuser
7. Start the development server:

   ````
   python manage.py runserver
8. Open your web browser and access the application at `http://localhost:8000`.

9. To access the Django admin panel, go to `http://localhost:8000/admin` and log in using the superuser account created in step 6.

You are now ready to explore and interact with the Django-Store application locally.

Please note that this is a basic setup guide, and additional configurations or steps may be required depending on your specific environment.

## Conclusion

Django-Store is a powerful e-commerce platform built using Django and Django Rest Framework. It provides a solid foundation for creating your own online marketplace and includes features such as product browsing, shopping cart management, and more. By following the instructions provided, you can easily set up and run the Django-Store project on your local machine. Feel free to explore the code and customize the application to suit your specific requirements.
