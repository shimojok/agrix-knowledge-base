
```text
PS C:\Users\user> "agrix-knowledge-base"
agrix-knowledge-base
PS C:\Users\user> "│"
│
PS C:\Users\user> $n = $rows.Count
PS C:\Users\user> for ($i = 0; $i -lt $n; $i++) {
>>     $branch = if ($i -eq $n-1 -and $files.Count -eq 0) { "└──" } else { "├──" }
>>     "{0} {1,-32} {2,6}" -f $branch, $rows[$i].Name, $rows[$i].Count.ToString("N0")
>> }
├── 00_inbox                          2,534
├── 01_Planetary_Problems               246
├── 02_Biological_Systems                69
├── 03_MBT55                            534
├── 04_AGRIX                            923
├── 05_AgriWare                          78
├── 06_PBPE                             509
├── 07_HealthBook                       727
├── 08_mbt_kampolibrary                 219
├── 09_MBT_漢方代謝ライブラリー            161
├── 10_MBT_Probiotics                   100
├── 11_AI Development                   173
├── 22_Claude                           104
├── dailynote                           288
├── data                                  1
├── slides                               37
├── Templates                             1
PS C:\Users\user> for ($j = 0; $j -lt $files.Count; $j++) {
>>     $branch = if ($j -eq $files.Count-1) { "└──" } else { "├──" }
>>     "{0} {1}" -f $branch, $files[$j].Name
>> }
├── .gitignore
├── 2026-09-21.md
├── agrix-knowledge-base-tree.txt
├── bionexus-engine-tree.txt
├── GitHub リポジトリに関して.md
├── kb006. 着手内容と実装ステップ.md
└── agrix-knowledge-base の構造.md
```

