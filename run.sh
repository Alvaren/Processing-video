for i in video_retriever client server receiver statistics; do python $i.py & done
#start "" %CD%/graphs/final.svg
# printf "\n Video has been processed. \n"
# $SHELL