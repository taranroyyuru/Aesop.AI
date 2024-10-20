"""Talk page."""

import reflex as rx
from reflex_audio_capture import AudioRecorderPolyfill, get_codec, strip_codec_part

from aesop.frontend.components.footer import index as footer
from aesop.frontend.components.header import index as header
from aesop.frontend.utils import BaseState

from cartesia import Cartesia
import base64
from pathlib import Path

cartesia_key = '581b6842-6aac-4de8-ab77-f40fae74e18f'

client = Cartesia(api_key=cartesia_key)

REF = "recorded_audio"


class State(rx.State):
    """The app state."""

    has_error: bool = False
    processing: bool = False
    device_id: str = ""
    use_mp3: bool = True

    async def on_data_available(self, chunk: str):
        mime_type, _, codec = get_codec(chunk).partition(";")
        audio_type = mime_type.partition("/")[2]
        if audio_type == "mpeg":
            audio_type = "mp3"

        base64_audio = chunk
        
        audio_data = base64.b64decode(base64_audio.split(',')[1])

        temp_audio_name = 'audio.mp3'

        with open(f'assets/{temp_audio_name}', 'wb') as audio_file:
            audio_file.write(audio_data)

        # print(len(chunk), mime_type, codec, audio_type)

    def clone_save_audio(self):
        # # play the voice and ask them to re record if they are not satisfied
        cloned_voice_embedding = client.voices.clone('assets/audio.mp3')

        # # Create a new voice # it also saves the voice on the cloud
        new_voice = client.voices.create(
            name="New Voice1",
            description="A clone of my own voice",
            embedding=cloned_voice_embedding,
        )

        voices = client.voices.list()
        print(voices)

    def set_device_id(self, value):
        self.device_id = value
        yield capture.stop()

    def on_error(self, err):
        print(err)

    def on_load(self):
        # We can start the recording immediately when the page loads
        return capture.start()

    def play_audio(self):
        return ''
    
    def reload_page(self):
        print('i am here')
        return rx.redirect("/talk")





capture = AudioRecorderPolyfill.create(
    id=REF,
    on_data_available=State.on_data_available,
    on_error=State.on_error,
    device_id=State.device_id,
    use_mp3=State.use_mp3,
)

def input_device_select():
    return rx.select.root(
        rx.select.trigger(placeholder="Select Input Device"),
        rx.select.content(
            rx.foreach(
                capture.media_devices,
                lambda device: rx.cond(
                    device.deviceId & device.kind == "audioinput",
                    rx.select.item(device.label, value=device.deviceId),
                ),
            ),
        ),
        on_change=State.set_device_id,
    )

def record() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Recorder Your Custom Voice"),
            capture,
            rx.text(f"Recorder Status: {capture.recorder_state}"),
            rx.cond(
                capture.is_recording,
                rx.button(
                    "Stop Recording", 
                    on_click=capture.stop()
                ),
                rx.button(
                    "Start Recording",
                    on_click=capture.start(),
                ),
            ),
            
            rx.button(
                    "Reload After Recording", 
                    on_click=rx.call_script("window.location.reload()"),
            ),
            rx.button(
                    "Satisfied? Clone it.", 
                    on_click=State.clone_save_audio
            ),
            style={"width": "100%", "> *": {"width": "100%"}},
        ),
        size="1",
        margin_y="2em",
    )

def play() -> rx.Component:
    # if Path('audio.mp3').exists():
            return rx.audio(
                url="/audio.mp3",
                controls=True,
                width="400px",
                height="32px",
            )
    # return False
@rx.page(on_load=BaseState.get_configs)
def talk_page() -> rx.Component:
    return rx.container(
        header(redirect_to_signin=True),
        play(),
        record(),

        footer(),
        padding="0",
        
    )
