from flask import Flask, render_template, request
app = Flask(__name__)

# PDA-based palindrome checker
def is_palindrome_pda(string):
    if len(string) < 8:
        return False, "Rejected: String must be at least 8 characters long."

    stack = []
    mid = len(string) // 2

    # Push first half onto stack
    for i in range(mid):
        stack.append(string[i])

    # Skip middle character if odd length
    start_second_half = mid if len(string) % 2 == 0 else mid + 1

    # Pop and compare
    for i in range(start_second_half, len(string)):
        if len(stack) == 0:
            return False, "Rejected: Stack empty too early (not a palindrome)."
        top = stack.pop()
        if top != string[i]:
            return False, f"Rejected: String is not palindrome."

    if len(stack) == 0:
        return True, "Accepted: This string is a palindrome according to PDA rules."
    else:
        return False, "Rejected: Stack not empty (extra unmatched characters)."


# Home route with form
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_input = request.form["string_input"]
        _, result = is_palindrome_pda(user_input)
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
