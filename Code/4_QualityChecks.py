{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red15\green112\blue1;\red255\green255\blue255;\red0\green0\blue0;
\red131\green0\blue165;\red0\green0\blue255;\red144\green1\blue18;\red86\green65\blue25;\red19\green85\blue52;
}
{\*\expandedcolortbl;;\cssrgb\c0\c50196\c0;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c59216\c13725\c70588;\cssrgb\c0\c0\c100000;\cssrgb\c63922\c8235\c8235;\cssrgb\c41569\c32157\c12941;\cssrgb\c6667\c40000\c26667;
}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # CELL 4 \'97 DATA QUALITY CHECKS\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # Coverage audit across all three tables before any analysis\cf0 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 # \uc0\u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \u9552 \cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 for\cf0 \strokec4  name, tbl \cf6 \strokec6 in\cf0 \strokec4  [(\cf7 \strokec7 'HealthStatus'\cf0 \strokec4 , HealthStatus),\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3                    (\cf7 \strokec7 'HealthHabits'\cf0 \strokec4 , HealthHabits),\cb1 \
\cb3                    (\cf7 \strokec7 'HealthDiet'\cf0 \strokec4 ,   HealthDiet)]:\cb1 \
\cb3     \cf8 \strokec8 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 "\\n\cf0 \strokec4 \{\cf7 \strokec7 '\uc0\u9472 '\cf0 \strokec4 *\cf9 \strokec9 50\cf0 \strokec4 \}\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \
\cb3     \cf8 \strokec8 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 " \cf0 \strokec4 \{name\}\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \
\cb3     \cf8 \strokec8 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 "\cf0 \strokec4 \{\cf7 \strokec7 '\uc0\u9472 '\cf0 \strokec4 *\cf9 \strokec9 50\cf0 \strokec4 \}\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \
\cb3     \cf8 \strokec8 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 "  Years         : \cf0 \strokec4 \{\cf8 \strokec8 sorted\cf0 \strokec4 (tbl[\cf7 \strokec7 'Year'\cf0 \strokec4 ].unique())\}\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \
\cb3     \cf8 \strokec8 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 "  States        : \cf0 \strokec4 \{tbl[\cf7 \strokec7 'State'\cf0 \strokec4 ].nunique()\}\cf7 \strokec7  unique"\cf0 \strokec4 )\cb1 \
\cb3     \cf8 \strokec8 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 "  Groups        : \cf0 \strokec4 \{tbl[\cf7 \strokec7 'Group'\cf0 \strokec4 ].unique().tolist()\}\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \
\cb3     \cf8 \strokec8 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 "  Regions       : \cf0 \strokec4 \{tbl[\cf7 \strokec7 'Region'\cf0 \strokec4 ].unique().tolist()\}\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \
\cb3     \cf8 \strokec8 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 "  Sample Size   :\\n\cf0 \strokec4 \{tbl[\cf7 \strokec7 'Sample Size'\cf0 \strokec4 ].describe().\cf8 \strokec8 round\cf0 \strokec4 (\cf9 \strokec9 0\cf0 \strokec4 ).to_string()\}\cf7 \strokec7 "\cf0 \strokec4 )\cb1 \
\cb3     \cf8 \strokec8 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 "  n < 50        : \cf0 \strokec4 \{(tbl[\cf7 \strokec7 'Sample Size'\cf0 \strokec4 ] < \cf9 \strokec9 50\cf0 \strokec4 ).\cf8 \strokec8 sum\cf0 \strokec4 ()\}\cf7 \strokec7  rows"\cf0 \strokec4 )\cb1 \
\cb3     \cf8 \strokec8 print\cf0 \strokec4 (\cf6 \strokec6 f\cf7 \strokec7 "  Weighted mean : \cf0 \strokec4 \{w_mean(tbl, \cf7 \strokec7 'Percentage'\cf0 \strokec4 )\cf9 \strokec9 :.1f\cf0 \strokec4 \}\cf7 \strokec7 %"\cf0 \strokec4 )\cb1 \
}