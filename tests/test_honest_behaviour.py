from historia_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_ethnic_shares_match_the_2019_census_counts():
    """Computed from KNBS 2019 counts over 47,564,296: Kalenjin 6,358,113 = 13.4%, Luo 5,066,966 = 10.7%, Kamba 4,663,910 = 9.8%."""
    g = _fn("ethnic_groups_guide")(None)["groups"]
    assert (g["Kalenjin"]["population_pct"], g["Luo"]["population_pct"], g["Kamba"]["population_pct"]) == (13.4, 10.7, 9.8)


def test_no_present_tense_claims_about_named_politicians_remain():
    text = str(_fn("ethnic_groups_guide")(None))
    assert "Ruto is" not in text and "Raila Odinga is" not in text


def test_an_unmatched_heritage_region_is_flagged_not_silently_all_sites():
    assert _fn("cultural_heritage_sites")("Atlantis")["region_matched"] is False and _fn("cultural_heritage_sites")("Coast")["region_matched"] is True
