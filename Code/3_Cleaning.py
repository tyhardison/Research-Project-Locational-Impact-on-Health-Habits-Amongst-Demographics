{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red144\green1\blue18;\red86\green65\blue25;\red19\green85\blue52;\red131\green0\blue165;\red0\green0\blue255;
\red0\green0\blue109;}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c63922\c8235\c8235;\cssrgb\c41569\c32157\c12941;\cssrgb\c6667\c40000\c26667;\cssrgb\c59216\c13725\c70588;\cssrgb\c0\c0\c100000;
\cssrgb\c0\c6275\c50196;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 3 \'97 DATA LOADING & CLEANING\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Produces three analytical tables: HealthStatus, HealthHabits, HealthDiet\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Load \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 raw = pd.read_csv(\cf5 \strokec5 '/content/drive/MyDrive/CSCE_676/Project/Obesity.csv'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Clean \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 df = (raw\cb1 \
\cb3       .loc[raw[\cf5 \strokec5 'Data_Value_Footnote_Symbol'\cf0 \strokec4 ].isna()]   \cf2 \strokec2 # remove suppressed rows\cf0 \cb1 \strokec4 \
\cb3       .loc[raw[\cf5 \strokec5 'Total'\cf0 \strokec4 ] != \cf5 \strokec5 'Total'\cf0 \strokec4 ]                    \cf2 \strokec2 # remove population aggregates\cf0 \cb1 \strokec4 \
\cb3       .loc[raw[\cf5 \strokec5 'Income'\cf0 \strokec4 ] != \cf5 \strokec5 'Data not reported'\cf0 \strokec4 ]       \cf2 \strokec2 # remove non-disclosed income\cf0 \cb1 \strokec4 \
\cb3       .copy()\cb1 \
\cb3 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Standardize one education spelling variant\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 df[\cf5 \strokec5 'Education'\cf0 \strokec4 ] = df[\cf5 \strokec5 'Education'\cf0 \strokec4 ].replace(\cb1 \
\cb3     \cf5 \strokec5 'some college or technical sch'\cf0 \strokec4 , \cf5 \strokec5 'Some college or technical sch'\cf0 \cb1 \strokec4 \
\cb3 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  State \u8594  Urbanicity mapping \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Based on NCHS Urban-Rural Classification Scheme (designed for health data).\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Four levels: Urban, Suburban, Rural, Mixed (states with no clear majority).\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Any state not in the map defaults to Mixed \'97 the most honest fallback.\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 URBANICITY = \{\cb1 \
\cb3     \cf2 \strokec2 # Urban\cf0 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 'California'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 'New York'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 'Illinois'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Massachusetts'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 'New Jersey'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 'Maryland'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Connecticut'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 'Washington'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 'Colorado'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Oregon'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 'Nevada'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 'Rhode Island'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'District of Columbia'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cf5 \strokec5 'Delaware'\cf0 \strokec4 :\cf5 \strokec5 'Urban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf2 \strokec2 # Suburban\cf0 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 'Pennsylvania'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'Ohio'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'Michigan'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Virginia'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'Arizona'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'Indiana'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Missouri'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'Wisconsin'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'Tennessee'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Utah'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'Kansas'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'Nebraska'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'New Hampshire'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'New Mexico'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Idaho'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cf5 \strokec5 'Maine'\cf0 \strokec4 :\cf5 \strokec5 'Suburban'\cf0 \strokec4 ,\cb1 \
\cb3     \cf2 \strokec2 # Rural\cf0 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 'Wyoming'\cf0 \strokec4 :\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cf5 \strokec5 'Montana'\cf0 \strokec4 :\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cf5 \strokec5 'North Dakota'\cf0 \strokec4 :\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'South Dakota'\cf0 \strokec4 :\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cf5 \strokec5 'Alaska'\cf0 \strokec4 :\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cf5 \strokec5 'Vermont'\cf0 \strokec4 :\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'West Virginia'\cf0 \strokec4 :\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cf5 \strokec5 'Mississippi'\cf0 \strokec4 :\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Arkansas'\cf0 \strokec4 :\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cf5 \strokec5 'Iowa'\cf0 \strokec4 :\cf5 \strokec5 'Rural'\cf0 \strokec4 ,\cb1 \
\cb3     \cf2 \strokec2 # Mixed \'97 genuinely heterogeneous states\cf0 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 'Texas'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cf5 \strokec5 'Florida'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cf5 \strokec5 'Georgia'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'North Carolina'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cf5 \strokec5 'South Carolina'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cf5 \strokec5 'Alabama'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Louisiana'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cf5 \strokec5 'Kentucky'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cf5 \strokec5 'Oklahoma'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Minnesota'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cf5 \strokec5 'Hawaii'\cf0 \strokec4 :\cf5 \strokec5 'Mixed'\cf0 \strokec4 ,\cb1 \
\cb3     \cf2 \strokec2 # National and territories\cf0 \cb1 \strokec4 \
\cb3     \cf5 \strokec5 'National'\cf0 \strokec4 :\cf5 \strokec5 'National'\cf0 \strokec4 ,\cf5 \strokec5 'Puerto Rico'\cf0 \strokec4 :\cf5 \strokec5 'Territory'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Guam'\cf0 \strokec4 :\cf5 \strokec5 'Territory'\cf0 \strokec4 ,\cf5 \strokec5 'Virgin Islands'\cf0 \strokec4 :\cf5 \strokec5 'Territory'\cf0 \strokec4 ,\cb1 \
\cb3 \}\cb1 \
\cb3 df[\cf5 \strokec5 'Region'\cf0 \strokec4 ] = df[\cf5 \strokec5 'LocationDesc'\cf0 \strokec4 ].\cf6 \strokec6 map\cf0 \strokec4 (URBANICITY).fillna(\cf5 \strokec5 'Mixed'\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Select columns needed downstream \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 GRP_COLS  = [\cf5 \strokec5 'Age(years)'\cf0 \strokec4 , \cf5 \strokec5 'Education'\cf0 \strokec4 , \cf5 \strokec5 'Sex'\cf0 \strokec4 , \cf5 \strokec5 'Income'\cf0 \strokec4 , \cf5 \strokec5 'Race/Ethnicity'\cf0 \strokec4 ]\cb1 \
\cb3 KEEP_COLS = [\cf5 \strokec5 'YearStart'\cf0 \strokec4 ,\cf5 \strokec5 'LocationDesc'\cf0 \strokec4 ,\cf5 \strokec5 'Region'\cf0 \strokec4 ,\cf5 \strokec5 'Class'\cf0 \strokec4 ,\cb1 \
\cb3              \cf5 \strokec5 'Question'\cf0 \strokec4 ,\cf5 \strokec5 'Data_Value'\cf0 \strokec4 ,\cf5 \strokec5 'Sample_Size'\cf0 \strokec4 ] + GRP_COLS\cb1 \
\cb3 df = df[KEEP_COLS].copy()\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # Confirm exactly one group column is populated per row\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 n_bad = (df[GRP_COLS].notna().\cf6 \strokec6 sum\cf0 \strokec4 (axis=\cf7 \strokec7 1\cf0 \strokec4 ) != \cf7 \strokec7 1\cf0 \strokec4 ).\cf6 \strokec6 sum\cf0 \strokec4 ()\cb1 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 print\cf0 \strokec4 (\cf5 \strokec5 "Group column check:"\cf0 \strokec4 , \cf5 \strokec5 "PASS"\cf0 \strokec4  \cf8 \strokec8 if\cf0 \strokec4  n_bad == \cf7 \strokec7 0\cf0 \strokec4  \cf8 \strokec8 else\cf0 \strokec4  \cf9 \strokec9 f\cf5 \strokec5 "WARNING \'97 \cf0 \strokec4 \{n_bad\}\cf5 \strokec5  bad rows"\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  Unpivot: 5 group columns \u8594  (Group, Group Value) \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # stack() drops nulls by default \uc0\u8594  exactly one output row per input row\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 df_long = (\cb1 \
\cb3     df.set_index([\cf5 \strokec5 'YearStart'\cf0 \strokec4 ,\cf5 \strokec5 'LocationDesc'\cf0 \strokec4 ,\cf5 \strokec5 'Region'\cf0 \strokec4 ,\cf5 \strokec5 'Class'\cf0 \strokec4 ,\cb1 \
\cb3                   \cf5 \strokec5 'Question'\cf0 \strokec4 ,\cf5 \strokec5 'Data_Value'\cf0 \strokec4 ,\cf5 \strokec5 'Sample_Size'\cf0 \strokec4 ])\cb1 \
\cb3       [GRP_COLS]\cb1 \
\cb3       .stack()\cb1 \
\cb3       .reset_index()\cb1 \
\cb3       .rename(columns=\{\cf5 \strokec5 'level_7'\cf0 \strokec4 :\cf5 \strokec5 'Group'\cf0 \strokec4 , \cf7 \strokec7 0\cf0 \strokec4 :\cf5 \strokec5 'Group Value'\cf0 \strokec4 ,\cb1 \
\cb3                         \cf5 \strokec5 'YearStart'\cf0 \strokec4 :\cf5 \strokec5 'Year'\cf0 \strokec4 ,\cf5 \strokec5 'LocationDesc'\cf0 \strokec4 :\cf5 \strokec5 'State'\cf0 \strokec4 ,\cb1 \
\cb3                         \cf5 \strokec5 'Data_Value'\cf0 \strokec4 :\cf5 \strokec5 'Percentage'\cf0 \strokec4 ,\cf5 \strokec5 'Sample_Size'\cf0 \strokec4 :\cf5 \strokec5 'Sample Size'\cf0 \strokec4 \})\cb1 \
\cb3 )\cb1 \
\
\cb3 BASE = [\cf5 \strokec5 'Year'\cf0 \strokec4 ,\cf5 \strokec5 'State'\cf0 \strokec4 ,\cf5 \strokec5 'Region'\cf0 \strokec4 ,\cf5 \strokec5 'Class'\cf0 \strokec4 ,\cf5 \strokec5 'Group'\cf0 \strokec4 ,\cf5 \strokec5 'Group Value'\cf0 \strokec4 ,\cb1 \
\cb3         \cf5 \strokec5 'Percentage'\cf0 \strokec4 ,\cf5 \strokec5 'Sample Size'\cf0 \strokec4 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  HealthStatus \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Each respondent is classified as Obese OR Overweight (mutually exclusive).\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Both are kept separately here and combined with a sum in Cell 7.\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 WS_MAP = \{\cb1 \
\cb3     \cf5 \strokec5 'Percent of adults aged 18 years and older who have obesity'\cf0 \strokec4                       : \cf5 \strokec5 'Obese'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Percent of adults aged 18 years and older who have an overweight classification'\cf0 \strokec4  : \cf5 \strokec5 'Overweight'\cf0 \strokec4 ,\cb1 \
\cb3 \}\cb1 \
\cb3 hs = df_long[df_long[\cf5 \strokec5 'Class'\cf0 \strokec4 ] == \cf5 \strokec5 'Obesity / Weight Status'\cf0 \strokec4 ].copy()\cb1 \
\cb3 hs[\cf5 \strokec5 'Weight Status'\cf0 \strokec4 ] = hs[\cf5 \strokec5 'Question'\cf0 \strokec4 ].\cf6 \strokec6 map\cf0 \strokec4 (WS_MAP)\cb1 \
\cb3 HealthStatus = hs.dropna(subset=[\cf5 \strokec5 'Weight Status'\cf0 \strokec4 ])[BASE + [\cf5 \strokec5 'Weight Status'\cf0 \strokec4 ]].reset_index(drop=\cf9 \strokec9 True\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  HealthHabits \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Five activity questions represent different behavioral thresholds.\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Each maps to (Moderate AE min, Vigorous AE min, Strength Training, No Activity).\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 ACT_MAP = \{\cb1 \
\cb3     \cf5 \strokec5 'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)'\cf0 \strokec4                                                                                                                     : (\cf7 \strokec7 150\cf0 \strokec4 , \cf7 \strokec7 75\cf0 \strokec4 ,  \cf9 \strokec9 False\cf0 \strokec4 , \cf9 \strokec9 False\cf0 \strokec4 ),\cb1 \
\cb3     \cf5 \strokec5 'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic physical activity (or an equivalent combination) and engage in muscle-strengthening activities on 2 or more days a week'\cf0 \strokec4                                : (\cf7 \strokec7 150\cf0 \strokec4 , \cf7 \strokec7 75\cf0 \strokec4 ,  \cf9 \strokec9 True\cf0 \strokec4 ,  \cf9 \strokec9 False\cf0 \strokec4 ),\cb1 \
\cb3     \cf5 \strokec5 'Percent of adults who achieve more than 300 minutes a week of moderate-intensity aerobic physical activity or 150 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)'\cf0 \strokec4                                                                                                                 : (\cf7 \strokec7 300\cf0 \strokec4 , \cf7 \strokec7 150\cf0 \strokec4 , \cf9 \strokec9 False\cf0 \strokec4 , \cf9 \strokec9 False\cf0 \strokec4 ),\cb1 \
\cb3     \cf5 \strokec5 'Percent of adults who engage in muscle-strengthening activities on 2 or more days a week'\cf0 \strokec4                                                                                                                                                                                                                             : (\cf7 \strokec7 0\cf0 \strokec4 ,   \cf7 \strokec7 0\cf0 \strokec4 ,   \cf9 \strokec9 True\cf0 \strokec4 ,  \cf9 \strokec9 False\cf0 \strokec4 ),\cb1 \
\cb3     \cf5 \strokec5 'Percent of adults who engage in no leisure-time physical activity'\cf0 \strokec4                                                                                                                                                                                                                                                    : (\cf7 \strokec7 0\cf0 \strokec4 ,   \cf7 \strokec7 0\cf0 \strokec4 ,   \cf9 \strokec9 False\cf0 \strokec4 , \cf9 \strokec9 True\cf0 \strokec4 ),\cb1 \
\cb3 \}\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9 def\cf0 \strokec4  \cf6 \strokec6 activity_label\cf0 \strokec4 (\cf10 \strokec10 row\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 """Convert activity metric tuple to a readable profile name."""\cf0 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 if\cf0 \strokec4  row[\cf5 \strokec5 'No Activity'\cf0 \strokec4 ]:               \cf8 \strokec8 return\cf0 \strokec4  \cf5 \strokec5 'No Activity'\cf0 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 if\cf0 \strokec4  row[\cf5 \strokec5 'Strength Training'\cf0 \strokec4 ] \cf9 \strokec9 and\cf0 \strokec4  row[\cf5 \strokec5 'Moderate AE (Min)'\cf0 \strokec4 ] == \cf7 \strokec7 150\cf0 \strokec4 : \cf8 \strokec8 return\cf0 \strokec4  \cf5 \strokec5 '150 Min + Strength'\cf0 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 if\cf0 \strokec4  row[\cf5 \strokec5 'Strength Training'\cf0 \strokec4 ]:         \cf8 \strokec8 return\cf0 \strokec4  \cf5 \strokec5 'Strength Only'\cf0 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 if\cf0 \strokec4  row[\cf5 \strokec5 'Moderate AE (Min)'\cf0 \strokec4 ] == \cf7 \strokec7 300\cf0 \strokec4 :  \cf8 \strokec8 return\cf0 \strokec4  \cf5 \strokec5 '300+ Min Aerobic'\cf0 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 if\cf0 \strokec4  row[\cf5 \strokec5 'Moderate AE (Min)'\cf0 \strokec4 ] == \cf7 \strokec7 150\cf0 \strokec4 :  \cf8 \strokec8 return\cf0 \strokec4  \cf5 \strokec5 '150 Min Aerobic'\cf0 \cb1 \strokec4 \
\cb3     \cf8 \strokec8 return\cf0 \strokec4  \cf5 \strokec5 'Other'\cf0 \cb1 \strokec4 \
\
\cb3 ha = df_long[df_long[\cf5 \strokec5 'Class'\cf0 \strokec4 ] == \cf5 \strokec5 'Physical Activity'\cf0 \strokec4 ].copy()\cb1 \
\cb3 ha[[\cf5 \strokec5 'Moderate AE (Min)'\cf0 \strokec4 ,\cf5 \strokec5 'Vigorous AE (Min)'\cf0 \strokec4 ,\cf5 \strokec5 'Strength Training'\cf0 \strokec4 ,\cf5 \strokec5 'No Activity'\cf0 \strokec4 ]] = (\cb1 \
\cb3     ha[\cf5 \strokec5 'Question'\cf0 \strokec4 ].\cf6 \strokec6 map\cf0 \strokec4 (ACT_MAP).apply(pd.Series)\cb1 \
\cb3 )\cb1 \
\cb3 ha[\cf5 \strokec5 'Activity Profile'\cf0 \strokec4 ] = ha.apply(activity_label, axis=\cf7 \strokec7 1\cf0 \strokec4 )\cb1 \
\cb3 HealthHabits = (ha.dropna(subset=[\cf5 \strokec5 'Moderate AE (Min)'\cf0 \strokec4 ])\cb1 \
\cb3                   [BASE + [\cf5 \strokec5 'Moderate AE (Min)'\cf0 \strokec4 ,\cf5 \strokec5 'Vigorous AE (Min)'\cf0 \strokec4 ,\cb1 \
\cb3                             \cf5 \strokec5 'Strength Training'\cf0 \strokec4 ,\cf5 \strokec5 'No Activity'\cf0 \strokec4 ,\cf5 \strokec5 'Activity Profile'\cf0 \strokec4 ]]\cb1 \
\cb3                   .reset_index(drop=\cf9 \strokec9 True\cf0 \strokec4 ))\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 # \uc0\u9472 \u9472  HealthDiet \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \u9472 \cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 DIET_MAP = \{\cb1 \
\cb3     \cf5 \strokec5 'Percent of adults who report consuming fruit less than one time daily'\cf0 \strokec4       : \cf5 \strokec5 'No Fruit'\cf0 \strokec4 ,\cb1 \
\cb3     \cf5 \strokec5 'Percent of adults who report consuming vegetables less than one time daily'\cf0 \strokec4  : \cf5 \strokec5 'No Vegetables'\cf0 \strokec4 ,\cb1 \
\cb3 \}\cb1 \
\cb3 hd = df_long[df_long[\cf5 \strokec5 'Class'\cf0 \strokec4 ] == \cf5 \strokec5 'Fruits and Vegetables'\cf0 \strokec4 ].copy()\cb1 \
\cb3 hd[\cf5 \strokec5 'No Fruits and Vegetables'\cf0 \strokec4 ] = hd[\cf5 \strokec5 'Question'\cf0 \strokec4 ].\cf6 \strokec6 map\cf0 \strokec4 (DIET_MAP)\cb1 \
\cb3 HealthDiet = (hd.dropna(subset=[\cf5 \strokec5 'No Fruits and Vegetables'\cf0 \strokec4 ])\cb1 \
\cb3                 [BASE + [\cf5 \strokec5 'No Fruits and Vegetables'\cf0 \strokec4 ]]\cb1 \
\cb3                 .reset_index(drop=\cf9 \strokec9 True\cf0 \strokec4 ))\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 print\cf0 \strokec4 (\cf9 \strokec9 f\cf5 \strokec5 "HealthStatus : \cf0 \strokec4 \{HealthStatus.shape[\cf7 \strokec7 0\cf0 \strokec4 ]\cf7 \strokec7 :,\cf0 \strokec4 \}\cf5 \strokec5  rows"\cf0 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 print\cf0 \strokec4 (\cf9 \strokec9 f\cf5 \strokec5 "HealthHabits : \cf0 \strokec4 \{HealthHabits.shape[\cf7 \strokec7 0\cf0 \strokec4 ]\cf7 \strokec7 :,\cf0 \strokec4 \}\cf5 \strokec5  rows"\cf0 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 print\cf0 \strokec4 (\cf9 \strokec9 f\cf5 \strokec5 "HealthDiet   : \cf0 \strokec4 \{HealthDiet.shape[\cf7 \strokec7 0\cf0 \strokec4 ]\cf7 \strokec7 :,\cf0 \strokec4 \}\cf5 \strokec5  rows"\cf0 \strokec4 )\cb1 \
}