import os

from dotenv import load_dotenv

from utils import (
    make_prove_your_worth_request,
    get_stateful_hash_from_response,
    get_image_from_payload,
    write_over_image,
    send_information,
)

from sessions import ProveYourWorthSession

from constants import USERNAME, NAME, ROLE, ABOUT_ME, EMAIL


load_dotenv()

start_session_uri = str(os.getenv("START_SESSION_URI"))
start_active_session_uri = str(os.getenv("ACTIVATE_SESSION_URI"))
payload_uri = str(os.getenv("PAYLOAD_URI"))


if __name__ == "__main__":
    with ProveYourWorthSession() as session:
        session = session.__enter__()

        start_response = make_prove_your_worth_request(
            session, start_uri=start_session_uri, uri=None
        )
        hashvalue = get_stateful_hash_from_response(start_response)

        # Build Activation URI
        activation_uri = start_active_session_uri + f"={hashvalue}&username={USERNAME}"

        # Activate session
        activated_response = make_prove_your_worth_request(
            session, start_session_uri, activation_uri
        )

        image = get_image_from_payload(session, payload_uri)

        write_over_image(image, NAME, ROLE, hashvalue)

        send_information(session, payload_uri, NAME, EMAIL, ABOUT_ME)
