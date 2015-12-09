for i in client server receiver statistics video_retriever; do python ~/documents/repositories/processing-video/$i.py & done
#start "" %CD%/graphs/final.svg
# printf "\n Video has been processed. \n"
$SHELL