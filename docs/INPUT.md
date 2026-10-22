# Input and output

English | [简体中文](input.zh-CN.md)

Supply a UTF-8 JSON object (maximum 10 MiB). Use `--input PATH` for a file or `--input -` for standard input. Run `--version` to inspect the installed helper version. Duplicate JSON keys and non-finite JSON constants are rejected. Arrays are required unless documented as optional. IDs must be stable and unique. Dates use ISO 8601; timestamps require an explicit UTC offset.

| Field | Contract |
| --- | --- |
| now | Offset-aware timestamp. |
| max_attempts | Positive integer. |
| contacts | Objects: unique id, name, status (waiting/replied/closed), attempts integer, next_check timestamp, optional expires timestamp. |

## Example

```json
{
  "now": "2026-10-19T12:00:00Z",
  "max_attempts": 3,
  "contacts": [
    {
      "id": "c1",
      "name": "Example partner",
      "status": "waiting",
      "attempts": 1,
      "next_check": "2026-10-19T10:00:00Z"
    },
    {
      "id": "c2",
      "name": "Former lead",
      "status": "replied",
      "attempts": 1,
      "next_check": "2026-10-18T10:00:00Z"
    }
  ]
}
```

## Result

due, scheduled, and stopped lists, with stop_reason on stopped records.

See [the complete sample result](../examples/expected.json). Exit 0 means processing completed, not that all reported findings passed.

## Errors and side effects

The helper makes no network requests and executes no submitted commands. It reads the input and explicitly documented local paths. It writes only a requested new output file; stdout is the default. Invalid input exits 2. Existing output is preserved. An output write failure can leave a partial new file; remove that file before retrying. Installation is a separate explicit action.
