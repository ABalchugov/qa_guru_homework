from dataclasses import dataclass, field


@dataclass
class UserData:
    name: str = "Александр Александров"
    email: str = field(default="alexandr@example.com", repr=False)
    current_address: str = field(default="", repr=False)
    permanent_address: str = field(default="", repr=False)
