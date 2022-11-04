from app.services import abilities


def invoke(role: str, seat: int, targets: list) -> str:
    inputs = f"{seat}"
    for t in targets:
        inputs += f", {str(t)}"
    s = f"abilities.{role}({inputs})"
    eval_result = eval(s)

    return eval_result
