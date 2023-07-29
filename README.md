<!-- ABOUT THE PROJECT -->
# Prove your worth Level 3 - Python Backend Developer

## About The Project

This Python script is to accomplish the Prove Your Worth Level 3 Tech Test. Basically, by using only code processes we have to make various requests to the server in order to get the final URI, through which we will be able to send our data.

## Built With

* ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/3)

<!-- GETTING STARTED -->
## Getting Started

The script was builded in Python 3+ environment. So in order to run it you want to have:

### Prerequisites

* python

  ```sh
  python --version
  ```

* pip

    ``` sh
    pip --version
    ```

* virtualenv

    ``` sh
    virtualenv --version
    ```

### Installation

_Below is an example of how you can run the script in your local machine._

1. Clone the repo

   ```sh
   git clone https://github.com/AlexCuenca99/prove-your-worth-level-3.git
   ```

2. Create a virtual environment. (It is highly recommended to use Python 3.9)

    ```sh
    virtualenv env/ini-dev --python=python3.9
    ```

    or just,

    ```sh
    virtualenv env/ini-dev
    ```

3. Activate environment

    ```sh
    env/ini-dev/Scripts/activate
    ```

4. Install packages

   ```sh
   (ini-dev) pip install -r requirements.txt
   ```

5. Create .env file

    Windows command:

   ```sh
   (ini-dev) touch .env 
   ```

   Inside it copy content from [.env.dist]() and add the correct URI's to the server.

<!-- USAGE EXAMPLES -->
## Usage

To achieve the goal you have to run main file [main.py](https://github.com/AlexCuenca99/prove-your-worth-level-3/blob/4cb3e2c9d3bca88a9d3de19dddda57b8472c9f81/main.py)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License.

<!-- CONTACT -->
## Contact

Alex Cuenca - [@alex_pcr99](https://twitter.com/alex_pcr99) - <alex-patricio1999@hotmail.com>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Helpful resources used on this project!

* [Requests](https://requests.readthedocs.io/en/latest/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [Python-dotenv](https://github.com/theskumar/python-dotenv)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
