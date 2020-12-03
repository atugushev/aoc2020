if [ -z "$AOC_SESSION" ]
then
    echo "\$AOC_SESSION env is required"
    exit 1
fi

padded_day=$(printf "%02d" $1)
current_year=$(date +"%Y")

curl https://adventofcode.com/$current_year/day/$1/input \
    -o "day$padded_day/input.txt" \
    --cookie "session=$AOC_SESSION"
