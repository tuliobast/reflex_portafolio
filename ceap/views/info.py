import reflex as rx

from ceap.styles.styles import Size
from ceap.components.heading import heading
from ceap.components.info_detail import info_detail  

def info(title: str) -> rx.Component:
    return rx.vstack(
        heading(title),
        info_detail(),
        spacing=Size.DEFAULT.value,
        width="100%"    
    )