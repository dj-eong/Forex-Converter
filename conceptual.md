### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

    JavaScript is _the_ programming language for the world wide web - browsers use JS, along with HTML/CSS, to display webpages. JS is generally used client-side for the front-end (although can be used for back-end) whereas Python is a more general programming language that can be used for a variety of tasks, including back-end web dev, data analysis, etc.

    In terms of specific differences between the two languages, there are several. Some differences include Python being a more explicit language than JavaScript, where Python raises errors in places JS returns undefined, as well as syntactical differences like Python not requiring brackets but instead indentations, variable naming conventions (camelCasing vs. lower_snake_casing), etc.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your program
  crashing.

    ```
    dictionary = {"a": 1, "b": 2}

    dictionary.get('c', 0)      # 0

    'c' in dictionary           # False

    try:  
        dictionary['c']
    except KeyError:
        return 'key missing'    # 'key missing'
    ```

- What is a unit test?

    A unit test tests one "unit" of functionality. In other words, it tests a single function by itself without taking into consideration anything outside the function.

- What is an integration test?

    An integration test tests how multiple components/units integrate to work with each other.

- What is the role of web application framework, like Flask?

    A web application framework consists of a set of functions, classes, etc. that a coder can import that helps to streamline certain functionalities. For instance, with Flask, it becomes easier to set up URL routes and process & respond to HTTP requests with fewer lines of code; it provides structure for the coder to follow.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

    A query parameter would generally be used when it feels more like the parameter is providing extra/supplemental info about the page (e.g. `/search?query=doughnuts` or `/images?sort=new`). A URL parameter is used when the parameter feels more like the topic/subject of the page (e.g. `/products/keyboard`) .

- How do you collect data from a URL placeholder parameter using Flask?

    ```
    @app.route('/products/<product>')
    def show_product_page(product):
        product...
    ```

- How do you collect data from the query string using Flask?

    ```
    @app.route('/search')
    def search():
        search_term = request.args['query']
        ...
    ```

- How do you collect data from the body of the request using Flask?

    ```
    @app.route('/something', methods=['POST'])
    def do_something():
        value = request.json['some_key']
        ...
    ```

- What is a cookie and what kinds of things are they commonly used for?

    Cookies are a way to save small bits of information on the client. They can be used for storing info like log-in status, username/user ID, etc. When a server responds to a request to a browser, it may send along some cookies; the browser then keeps those cookies, and whenever it makes another request to the server, reminds the server of the cookies.

- What is the session object in Flask?

    The session object is essentially a 'magic dictionary' that stores cookies. It makes the coder's job easier as one can pass in different data types and structures without having to convert it; the session object takes care of formatting the data correctly as well as encrypting its cookies.

- What does Flask's `jsonify()` do?

    `jsonify()` takes an input and turns it into properly formatted JSON.