for x in load_*.sh
do
  echo "$x"
  . "$x"
  ./generate.py
done
