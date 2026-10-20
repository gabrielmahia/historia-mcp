"""HistoriaMCP — Kenya & East Africa Historical Archives (6 tools). All data DEMO."""
from __future__ import annotations

from typing import Annotated, Optional

from fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP(name="historia-mcp", instructions="Kenya and East Africa historical archives via MCP. DEMO.")

TIMELINE = [
    {"year": 3000, "event": "Cushitic-speaking herders settle in northern Kenya (earliest known inhabitants)"},
    {"year": 500, "event": "Bantu-speaking farmers settle in western Kenya from the Great Lakes region"},
    {"year": 900, "event": "Swahili coast trading settlements established — Mombasa, Malindi, Lamu"},
    {"year": 1498, "event": "Vasco da Gama arrives at Malindi — Portuguese era begins"},
    {"year": 1698, "event": "Omani Arabs capture Fort Jesus from Portuguese — Omani rule begins"},
    {"year": 1888, "event": "Imperial British East Africa Company (IBEAC) granted charter"},
    {"year": 1895, "event": "British East Africa Protectorate declared"},
    {"year": 1900, "event": "Uganda Railway ('Lunatic Express') completed Mombasa to Lake Victoria"},
    {"year": 1920, "event": "Kenya Colony formally established — direct British rule"},
    {"year": 1944, "event": "Kenya African Union (KAU) founded — early independence movement"},
    {"year": 1952, "event": "State of Emergency declared — Mau Mau uprising begins"},
    {"year": 1957, "event": "First African members elected to Legislative Council"},
    {"year": 1963, "event": "Kenya achieves independence — Jomo Kenyatta becomes first PM (December 12)"},
    {"year": 1964, "event": "Republic of Kenya declared — Kenyatta becomes President"},
    {"year": 1978, "event": "Kenyatta dies — Daniel arap Moi becomes President"},
    {"year": 1982, "event": "Failed coup attempt — Kenya declared one-party state"},
    {"year": 1991, "event": "Multiparty democracy restored under international pressure"},
    {"year": 2002, "event": "Mwai Kibaki wins election — first peaceful transfer of power"},
    {"year": 2007, "event": "Post-election violence — 1,300 deaths, 350,000 displaced"},
    {"year": 2008, "event": "Kofi Annan-brokered peace deal — Grand Coalition Government"},
    {"year": 2010, "event": "New Constitution adopted by referendum — devolution, Bill of Rights"},
    {"year": 2013, "event": "First election under new constitution — Uhuru Kenyatta elected"},
    {"year": 2017, "event": "Landmark Supreme Court annuls presidential election — unprecedented in Africa"},
    {"year": 2022, "event": "William Ruto elected President — first time a deputy president wins"},
]

@mcp.tool(name="kenya_history_timeline", description="Key events in Kenya's history in date order, optionally limited to a range of years. Use when someone asks what happened in a period. start_year and end_year keep events from and up to those years (inclusive); with no events in range the list is empty. Returns the source label, the events, the total and an archives pointer. A short selection labelled DEMO, not a complete history: consult the Kenya National Archives. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def kenya_history_timeline(start_year: Annotated[Annotated[int | None, Field(description="Optional first year to include.")], "Filter events from this year e.g. 1900, 1963 (independence). Leave empty for full timeline."] = None, end_year: Annotated[Annotated[int | None, Field(description="Optional last year to include.")], "Filter events up to this year e.g. 2010, 2024. Leave empty for no end limit."] = None) -> dict:
    events = TIMELINE
    if start_year: events = [e for e in events if e["year"] >= start_year]
    if end_year: events = [e for e in events if e["year"] <= end_year]
    return {"source": "DEMO — Kenya National Archives reference", "events": events,
            "total": len(events), "archive": "archives.go.ke | Kenya National Archives"}

@mcp.tool(name="independence_leaders", description="Profiles of key figures in Kenya's struggle for independence and early nationhood, with their roles, years and significance. Use when someone asks who the independence leaders were. Takes no arguments. Returns the source label and the leaders. A short selection labelled DEMO and not exhaustive: many contributors, including women and rural fighters, are not listed. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def independence_leaders() -> dict:
    return {"source": "DEMO — Kenya National Archives, Kenya History Project",
            "leaders": [
                {"name": "Jomo Kenyatta", "role": "First President of Kenya", "years": "1963–1978",
                 "significance": "Led Kenya to independence. Father of the nation. Kikuyu elder, London School of Economics graduate.",
                 "quote": "'We are not here to ask for rights from colonial powers, but to create rights.'"},
                {"name": "Oginga Odinga", "role": "First Vice President", "years": "1964–1966",
                 "significance": "Luo nationalist. Later opposition leader. Father of Raila Odinga.", "aka": "Jaramogi"},
                {"name": "Tom Mboya", "role": "Labour leader and minister", "years": "1930–1969",
                 "significance": "Organised the 'Airlift' of Kenyan students to US universities. Assassinated 1969.",
                 "legacy": "Kennedy Airlift brought 800+ Kenyans including Barack Obama Sr. to study in America"},
                {"name": "Dedan Kimathi", "role": "Mau Mau field marshal", "years": "1920–1957",
                 "significance": "Led armed resistance against British. Captured and executed 1957. National hero.",
                 "memorial": "Dedan Kimathi statue, Kimathi Street, Nairobi"},
                {"name": "Mekatilili wa Menza", "role": "Giriama resistance leader", "years": "~1840–1924",
                 "significance": "Led Giriama people against British colonialism. First major woman resistance leader in Kenya.",
                 "recognition": "Face on 400 KES coin. National heroine."},
                {"name": "Harry Thuku", "role": "Early nationalist", "years": "1895–1970",
                 "significance": "Founded Young Kikuyu Association (1921). Arrested 1922 — sparked Nairobi's first political riot."},
                {"name": "Wangari Maathai", "role": "Environmentalist and politician", "years": "1940–2011",
                 "significance": "Founded Green Belt Movement. First African woman Nobel Peace Prize laureate (2004). MP for Tetu."},
            ]}

@mcp.tool(name="cultural_heritage_sites", description="Sample Kenyan cultural and natural heritage sites (UNESCO and national) with region and significance. Use when someone asks about heritage sites in a region. region filters by matching text; if nothing matches, ALL sites are returned and region_matched is false. Returns the source label, the sites, region_matched and a National Museums of Kenya pointer. A short sample labelled DEMO, not a full register. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def cultural_heritage_sites(region: Annotated[Annotated[str | None, Field(description="Optional region such as Coast or Rift Valley; unmatched values return all sites.")], "Kenya region or county e.g."] = None) -> dict:
    """Return UNESCO and national cultural heritage sites and landmarks in Kenya."""
    SITES = [
        {"name": "Lamu Old Town", "type": "UNESCO World Heritage", "region": "Coast",
         "significance": "Best-preserved Swahili settlement in East Africa. Founded 14th century. Coral architecture.",
         "visit": "Accessible by ferry from Manda Island"},
        {"name": "Fort Jesus, Mombasa", "type": "UNESCO World Heritage", "region": "Coast",
         "significance": "Portuguese fort built 1593. Fought over 9 times. Now a museum.",
         "visit": "Old Town Mombasa | KES 1,200 adult entry"},
        {"name": "Kenya Lake System (Nakuru, Bogoria, Elementaita)", "type": "UNESCO World Heritage", "region": "Rift Valley",
         "significance": "Flamingo habitat. Over 1.5 million flamingos at peak. Geological significance."},
        {"name": "Mount Kenya National Park", "type": "UNESCO World Heritage / National Park", "region": "Central",
         "significance": "Second highest peak in Africa (5,199m). Sacred to Kikuyu people (Kĩrĩnyaga)."},
        {"name": "Kariandusi Archaeological Site", "type": "National Museum", "region": "Rift Valley",
         "significance": "Acheulean tools dated 700,000+ years. Evidence of early human habitation."},
        {"name": "Gede Ruins", "type": "National Monument", "region": "Coast",
         "significance": "13th-17th century Swahili town near Malindi. Population 2,500-3,000 at peak."},
        {"name": "Hyrax Hill", "type": "National Monument", "region": "Rift Valley",
         "significance": "Archaeological site near Nakuru. Neolithic, Iron Age, and pastoral Neolithic remains."},
        {"name": "Thimlich Ohinga", "type": "UNESCO World Heritage", "region": "Nyanza",
         "significance": "Largest and best-preserved dry-stone walled enclosure in East Africa. Built ~500 AD."},
    ]
    region_matched = None
    if region:
        by_region = [s for s in SITES if region.lower() in s["region"].lower()]
        region_matched = bool(by_region)
        SITES = by_region or SITES
    return {"source": "DEMO — Kenya National Museums, UNESCO", "sites": SITES, "region_matched": region_matched,
            "national_museums": "museums.or.ke | National Museums of Kenya"}

@mcp.tool(name="ethnic_groups_guide", description="Population share, region, language and notable traits for Kenya's larger ethnic groups, computed from the 2019 census counts (total 47.6 million), or an overview of all. Use when someone asks about a community's size or home region. group is matched by name; a group not in the sample returns a note, not a guess. Returns the source label, the group and its info, or all groups with a total-groups note. Shares are percentages of the national population; the descriptions are broad generalisations labelled DEMO and no community is homogeneous. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def ethnic_groups_guide(group: Annotated[Annotated[str | None, Field(description="Optional community name such as Luo; omit for all.")], "Ethnic group name e.g."] = None) -> dict:
    """Return cultural, linguistic, and historical information about Kenya ethnic groups."""
    GROUPS = {
        "Kikuyu": {"population_pct": 17.1, "region": "Central Kenya (Mt. Kenya region)", "language": "Gĩkũyũ (Bantu)", "known_for": "Agriculture, business, coffee and tea farming. Largest ethnic group."},
        "Luhya": {"population_pct": 14.3, "region": "Western Kenya", "language": "Multiple Luhya dialects (Bantu)", "known_for": "Agriculture, diversity (18 sub-groups), progressive politics."},
        "Kalenjin": {"population_pct": 13.4, "region": "Rift Valley", "language": "Kalenjin (Nilotic)", "known_for": "Long-distance running and Rift Valley athletics. 11+ sub-groups."},
        "Luo": {"population_pct": 10.7, "region": "Nyanza / Lake Victoria basin", "language": "Dholuo (Nilotic)", "known_for": "Fishing, education, music, political activism (Tom Mboya and Jaramogi Oginga Odinga were Luo)."},
        "Kamba": {"population_pct": 9.8, "region": "Eastern Kenya", "language": "Kikamba (Bantu)", "known_for": "Wood carving, military service, trade routes. Machakos, Kitui, Makueni counties."},
        "Somali": {"population_pct": 5.8, "region": "Northern Kenya (NFD)", "language": "Somali (Cushitic)", "known_for": "Pastoralism, trade, Islam. Mainly in Garissa, Wajir, Mandera counties."},
        "Kisii": {"population_pct": 5.7, "region": "Nyanza / Kisii highlands", "language": "Ekegusii (Bantu)", "known_for": "Dense population, agriculture (tea, banana), soapstone carving."},
        "Mijikenda": {"population_pct": 5.2, "region": "Coast", "language": "Mijikenda dialects (Bantu)", "known_for": "9 sub-groups. Kaya forests (UNESCO heritage). Swahili coast culture."},
        "Meru": {"population_pct": 4.2, "region": "Mt. Kenya region", "language": "Kimeru (Bantu)", "known_for": "Miraa (khat) production, Mount Kenya access, conservative traditions."},
        "Maasai": {"population_pct": 2.5, "region": "Rift Valley, Kajiado, Narok", "language": "Maa (Nilotic)", "known_for": "Pastoralism, warrior traditions, beadwork, iconic international recognition."},
    }
    if group:
        g = group.lower().title()
        matched = {k: v for k, v in GROUPS.items() if g in k or group.lower() in k.lower()}
        return {"source": "DEMO — Kenya National Bureau of Statistics 2019 Census", "group": group,
                "info": matched or {"note": f"Group '{group}' not in sample. Kenya has 44+ ethnic groups."}}
    return {"source": "DEMO — KNBS 2019 Census", "groups": GROUPS, "total_groups": "44+ officially recognised",
            "note": "Kenya's diversity is a strength. The constitution protects cultural rights of all communities."}

@mcp.tool(name="oral_history_resources", description="Institutions and projects that hold or digitise Kenya's oral histories and archives. Use when someone asks where to find oral history sources. Takes no arguments. Returns the source label, why oral history matters, the institutions and preservation projects. A starting list labelled DEMO: check each institution's access terms. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def oral_history_resources() -> dict:
    return {"source": "DEMO — Kenya memory institutions",
            "why_important": "East Africa's history is primarily oral. Written records from colonialism are incomplete and biased. Oral traditions preserve indigenous knowledge, genealogies, customary law, and cultural practices.",
            "institutions": [
                {"name": "Kenya National Archives (KNA)", "location": "Moi Avenue, Nairobi",
                 "holdings": "Colonial records, independence documents, photos, maps", "access": "archives.go.ke"},
                {"name": "National Museums of Kenya", "location": "Museum Hill, Nairobi",
                 "holdings": "Ethnographic collections, oral history recordings, archaeological finds", "access": "museums.or.ke"},
                {"name": "Fort Jesus Museum Library", "location": "Mombasa",
                 "holdings": "Swahili coast oral traditions, manuscripts", "access": "museums.or.ke/fort-jesus"},
                {"name": "SOAS Africa Collections", "location": "London (digital access)",
                 "holdings": "East African oral literature, colonial ethnographies", "access": "soas.ac.uk"},
                {"name": "African Digital Heritage (ADH)", "location": "Online",
                 "holdings": "3D digital heritage sites including Kenya", "access": "africandigitalheritage.org"},
                {"name": "Internet Archive - Kenya", "location": "Online",
                 "holdings": "Digitized Kenya newspapers, reports, government documents", "access": "archive.org"},
            ],
            "preservation_projects": [
                "Endangered Archives Programme (British Library) — digitises Kenyan oral traditions",
                "ELDP (Endangered Language Documentation Programme) — Kikuyu, Luo, Maasai oral traditions",
                "Masakhane NLP — training AI models on African language oral texts",
            ]}

@mcp.tool(name="historical_documents", description="Where to find key Kenyan historical documents (constitutions, colonial records, commission reports) in digital archives. Use when someone asks where to read a primary source. document_type matches by name or description; an unmatched type returns a note pointing to Kenya Law and the National Archives. Returns the source label, the document and the sources found, or all sources and the main portals. A pointer list labelled DEMO: availability changes. Read-only; no side effects.", annotations={"readOnlyHint": True, "openWorldHint": False})
def historical_documents(document_type: Annotated[Annotated[str | None, Field(description="Optional document kind such as constitution or commission report.")], "Document category e.g."] = None) -> dict:
    """Return references to historical documents, treaties, and constitutional texts relevant to Kenya."""
    SOURCES = {
        "constitution_1963": {"description": "Kenya Independence Constitution 1963", "access": "kenyalaw.org", "free": True},
        "constitution_2010": {"description": "Kenya Constitution 2010 (current)", "access": "kenyalaw.org", "free": True},
        "hola_camp_report": {"description": "Hola Massacre Report 1959 (Mau Mau)", "access": "UK National Archives (PRO)", "free": False},
        "carter_commission": {"description": "Kenya Land Commission 1932 (colonial land policy)", "access": "archive.org", "free": True},
        "dedan_kimathi_trial": {"description": "Dedan Kimathi trial transcripts 1956", "access": "Kenya National Archives", "free": False},
        "sessional_paper_10": {"description": "African Socialism and Its Application to Planning in Kenya (1965)", "access": "Kenya National Archives", "free": True},
        "waki_commission": {"description": "Commission of Inquiry into 2007/08 Post-Election Violence", "access": "knchr.org", "free": True},
        "ndung_u_commission": {"description": "Truth, Justice and Reconciliation Commission Report 2013", "access": "tjrckenya.org", "free": True},
    }
    if document_type:
        d = document_type.lower().replace(" ","_")
        matched = {k: v for k, v in SOURCES.items() if d in k or any(d in str(v[f]) for f in ["description"])}
        return {"source": "DEMO — Kenya digital archives", "document": document_type, "found": matched or {"note": "Not in sample dataset. Try kenyalaw.org or archives.go.ke"}}
    return {"source": "DEMO", "documents": SOURCES,
            "primary_portals": ["kenyalaw.org (Kenya Law)", "archives.go.ke (KNA)", "knchr.org (KNCHR)", "archive.org"]}

def main() -> None:
    """Console entry point."""
    mcp.run()
