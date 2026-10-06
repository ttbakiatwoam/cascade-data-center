#!/usr/bin/env bash
set -u

FORM='https://docs.google.com/forms/d/e/1FAIpQLSez9hfMvtFT9ME96bN0J2wK14d57DDhZLc4ksjsuHIOtmiI4A/formResponse'
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
CSV="${CSV:-$SCRIPT_DIR/../dataset/community/questions.csv}"
PROGRESS="${PROGRESS:-$HOME/simple-mining-forum/.submission-progress}"

[[ -f "$CSV" ]] || { echo "ERROR: Missing $CSV"; exit 1; }

total=$(python3 -c 'import csv,sys; f=open(sys.argv[1],newline="",encoding="utf-8-sig"); r=csv.DictReader(f); assert r.fieldnames==["Topic","Question"], r.fieldnames; rows=list(r); assert all((x.get("Topic") or "").strip() and (x.get("Question") or "").strip() for x in rows); print(len(rows))' "$CSV") || exit 1

start=0
if [[ -f "$PROGRESS" ]]; then
    read -r start < "$PROGRESS"
fi

[[ "$start" =~ ^[0-9]+$ ]] || { echo 'ERROR: Invalid progress file'; exit 1; }
(( start <= total )) || { echo 'ERROR: Progress exceeds CSV row count'; exit 1; }
(( start < total )) || { echo "All $total questions are already marked submitted."; exit 0; }

read -r -p 'First and Last Name: ' NAME
[[ -n "$NAME" ]] || { echo 'ERROR: Name cannot be blank'; exit 1; }

read -r -p 'Street Address (City, State, Zip): ' ADDRESS
[[ -n "$ADDRESS" ]] || { echo 'ERROR: Address cannot be blank'; exit 1; }

remaining=$((total - start))

echo "Total: $total | Already submitted: $start | Remaining: $remaining"
echo 'Delay: random 60-90 seconds between successful submissions.'

IFS=$'\t' read -r first_topic first_question < <(
    python3 -c 'import csv,sys; rows=list(csv.DictReader(open(sys.argv[1],newline="",encoding="utf-8-sig"))); r=rows[int(sys.argv[2])]; print(r["Topic"]+"\t"+r["Question"])' "$CSV" "$start"
)

echo "Next: [$first_topic] $first_question"

read -r -p "Type SUBMIT to send the remaining $remaining questions: " confirm
[[ "$confirm" == 'SUBMIT' ]] || { echo 'Cancelled. Nothing was submitted.'; exit 0; }

for ((n=start+1; n<=total; n++)); do

    IFS=$'\t' read -r topic question < <(
        python3 -c 'import csv,sys; rows=list(csv.DictReader(open(sys.argv[1],newline="",encoding="utf-8-sig"))); r=rows[int(sys.argv[2])-1]; print(r["Topic"]+"\t"+r["Question"])' "$CSV" "$n"
    )

    response="/tmp/simple-mining-response-$n.html"
    headers="/tmp/simple-mining-headers-$n.txt"

    printf '\n[%d/%d] %s\n%s\nSubmitting...\n' \
        "$n" "$total" "$topic" "$question"

    if ! status=$(curl \
        --disable \
        -sS \
        --connect-timeout 15 \
        --max-time 45 \
        --retry 0 \
        -D "$headers" \
        -o "$response" \
        -w '%{http_code}' \
        -X POST "$FORM" \
        --data-urlencode "entry.1845686698=$NAME" \
        --data-urlencode "entry.1356760338=$ADDRESS" \
        --data-urlencode "entry.191983961=$topic" \
        --data-urlencode "entry.2088474544=$question"); then

        echo 'ERROR: curl failed. No retry. Stopping.'
        exit 1
    fi

    echo "HTTP status: $status"

    if [[ "$status" != '200' ]]; then
        echo "ERROR: Google returned HTTP $status. No retry. Stopping."
        echo "Response: $response"
        echo "Headers:  $headers"
        exit 1
    fi

    if grep -Eqi \
        'your response has been recorded|submit another response' \
        "$response"; then

        echo 'Google Forms confirmation detected.'

    elif grep -Eqi \
        'unusual traffic|automated queries|our systems have detected|/sorry/|too many requests|rate limit|access denied|temporarily blocked|captcha' \
        "$response"; then

        echo 'ERROR: Possible Google challenge/rate-limit/block page.'
        echo 'No retry. Stopping.'
        echo "Response: $response"
        echo "Headers:  $headers"
        exit 1

    else
        echo 'ERROR: HTTP 200 received, but the normal Google Forms'
        echo 'confirmation was not found. No retry. Stopping.'
        echo "Response: $response"
        echo "Headers:  $headers"
        exit 1
    fi

    printf '%s\n' "$n" > "$PROGRESS"
    echo "Confirmed and recorded: $n/$total"

    if (( n < total )); then
        delay=$((60 + RANDOM % 31))
        echo "Waiting $delay seconds..."
        sleep "$delay"
    fi

done

echo "Finished: $total questions successfully submitted."
