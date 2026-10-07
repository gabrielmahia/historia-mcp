# historia-mcp

## Why This Exists

East African history is well documented but poorly structured for machines — timelines, independence-era figures, heritage sites and oral history sit in prose across archives. Making it queryable is what lets it be taught, cited and built on.

## Install

```bash
pip install historia-mcp
```

## Tools (6)

- **`kenya_history_timeline`** —   
  <sub>args: start_year, end_year</sub>
- **`independence_leaders`** —   
  <sub>args: no arguments</sub>
- **`cultural_heritage_sites`** — Return UNESCO and national cultural heritage sites and landmarks in Kenya.  
  <sub>args: region</sub>
- **`ethnic_groups_guide`** — Return cultural, linguistic, and historical information about Kenya ethnic groups.  
  <sub>args: group</sub>
- **`oral_history_resources`** —   
  <sub>args: no arguments</sub>
- **`historical_documents`** — Return references to historical documents, treaties, and constitutional texts relevant to Kenya.  
  <sub>args: document_type</sub>

## Example

```python
from historia_mcp.server import kenya_timeline

result = kenya_timeline()
# period, events, significance, further reading
```

## Claude Desktop Integration

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "historia-mcp": {
      "command": "python",
      "args": ["-m", "historia_mcp.server"]
    }
  }
}
```

## Data & Disclaimers

Historical reference material compiled from public sources. Oral history in particular carries contested interpretations; treat entries as a starting point for research, not a settled account.

Every tool response carries a `source` field. Responses labelled `DEMO` are
illustrative reference data, not a live feed — verify against the authority
named in the response before acting on it.

## Part of the East Africa Coordination Stack

This MCP server is part of the Kenya coordination infrastructure.
Connect it to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) —
the coordination event bus that routes signals between domains automatically.

```bash
pip install africa-coord-bus
```

All servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
Live demo: [coord-cascade-demo](https://github.com/gabrielmahia/coord-cascade-demo)

## IP & Collaboration

MIT licensed. Feedback via GitHub Issues only — pull requests are not accepted. Demo data is labeled DEMO and is not suitable for operational decisions. Full policy: [docs/architecture/IP_POLICY.md](docs/architecture/IP_POLICY.md). Security reports: see [SECURITY.md](SECURITY.md).

<!-- interconnect:v1 -->
## Part of the East Africa coordination stack

- **Install & run:** `pip install reli-cli && reli list` — the MCP servers on the [official MCP Registry](https://registry.modelcontextprotocol.io) under `io.github.gabrielmahia`
- **Evaluate any model on Swahili agent tasks:** [kipimo](https://github.com/gabrielmahia/kipimo) · [dataset](https://huggingface.co/datasets/gmahia/kipimo) · [leaderboard](https://huggingface.co/spaces/gmahia/kipimo-leaderboard)
- **Coordinate across servers:** [africa-coord-bus](https://pypi.org/project/africa-coord-bus/) — offline-first event bus with a built-in Kenya routing table
- **Datasets:** [huggingface.co/gmahia](https://huggingface.co/gmahia) · **Docs hub:** [nairobi-stack](https://github.com/gabrielmahia/nairobi-stack)

Model-agnostic by design: closed APIs, open-weight models, and small distilled models are all first-class citizens.
<!-- /interconnect:v1 -->
