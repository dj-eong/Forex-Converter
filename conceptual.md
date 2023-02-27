### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

    Generally speaking, JavaScript is the language for the web/browser

    In terms of specific differences between the two languages, 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

    dictionary = {"a": 1, "b": 2}
    dictionary.get('c', 0) # 0
    'c' in dictionary # False
    try:
        dictionary['c']
    except KeyError:
        print('key missing') # key missing

- What is a unit test?

- What is an integration test?

- What is the role of web application framework, like Flask?

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

- How do you collect data from a URL placeholder parameter using Flask?

- How do you collect data from the query string using Flask?

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?

- What is the session object in Flask?

- What does Flask's `jsonify()` do?
