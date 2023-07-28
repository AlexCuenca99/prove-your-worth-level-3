import logging
import io
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont


def make_prove_your_worth_request(
    session: requests.Session,
    start_uri: str,
    uri: str,
) -> requests.Response:
    """Make sessions requests to Prove your Worth

    Args:
        start_uri (str): URI to make the start HTTP request (Could be None)
        uri (str): URI to make the HTTP request

    Raises:
        requests.ConnectionError: Any response different to 200 means connection error

    Returns:
        Response: Prove your worth server request response
    """

    if uri:
        session.get(start_uri)
        response = session.get(uri)
    else:
        response = session.get(start_uri)

    # If server throws 200
    if response.status_code == 200:
        return response
    else:
        print(f"Server throws {response.status_code} - {response.text}")
        raise requests.ConnectionError


def get_stateful_hash_from_response(response: requests.Response) -> str:
    """Get statefulhash from input tag of the response

    Args:
        response (requests.Response): Prove your worth server request response

    Returns:
        str: Hash value
    """

    soup = BeautifulSoup(response.text, "html.parser")
    input_element = soup.find("input", {"name": "statefulhash"})

    if input_element:
        statefulhash = input_element["value"]

        return statefulhash
    else:
        raise Exception("No hash was found")


def get_image_from_payload(session: requests.Session, uri: str) -> io.BytesIO:
    """Get image from Prove your worth request

    Args:
        session (requests.Session): Current session
        uri (str): Uri to request the image

    Raises:
        requests.ConnectionError: Any response different to 200 means connection error

    Returns:
        io.BytesIO: An instance of io.BytesIO that can be treated as an image
    """
    response = session.get(uri)

    # If server throws 200
    if response.status_code == 200:
        image = io.BytesIO(response.content)
        return image
    else:
        print(f"Server throws {response.status_code} - {response.text}")
        raise requests.ConnectionError


def write_over_image(
    image: io.BytesIO, full_name: str, role: str, hash_value: str
) -> Image:
    """Draw over the image

    Args:
        image (io.BytesIO): The image obtained from the request
        full_name (str): Name of the contestant
        role (str): Role you want to get
        hash_value (str): Hashvalue of the session

    Returns:
        Image: Drawed image
    """

    try:
        coordinates = (20, 20)
        text = f"Modified by {full_name}. \nI am using hash: {hash_value}. \nCurrently looking for {role} role."
        font_size = 30
        font = ImageFont.truetype("arial.ttf", font_size)
        font_color = (239, 126, 47)

        image_to_process = Image.open(image)
        content_to_draw = ImageDraw.Draw(image_to_process)
        content_to_draw.text(coordinates, text, fill=font_color, font=font)

        processed_image = "written_image.jpg"
        image_to_process.save(processed_image)
    except Exception as e:
        logging.exception(e)
        print("Image processing could not be completed:", e)


def send_information(
    session: requests.Session, uri: str, name: str, email: str, about_me: str
) -> None:
    """Send final result to the server

    Args:
        session (requests.Session): Current session
        uri (str): Payload URI where important data to send image is
        name (str): Name of the contestant
        email (str): Email of the contestant
        about_me (str): About of the contestant
    """

    payload = session.get(uri)
    uri_for_post = payload.headers["X-Post-Back-To"]

    data = {
        "name": name,
        "email": email,
        "about_me": about_me,
    }

    image_path = open("./written_images.jpg", "rb")
    resume_path = open("./Alex-C-Resume.pdf", "rb")
    code = open("./code.txt", "rb")

    files = {"image": image_path, "resume": resume_path, "code": code}

    response = session.post(uri_for_post, data=data, files=files)

    # If server throws 200
    if response.status_code == 200:
        print(response.status_code)
        print(response.text)
    else:
        print(f"Server throws {response.status_code} - {response.text}")
        raise requests.ConnectionError
