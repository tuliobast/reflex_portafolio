import reflex as rx

from ceap.components.media import media
from ceap.components.heading import heading
from ceap.styles.styles import Size


def header() -> rx.Component:
    return rx.hstack(
        rx.avatar(size=Size.BIG.value),
        rx.vstack(
            heading("Nombre", True),
            heading("Habilidad principal"),
            rx.text(
                rx.icon("map-pin"),
                "Localizacion",
                display= "inherit"
            ),
            media(),
            spacing=Size.SMALL.value,
        ),
        spacing=Size.DEFAULT.value,
    
    )
    
    