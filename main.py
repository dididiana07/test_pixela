import requests
import datetime

TOKEN = ""
USERNAME = ""


def create_pixela_user(username, token):
    """Create Pixela account."""
    request_body = {
        "token": f"{token}",
        "username": f"{username}",
        "agreeTermsOfService": "yes",
        "notMinor": "no"
    }
    pixela_create_user_response = requests.post(url=" https://pixe.la/v1/users",
                                                json=request_body)
    return pixela_create_user_response.json()


def delete_pixela_user(username, token):
    """Delete your Pixela account."""
    headers = {
        "X-USER-TOKEN": {token}
    }
    pixela_delete_user_response = requests.delete(url=f"https://pixe.la/v1/users/{username}",
                                                  headers=headers)
    return pixela_delete_user_response.json()


def change_pixela_token(username, new_token, old_token):
    """Update your Pixela token."""
    headers = {
        "X-USER-TOKEN": f"{old_token}"
    }
    request_body = {
        "newToken": {new_token}
    }
    pixela_update_user_response = requests.put(url=f"https://pixe.la/v1/users/{username}",
                                               headers=headers, json=request_body)
    return pixela_update_user_response.json()


def create_pixela_graph(id_graph, name, unit, type, color, **kwargs):
    """Add a graphic to your Pixela account."""
    headers = {
        "X-USER-TOKEN": kwargs["token"]
    }
    request_body = {
        "id": f"{id_graph}",
        "name": f"{name}",
        "unit": f"{unit}",
        "type": f"{type}",
        "color": f"{color}"
    }
    pixela_create_graph_response = requests.post(url=f"https://pixe.la/v1/users/{kwargs['user']}/graphs",
                                                 headers=headers, json=request_body)
    return pixela_create_graph_response.json()


def post_pixel(token, username, quantity: str, graph_id):
    """Add a pixel to the graph. You need to provide the graph id to identify which graph ypu want to access."""
    current_day = datetime.datetime.now().date().strftime("%Y%m%d")
    header = {
        "X-USER-TOKEN": f"{token}"
    }
    request_body = {
        "date": f"{current_day}",
        "quantity": f"{quantity}"
    }
    pixela_post_pixel_response = requests.post(url=f"https://pixe.la/v1/users/{username}/graphs/{graph_id}",
                                               headers=header,
                                               json=request_body)
    return pixela_post_pixel_response.json()


def update_pixel(day: str, token, username, quantity, **kwargs):
    """Update a pixel from the graph."""
    headers = {
        "X-USER-TOKEN": f"{token}"
    }
    request_body = {
        "quantity": f"{quantity}"
    }
    pixela_update_pixel_response = requests.put(
        url=f"https://pixe.la/v1/users/{username}/graphs/{kwargs['id_graph']}/{day}",
        json=request_body,
        headers=headers)
    pixela_update_pixel_response.json()


def delete_pixel(day: str, **kwargs):
    """Delete the pixel from the given day."""
    headers = {
        "X-USER-TOKEN": f"{kwargs['token']}"
    }
    pixela_delete_pixel_response = requests.delete(
        url=f"https://pixe.la/v1/users/{kwargs['user']}/graphs/{kwargs['id_graph']}/{day}", headers=headers)

    return pixela_delete_pixel_response.json()



