import os

"""
    Your credentials can be setted there, directly or using env var.
"""

IDRAC_IP = os.environ.get("IDRAC_IP", None)  # YOUR IDRAC IP OR HOSTNAME
IDRAC_USER = os.environ.get("IDRAC_USER", None)  # YOUR IDRAC USER NAME
IDRAC_PWD = os.environ.get("IDRAC_PWD", None)  # YOUR IDRAC PASSWORD
