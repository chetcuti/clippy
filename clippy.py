#!/usr/bin/env python3
"""
Author: Greg Chetcuti <greg@chetcuti.com>
Date: 2022-08-06
Purpose: Clippy -- Manipulate the Clipboard text
"""
import argparse
import random

import pyperclip


# =============================================================================
# Main                                                                     Main
# ----------------------------------------------------------
def main():
    """Run the main program"""
    args = get_args()

    clipboard_text = pyperclip.paste()
    clipboard_lines = clipboard_text.split("\n")
    full_text = manipulate_text(clipboard_lines, args.type)
    pyperclip.copy(full_text)


# =============================================================================
# Functions                                                           Functions
# ----------------------------------------------------------
def manipulate_text(text, manipulation_type):
    """Manipulate the text"""
    final_lines = []
    full_text = ""

    # Sort rows ASC
    if manipulation_type == "asc":

        final_lines = sorted(text, key=str.casefold)

    # Add a dash to the beginning of each line
    elif manipulation_type == "dash":

        final_lines = ["- " + x for x in text]

    # Sort rows DESC
    elif manipulation_type == "desc":

        final_lines = sorted(text, key=str.casefold, reverse=True)

    # Shuffle the lines
    elif manipulation_type == "shuf":

        final_lines = text
        random.shuffle(final_lines)

    # Select one random result
    elif manipulation_type == "rand":

        final_lines = text
        random.shuffle(final_lines)
        del final_lines[1::]

    for line in final_lines:
        full_text = full_text + line + "\n"

    return full_text.removesuffix("\n")


# =============================================================================
# Arguments                                                           Arguments
# ----------------------------------------------------------
def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Clippy -- Manipulate the Clipboard text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-t",
        "--type",
        default="asc",
        help="Which type of text manipulation to use? (asc, dash, desc, rand, shuf)",
        metavar="str",
        type=str,
    )
    return parser.parse_args()


# ----------------------------------------------------------
if __name__ == "__main__":
    main()
