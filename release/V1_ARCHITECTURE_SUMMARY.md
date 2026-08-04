# Version 1 Architecture Summary

The Version 1 path is ArtifactHandlingBoundary → ArtifactReceipt → registered
odop-json parser → Draft 2020-12 Schema → Structural Validator → local result.
The receipt remains the original representation; parsed values and local issues
do not replace it. Schema and validator results are local structural evidence,
not protocol conformance, verification, replay, or product decisions.
