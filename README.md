# AWS tag schema proof of concept

A proof of concept demonstrating tag schema generation from a source input file into a set of tag policies suitable for use in AWS.

The purpose of this is to group tagging policies together for the same tag, which should reduce the risk of inconsistency.

We have chosen TOML for the input format, for no particular reason other than to emphasise that transformation is necessary in order to produce a real policy.

The demo input schema is called
[sample-schema.toml](./sample-schema.toml).

## Installing and running the demo

```
poetry install
poetry run python process.py
```
