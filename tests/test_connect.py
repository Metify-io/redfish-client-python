from redfish_client import connect


def test_connect(requests_mock):
    requests_mock.get(
        "https://demo.dev/redfish/v1",
        status_code=200,
        json={
            "Chassis": {"@odata.id": "/redfish/v1/Chassis"},
            "Links": {"Sessions": {"@odata.id": "/redfish/v1/SessionService/Sessions"}},
        },
    )
    requests_mock.post(
        "https://demo.dev/redfish/v1/SessionService/Sessions",
        status_code=201,
        headers={"X-Auth-Token": "fake-token", "Location": "fake-location"},
        json=dict(hello="fish3"),
    )
    conn = connect("https://demo.dev/", "user", "pass")
    assert conn


def test_connect_nulls(requests_mock):
    requests_mock.get(
        "https://demo.dev/redfish/v1",
        status_code=200,
        json={
            "foo": None,
            "Chassis": {"@odata.id": "/redfish/v1/Chassis"},
            "Links": {"Sessions": {"@odata.id": "/redfish/v1/SessionService/Sessions"}},
        },
    )
    requests_mock.post(
        "https://demo.dev/redfish/v1/SessionService/Sessions",
        status_code=201,
        headers={"X-Auth-Token": "fake-token", "Location": "fake-location"},
        json=dict(hello="fish3"),
    )
    conn = connect("https://demo.dev/", "user", "pass")
    assert conn
