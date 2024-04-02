- following [this tutorial](https://youtu.be/6IxgsW5VoKg?si=btrsG0l0zuEk9Q9c)
- **2:05** note: had to run activate.bat file manually in command prompt terminal in order for terminal to use venv python version (without additional libraries or dependencies)
- **2:55** requirements.txt file should be common practice
- the "api endpoints" defined seem to be functions that return parsable text to the frontend
  - this can either be python strings or html (the former seems to convert to html)
- **8:56** note on SetInterval:
  - to pass a function as an argument, it must be invoked without parentheses, otherwise it will be called and its return value will be passed as the argument instead
    - 🐇 parameter vs argument: 
      - parameters are the variables that are declared to be required for a function when it's defined
      - arguments are the variables which are passed into a function when it's used
- **10:00** shorthand for writing elements and their id in vs code is "your_element#your_id_name" without either "<>"
  - 📚 *span* : a container for tagging html content, useful for css styling  
- **13:00** to get font and make it the default for a site: 
  1. go to google fonts
  2. select font
  3. select "get font"
  4. select "embed code"
  5. select fonts.googleapis.com link
  6. create "style" tag
  7. add "@import url("your fonts.googleapis.com link")
- 🐇 element1 (e.g. "\<p1>\</p1>") removes newline from end of element, whereas element (e.g. "\<p>\</p>") creates newline at end of element
