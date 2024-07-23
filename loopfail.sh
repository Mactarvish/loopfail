SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"  
AA_PY_PATH="$SCRIPT_DIR/_loopfail.py"  
python "$AA_PY_PATH" $@
