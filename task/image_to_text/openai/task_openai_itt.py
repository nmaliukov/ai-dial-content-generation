import base64
from pathlib import Path

from task._utils.constants import API_KEY, DIAL_CHAT_COMPLETIONS_ENDPOINT
from task._utils.model_client import DialModelClient
from task._models.role import Role
from task.image_to_text.openai.message import (
    ContentedMessage,
    TxtContent,
    ImgContent,
    ImgUrl,
)


def start() -> None:
    project_root = Path(__file__).parent.parent.parent.parent
    image_path = project_root / "dialx-banner.png"

    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    base64_image = base64.b64encode(image_bytes).decode("utf-8")
    client = DialModelClient(
        endpoint=DIAL_CHAT_COMPLETIONS_ENDPOINT,
        deployment_name="gpt-4o",
        api_key=API_KEY,
    )
    #
    text_content = TxtContent(text="Describe the image")
    img_content = ImgContent(
        image_url=ImgUrl(url=f"data:image/png;base64,{base64_image}")
    )
    message = ContentedMessage(content=[text_content, img_content], role=Role.USER)
    client.get_completion(messages=[message])


start()
