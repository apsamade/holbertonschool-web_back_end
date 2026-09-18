# Unittests and Integration Tests

A learning project covering unit and integration testing in Python with
`unittest`, `unittest.mock`, and `parameterized`.

## Files

- `utils.py` — generic helpers (`access_nested_map`, `get_json`, `memoize`).
- `client.py` — `GithubOrgClient` that queries the GitHub API.
- `fixtures.py` — payload fixtures used by the integration tests.
- `test_utils.py` — unit tests for `utils`.
- `test_client.py` — unit and integration tests for `client`.

## Running the tests

```
python -m unittest test_utils.py
python -m unittest test_client.py
```

## Concepts

- **Unit tests** isolate a single function; external calls are mocked.
- **Integration tests** exercise a full code path, mocking only the
  lowest-level external calls (here, `requests.get`).
