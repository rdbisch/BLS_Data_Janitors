# Package all of the files required for supplemntal zip
# rdb4

rm -fr supplemental
rm -f supplemental.zip

mkdir supplemental
cd supplemental
mkdir operation_history
cp ../01_openrefine/*json operation_history
cp ../03_python/f04*py operation_history
cp ../03_python/f05*py operation_history

mkdir queries
cp ../04_sql/Queries.txt queries
cp ../04_sql/s04_ResolveViolations.ipynb queries
cp ../06_provenance/p06_ExtractingProvenance.py queries
cp ../06_provenance/provenance\ rules\ and\ queries.txt queries/

mkdir workflow
cp ../05_yesworkflow/*.yw workflow
cp ../05_yesworkflow/*.gv workflow

echo https://www.dropbox.com/sh/w36btljjgjk8v5e/AACShbDvzauP_4-jcNinrY_Ba?dl=0 > Data_Link.txt
echo https://github.com/rdbisch/BLS_Data_Janitors >> Data_Link.txt

cd ..
zip -r supplemeental.zip supplemental/
rm -fr supplemental
