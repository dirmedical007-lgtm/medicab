from rest_framework.test import APIClient
def test_patient_crud(db, medecin):
    c = APIClient()
    from rest_framework_simplejwt.tokens import RefreshToken
    token = str(RefreshToken.for_user(medecin).access_token)
    c.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    r = c.post("/api/v1/patients/", {"first_name":"Ali","last_name":"Y","dob":"1992-01-01"}, format="json")
    assert r.status_code == 201
    pid = r.data["id"]
    r = c.get("/api/v1/patients/")
    assert r.status_code == 200
    assert any(p["id"]==pid for p in r.data)
