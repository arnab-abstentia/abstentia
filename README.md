# How to use this repo

```git clone "https://github.com/arnab-abstentia/abstentia"```

```cd abstentia```

```mkdir data output```

**Put the input files in data directory. When running a script just pass the filename instead of full path.**

## Scripts

1. [generate_randomid.py](#for-generating-random-uuid)
2. [gen_report.py](#for-generating-report)
3. [calculate_average.py](#for-generating-calculating-average)

For generating random uuid
--

    python generate_randomid.py [OPTIONAL_ARGUMENTS]

    --num_uuid   Number of uuids to be generated. Default is 20 Million.
    --len_uuid   Length of uuid string. Default is 8.
    --num_cols   Number of cols in csv. Default is 20.
    --csv_fname  Outfile name. Which will be stored in output directory. Default is 'random_uuid.csv'

For generating report
--

    python gen_report.py --csv [FILE_NAME (REQUIRED)] --xlsx [FILE_NAME (REQUIRED)] --out [FILE_NAME (OPTIONAL)]

    --csv   Name of the csv file stored in data directory in which Citites field will be searched.
    --xlsx  Name of the xlsx file stored in data directory in which 'Citites' field will be added. Must be in Microsoft xlsx format otherwise it will not work.
    --out   Output file name which will be stored is output directory. It is optional and default is 'aggregate.xlsx'

For generating calculating average
--

    python calculate_average.py --city [FILE_NAME (REQUIRED)] --data [FILE_NAME (REQUIRED)] --out [FILE_NAME (OPTIONAL)]

    --city   Name of the xlsx file stored in data directory in which City frequency will be counted.
    --data  Name of the xlsx file stored in data directory in which 'Results' and 'Amount spent (INR)' will be present.
    --out   Output file name which will be stored is output directory. It is optional and default is 'avg_result.xlsx'
