"""Live tools: parsing, provenance, validation and failure behaviour, with the network mocked (CI never depends on the services)."""
import urllib.error

from historia_mcp import server


def _boom(url, params=None, timeout=20.0):
    raise urllib.error.URLError("down")

def test_wikidata_lookup_returns_ids_and_links(monkeypatch):
    monkeypatch.setattr(server, "_live_get", lambda url, params=None, timeout=20.0: {"search": [{"id": "Q610057", "label": "Dedan Kimathi", "description": "Kenyan leader"}]})
    r = server.wikidata_lookup("Dedan Kimathi", 1)
    assert r["results"] == [{"id": "Q610057", "label": "Dedan Kimathi", "description": "Kenyan leader", "url": "https://www.wikidata.org/wiki/Q610057"}] and "CC0" in r["attribution"]


def test_wikidata_lookup_failure_and_bad_input_never_give_results(monkeypatch):
    monkeypatch.setattr(server, "_live_get", _boom)
    assert "results" not in server.wikidata_lookup("Lamu") and "error" in server.wikidata_lookup("") and "error" in server.wikidata_lookup("Lamu", 50)
