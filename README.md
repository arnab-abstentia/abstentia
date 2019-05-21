## How to use this repo

```git clone "https://github.com/arnab-abstentia/abstentia"```

```cd abstentia```

```mkdir data output```

**Put the input files in data directory**

For generatingrandom uuid
--

    python generate_randomid.py [OPTIONS]

    --num_uuid   Number of uuids to be generated. Default is 20 Million.
    --len_uuid   Length of uuid string. Default is 8.
    --num_cols   Number of cols in csv. Default is 20.
    --csv_fname  Outfile name. Which will be stored in output directory. Default is 'random_uuid.csv'


For generating report
--

    python gen_report.py --csv [FILE_NAME (REQUIRED)] --xlsx [FILE_NAME (REQUIRED)] --out [FILE_NAME (OPTIONAL)]

    --csv   Name of the csv file stored in data directory in which Citites field will be searched.
    --xlsx  Name of the csv file stored in data directory in which    Citites field will be added. Must be in Microsoft xlsx format otherwise it will not work.
    --out   Output file name which will be stored is output directory. It is optional and default is 'aggregate.xlsx'
