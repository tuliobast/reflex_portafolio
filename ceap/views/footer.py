import reflex as rx

from ceap.components.media import media
from ceap.styles.styles import Size 

def footer() -> rx.Component:
    return rx.vstack(
        rx.text("Nombre"),
        media(),
        spacing=Size.SMALL.value
    )