#!/bin/bash

RED='\033[0;31m' # Color Red
NC='\033[0m' # No Color

# check if dependencies have version (are present)
check() {
    if ! command -v "$1" >/dev/null 2>&1; then
        printf "❌$RED $1 not found$NC \n"
        exit 1
    fi
}

# checks if dependencies are present
check python3
check pytest
check cc
check git

echo " ✅ All dependencies found"

# go into root of project
ROOT_DIR=$(git rev-parse --show-toplevel)
cd "$ROOT_DIR"

# write an pre-push hook to make sure test run before at least once commit
if [ ! -f ".git/hooks/pre-push" ]; then
cat <<'EOF' > .git/hooks/pre-push
#!/bin/bash
ROOT_DIR=$(git rev-parse --show-toplevel)
bash "$ROOT_DIR/test.bash"
EOF

# make pre-push executable
chmod +x .git/hooks/pre-push
fi

# check if an directory has changed, if so use tests for the directory
for dir in Aufgabe??/; do
    [ -d "$dir" ] || continue

    run_tests=false

    # 1️⃣ Unstaged or staged changes in folder
    if git status --porcelain "$dir" | grep -q .; then
        run_tests=true
    fi

    # 2️⃣ Committed but not pushed changes affecting folder
    if git rev-parse --abbrev-ref --symbolic-full-name @{u} >/dev/null 2>&1; then
        if git diff --name-only @{u}..HEAD -- "$dir" | grep -q .; then
            run_tests=true
        fi
    fi

    if [ "$run_tests" = true ]; then
        echo "🧪 Changes detected in $dir → running pytest"
        pytest "$dir" "-vv"
        status=$?
            if [ $status -ne 0 ]; then
                echo "❌ Tests failed in $dir"
                exit $status
            fi
    fi
done
echo " ✅ All Tests passed"