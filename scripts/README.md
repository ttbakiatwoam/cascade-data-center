# Repository tools

Run commands from the repository root unless otherwise noted. Python 3 and Bash are required; the optional submission helper also uses curl.

## Check the collection

```sh
python3 scripts/check-repository.py
```

This checks local Markdown targets and heading fragments, preserved-source hashes, the CSV schema and row count, and Bash syntax. It performs no network requests or question submissions. Source paths in `sources/SHA256SUMS` are relative to the repository root.

## Optional question-submission helper

The [submission helper](submit-questions.sh) reads the [76-question CSV](../dataset/community/questions.csv). Its default CSV path is resolved from the script location, so it can be invoked from another working directory. `CSV` can override the input path.

The existing default progress path, `$HOME/simple-mining-forum/.submission-progress`, is retained to avoid losing prior submission state. `PROGRESS` can override it. The progress directory must exist; keep an existing progress file when using the same question list.

From Bash, Zsh, or Fish, invoke the helper explicitly with Bash:

```sh
mkdir -p "$HOME/simple-mining-forum"
bash ./scripts/submit-questions.sh
```

The helper prompts for the operator's required name/address, shows the next question, and requires typing `SUBMIT` before it sends anything. It stops on failed requests, rate limits, anti-abuse challenges, or unexpected responses. Do not use it to bypass access controls. A changed question list needs deliberate review of the associated progress state.

Repository checks never execute this helper or send form responses. Do not commit progress files or response/header captures containing participant information.
