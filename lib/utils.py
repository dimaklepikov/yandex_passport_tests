"""Utils module is used to store utility functions for any purposes"""
import requests


def verify_response(response, reverse: bool = False):
    """Response verification to verify response"""
    if reverse:
        if not response.ok:
            if 400 <= response.status_code < 500:
                raise requests.exceptions.HTTPError(f"Client Error: {response.status_code} - {response.reason}")
            elif 500 <= response.status_code < 600:
                raise requests.exceptions.HTTPError(f"Server Error: {response.status_code} - {response.reason}")
            else:
                raise requests.exceptions.HTTPError(f"Unexpected Error: {response.status_code} - {response.reason}")
    else:
        if response.ok:
            raise requests.exceptions.HTTPError(f"Unexpected positive result: {response.status_code} - {response.reason}")