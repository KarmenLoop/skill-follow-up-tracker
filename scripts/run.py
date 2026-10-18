"""Surface due follow-ups and stop conditions from an outreach ledger."""
from runtime import *

def process(data):
    now=instant(data["now"])
    limit=integer(data["max_attempts"],"max_attempts",1)
    rows=records(data,"contacts")
    unique(rows)
    result={"due":[],"scheduled":[],"stopped":[]}
    for row in rows:
        text(row.get("name"),"name")
        state=choice(row.get("status"),("waiting","replied","closed"),"status")
        attempts=integer(row.get("attempts"),"attempts")
        due=instant(row["next_check"])
        expires=instant(row["expires"]) if row.get("expires") else None
        reason=state if state!="waiting" else "attempt_cap" if attempts>=limit else "expired" if expires and now>=expires else None
        if reason: result["stopped"].append(dict(row,stop_reason=reason))
        else: result["due" if due<=now else "scheduled"].append(row)
    for key in ("due","scheduled"):
        result[key].sort(key=lambda x:(instant(x["next_check"]),x["id"]))
    return result

if __name__ == "__main__":
    sys.exit(main(process, "Surface due follow-ups and stop conditions from an outreach ledger."))
