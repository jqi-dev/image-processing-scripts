function resize() {
  file="$1"
  name=${file%%.*}
  thumb="${name}_400.jpg"
  banner="${name}_1200.jpg"
  convert $1 -resize 400 "$thumb"
  convert $1 -resize 1200 "$banner" 
  /Applications/ImageOptim.app/Contents/MacOS/ImageOptim "$thumb"
  /Applications/ImageOptim.app/Contents/MacOS/ImageOptim "$banner"
  /Applications/ImageOptim.app/Contents/MacOS/ImageOptim "$file" 
 }     