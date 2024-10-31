python3 scripts/download_lfw_dataset.py

source_file="~/.cache/kagglehub/datasets/atulanandjha/lfwpeople/versions/3/lfw-funneled.tgz"
target_dir="../"

tar -xvzf "$source_file" -C "$target_dir"

echo "Dataset has been downloaded and extracted to $target_dir"