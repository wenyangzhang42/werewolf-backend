class Player:
    name: str
    seat: int
    role: str
    alignment: str
    status: str

    def __init__(self, name: str, seat: int, role: str, alignment: str):
        self.name = name
        self.seat = seat
        self.role = role
        self.alignment = alignment
        self.status = "alive"

    def __str__(self):
        return self.name + ", seat: " + self.seat + ", role: " + \
               self.role + ", alignment: " + self.alignment + ", status: " + self.status

    def set_role(self, role: str):
        self.role = role

    def set_status(self, status: str):
        self.status = status


