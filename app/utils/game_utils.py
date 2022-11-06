from app.services import abilities


def invoke(role: str, seat: str, targets: list) -> str:
    inputs = f"{int(seat)}"
    for t in targets:
        inputs += f", {str(t)}"
    s = f"abilities.{role}({inputs})"
    eval_result = eval(s)

    return eval_result
