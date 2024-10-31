
source_dir="./lfw_funneled"
target_dir="./images/face-images/positive"

mkdir -p "$target_dir"

find "$source_dir" -type f -name "*.jpg" -exec mv {} "$target_dir" \;

echo "All images have been moved to $target_dir"
