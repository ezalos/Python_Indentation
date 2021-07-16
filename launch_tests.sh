cp -r tests tests_copy
# python3 testor.py > curr_tests.txt
python3 testor.py
rm -r tests_copy
# diff curr_tests.txt last_tests.txt
# cat curr_tests.txt > last_tests.txt   