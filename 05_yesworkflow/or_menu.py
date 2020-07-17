#@begin CleanMenu
#@desc or2yw conversion
#@param newColumnName:location_cluster
#@param col-name:event
#@param col-name:event_loop
#@param col-name:currency
#@param col-name:call_number
#@param newColumnName:event_cluster
#@param col-name:sponsor
#@param col-name:currency_symbol
#@param newColumnName:sponsor_cluster
#@param col-name:physical_description
#@param col-name:keywords
#@param oldColumnName:sponsor_grel
#@param col-name:location
#@param expression:grel:value.replace(""",_"")
#@param expression:value.toLowercase()
#@param expression:grel:value.replace("(","")
#@param col-name:venue
#@param col-name:notes
#@param expression:grel:value.replace(")","")
#@param expression:value.trim()
#@param col-name:sponsor_grel
#@param col-name:location_type
#@param expression:grel:value.replace("[","")
#@param col-name:location_cluster
#@param col-name:status
#@param expression:value.toNumber()
#@param expression:grel:value.replace(";",_"")
#@param col-name:venue_cluster
#@param expression:grel:toString(toDate(value),"yyyy-MM-dd")
#@param col-name:page_count
#@param newColumnName:event_loop
#@param col-name:occasion_cluster
#@param col-name:language
#@param col-name:place
#@param oldColumnName:event_loop
#@param col-name:id
#@param newColumnName:venue_cluster
#@param expression:value.replace(/\\s+/,'_')
#@param col-name:occasion
#@param col-name:dish_count
#@param expression:value.toDate()
#@param col-name:place_cluster
#@param newColumnName:occasion_cluster
#@param expression:grel:value.replace("?","")
#@param newColumnName:sponsor_grel
#@param col-name:date
#@param col-name:name
#@param col-name:event_cluster
#@param newColumnName:place_cluster
#@param expression:grel:value.replace("]","")
#@in Menu @URI file:../raw_data/Menu.csv.gz
#@out Menu_clean @URI file:../01_openrefine/Menu_clean.csv.gz
#@begin core/column-removal0#@desc Remove column name
#@param col-name:name
#@in Menu
#@out table1
#@end core/column-removal0
#@begin core/text-transform0#@desc Text transform on cells in column id using expression value.trim()
#@param col-name:id
#@param expression:value.trim()
#@in table1
#@out table2
#@end core/text-transform0
#@begin core/text-transform1#@desc Text transform on cells in column sponsor using expression value.trim()
#@param col-name:sponsor
#@param expression:value.trim()
#@in table2
#@out table3
#@end core/text-transform1
#@begin core/text-transform2#@desc Text transform on cells in column event using expression value.trim()
#@param col-name:event
#@param expression:value.trim()
#@in table3
#@out table4
#@end core/text-transform2
#@begin core/text-transform3#@desc Text transform on cells in column venue using expression value.trim()
#@param col-name:venue
#@param expression:value.trim()
#@in table4
#@out table5
#@end core/text-transform3
#@begin core/text-transform4#@desc Text transform on cells in column place using expression value.trim()
#@param col-name:place
#@param expression:value.trim()
#@in table5
#@out table6
#@end core/text-transform4
#@begin core/text-transform5#@desc Text transform on cells in column physical_description using expression value.trim()
#@param col-name:physical_description
#@param expression:value.trim()
#@in table6
#@out table7
#@end core/text-transform5
#@begin core/text-transform6#@desc Text transform on cells in column id using expression value.replace(/\\s+/,' ')
#@param col-name:id
#@param expression:value.replace(/\\s+/,'_')
#@in table7
#@out table8
#@end core/text-transform6
#@begin core/text-transform7#@desc Text transform on cells in column occasion using expression value.trim()
#@param col-name:occasion
#@param expression:value.trim()
#@in table8
#@out table9
#@end core/text-transform7
#@begin core/text-transform8#@desc Text transform on cells in column notes using expression value.trim()
#@param col-name:notes
#@param expression:value.trim()
#@in table9
#@out table10
#@end core/text-transform8
#@begin core/text-transform9#@desc Text transform on cells in column call_number using expression value.trim()
#@param col-name:call_number
#@param expression:value.trim()
#@in table10
#@out table11
#@end core/text-transform9
#@begin core/text-transform10#@desc Text transform on cells in column keywords using expression value.trim()
#@param col-name:keywords
#@param expression:value.trim()
#@in table11
#@out table12
#@end core/text-transform10
#@begin core/text-transform11#@desc Text transform on cells in column language using expression value.trim()
#@param col-name:language
#@param expression:value.trim()
#@in table12
#@out table13
#@end core/text-transform11
#@begin core/text-transform12#@desc Text transform on cells in column language using expression value.trim()
#@param col-name:language
#@param expression:value.trim()
#@in table13
#@out table14
#@end core/text-transform12
#@begin core/text-transform13#@desc Text transform on cells in column date using expression value.trim()
#@param col-name:date
#@param expression:value.trim()
#@in table14
#@out table15
#@end core/text-transform13
#@begin core/text-transform14#@desc Text transform on cells in column location using expression value.trim()
#@param col-name:location
#@param expression:value.trim()
#@in table15
#@out table16
#@end core/text-transform14
#@begin core/text-transform15#@desc Text transform on cells in column location_type using expression value.trim()
#@param col-name:location_type
#@param expression:value.trim()
#@in table16
#@out table17
#@end core/text-transform15
#@begin core/text-transform16#@desc Text transform on cells in column currency using expression value.trim()
#@param col-name:currency
#@param expression:value.trim()
#@in table17
#@out table18
#@end core/text-transform16
#@begin core/text-transform17#@desc Text transform on cells in column currency_symbol using expression value.trim()
#@param col-name:currency_symbol
#@param expression:value.trim()
#@in table18
#@out table19
#@end core/text-transform17
#@begin core/text-transform18#@desc Text transform on cells in column status using expression value.trim()
#@param col-name:status
#@param expression:value.trim()
#@in table19
#@out table20
#@end core/text-transform18
#@begin core/text-transform19#@desc Text transform on cells in column status using expression value.trim()
#@param col-name:status
#@param expression:value.trim()
#@in table20
#@out table21
#@end core/text-transform19
#@begin core/text-transform20#@desc Text transform on cells in column page_count using expression value.trim()
#@param col-name:page_count
#@param expression:value.trim()
#@in table21
#@out table22
#@end core/text-transform20
#@begin core/text-transform21#@desc Text transform on cells in column dish_count using expression value.trim()
#@param col-name:dish_count
#@param expression:value.trim()
#@in table22
#@out table23
#@end core/text-transform21
#@begin core/text-transform22#@desc Text transform on cells in column sponsor using expression value.replace(/\\s+/,' ')
#@param col-name:sponsor
#@param expression:value.replace(/\\s+/,'_')
#@in table23
#@out table24
#@end core/text-transform22
#@begin core/text-transform23#@desc Text transform on cells in column event using expression value.replace(/\\s+/,' ')
#@param col-name:event
#@param expression:value.replace(/\\s+/,'_')
#@in table24
#@out table25
#@end core/text-transform23
#@begin core/text-transform24#@desc Text transform on cells in column venue using expression value.replace(/\\s+/,' ')
#@param col-name:venue
#@param expression:value.replace(/\\s+/,'_')
#@in table25
#@out table26
#@end core/text-transform24
#@begin core/text-transform25#@desc Text transform on cells in column place using expression value.replace(/\\s+/,' ')
#@param col-name:place
#@param expression:value.replace(/\\s+/,'_')
#@in table26
#@out table27
#@end core/text-transform25
#@begin core/text-transform26#@desc Text transform on cells in column physical_description using expression value.replace(/\\s+/,' ')
#@param col-name:physical_description
#@param expression:value.replace(/\\s+/,'_')
#@in table27
#@out table28
#@end core/text-transform26
#@begin core/text-transform27#@desc Text transform on cells in column occasion using expression value.replace(/\\s+/,' ')
#@param col-name:occasion
#@param expression:value.replace(/\\s+/,'_')
#@in table28
#@out table29
#@end core/text-transform27
#@begin core/text-transform28#@desc Text transform on cells in column physical_description using expression value.replace(/\\s+/,' ')
#@param col-name:physical_description
#@param expression:value.replace(/\\s+/,'_')
#@in table29
#@out table30
#@end core/text-transform28
#@begin core/text-transform29#@desc Text transform on cells in column occasion using expression value.replace(/\\s+/,' ')
#@param col-name:occasion
#@param expression:value.replace(/\\s+/,'_')
#@in table30
#@out table31
#@end core/text-transform29
#@begin core/text-transform30#@desc Text transform on cells in column notes using expression value.replace(/\\s+/,' ')
#@param col-name:notes
#@param expression:value.replace(/\\s+/,'_')
#@in table31
#@out table32
#@end core/text-transform30
#@begin core/text-transform31#@desc Text transform on cells in column call_number using expression value.replace(/\\s+/,' ')
#@param col-name:call_number
#@param expression:value.replace(/\\s+/,'_')
#@in table32
#@out table33
#@end core/text-transform31
#@begin core/text-transform32#@desc Text transform on cells in column notes using expression value.replace(/\\s+/,' ')
#@param col-name:notes
#@param expression:value.replace(/\\s+/,'_')
#@in table33
#@out table34
#@end core/text-transform32
#@begin core/text-transform33#@desc Text transform on cells in column keywords using expression value.replace(/\\s+/,' ')
#@param col-name:keywords
#@param expression:value.replace(/\\s+/,'_')
#@in table34
#@out table35
#@end core/text-transform33
#@begin core/text-transform34#@desc Text transform on cells in column language using expression value.replace(/\\s+/,' ')
#@param col-name:language
#@param expression:value.replace(/\\s+/,'_')
#@in table35
#@out table36
#@end core/text-transform34
#@begin core/text-transform35#@desc Text transform on cells in column date using expression value.replace(/\\s+/,' ')
#@param col-name:date
#@param expression:value.replace(/\\s+/,'_')
#@in table36
#@out table37
#@end core/text-transform35
#@begin core/text-transform36#@desc Text transform on cells in column location using expression value.replace(/\\s+/,' ')
#@param col-name:location
#@param expression:value.replace(/\\s+/,'_')
#@in table37
#@out table38
#@end core/text-transform36
#@begin core/text-transform37#@desc Text transform on cells in column location_type using expression value.replace(/\\s+/,' ')
#@param col-name:location_type
#@param expression:value.replace(/\\s+/,'_')
#@in table38
#@out table39
#@end core/text-transform37
#@begin core/text-transform38#@desc Text transform on cells in column location using expression value.replace(/\\s+/,' ')
#@param col-name:location
#@param expression:value.replace(/\\s+/,'_')
#@in table39
#@out table40
#@end core/text-transform38
#@begin core/text-transform39#@desc Text transform on cells in column currency using expression value.replace(/\\s+/,' ')
#@param col-name:currency
#@param expression:value.replace(/\\s+/,'_')
#@in table40
#@out table41
#@end core/text-transform39
#@begin core/text-transform40#@desc Text transform on cells in column currency using expression value.replace(/\\s+/,' ')
#@param col-name:currency
#@param expression:value.replace(/\\s+/,'_')
#@in table41
#@out table42
#@end core/text-transform40
#@begin core/text-transform41#@desc Text transform on cells in column currency_symbol using expression value.replace(/\\s+/,' ')
#@param col-name:currency_symbol
#@param expression:value.replace(/\\s+/,'_')
#@in table42
#@out table43
#@end core/text-transform41
#@begin core/text-transform42#@desc Text transform on cells in column status using expression value.replace(/\\s+/,' ')
#@param col-name:status
#@param expression:value.replace(/\\s+/,'_')
#@in table43
#@out table44
#@end core/text-transform42
#@begin core/text-transform43#@desc Text transform on cells in column page_count using expression value.replace(/\\s+/,' ')
#@param col-name:page_count
#@param expression:value.replace(/\\s+/,'_')
#@in table44
#@out table45
#@end core/text-transform43
#@begin core/text-transform44#@desc Text transform on cells in column dish_count using expression value.replace(/\\s+/,' ')
#@param col-name:dish_count
#@param expression:value.replace(/\\s+/,'_')
#@in table45
#@out table46
#@end core/text-transform44
#@begin core/text-transform45#@desc Text transform on cells in column id using expression value.toNumber()
#@param col-name:id
#@param expression:value.toNumber()
#@in table46
#@out table47
#@end core/text-transform45
#@begin core/text-transform46#@desc Text transform on cells in column call_number using expression value.toNumber()
#@param col-name:call_number
#@param expression:value.toNumber()
#@in table47
#@out table48
#@end core/text-transform46
#@begin core/text-transform47#@desc Text transform on cells in column date using expression value.toDate()
#@param col-name:date
#@param expression:value.toDate()
#@in table48
#@out table49
#@end core/text-transform47
#@begin core/text-transform48#@desc Text transform on cells in column page_count using expression value.toNumber()
#@param col-name:page_count
#@param expression:value.toNumber()
#@in table49
#@out table50
#@end core/text-transform48
#@begin core/text-transform49#@desc Text transform on cells in column dish_count using expression value.toNumber()
#@param col-name:dish_count
#@param expression:value.toNumber()
#@in table50
#@out table51
#@end core/text-transform49
#@begin core/text-transform50#@desc Text transform on cells in column sponsor using expression value.toLowercase()
#@param col-name:sponsor
#@param expression:value.toLowercase()
#@in table51
#@out table52
#@end core/text-transform50
#@begin core/column-removal1#@desc Remove column keywords
#@param col-name:keywords
#@in table52
#@out table53
#@end core/column-removal1
#@begin core/column-removal2#@desc Remove column language
#@param col-name:language
#@in table53
#@out table54
#@end core/column-removal2
#@begin core/column-removal3#@desc Remove column location_type
#@param col-name:location_type
#@in table54
#@out table55
#@end core/column-removal3
#@begin core/text-transform51#@desc Text transform on cells in column event using expression value.toLowercase()
#@param col-name:event
#@param expression:value.toLowercase()
#@in table55
#@out table56
#@end core/text-transform51
#@begin core/text-transform52#@desc Text transform on cells in column place using expression value.toLowercase()
#@param col-name:place
#@param expression:value.toLowercase()
#@in table56
#@out table57
#@end core/text-transform52
#@begin core/text-transform53#@desc Text transform on cells in column venue using expression value.toLowercase()
#@param col-name:venue
#@param expression:value.toLowercase()
#@in table57
#@out table58
#@end core/text-transform53
#@begin core/text-transform54#@desc Text transform on cells in column occasion using expression value.toLowercase()
#@param col-name:occasion
#@param expression:value.toLowercase()
#@in table58
#@out table59
#@end core/text-transform54
#@begin core/text-transform55#@desc Text transform on cells in column notes using expression value.toLowercase()
#@param col-name:notes
#@param expression:value.toLowercase()
#@in table59
#@out table60
#@end core/text-transform55
#@begin core/column-addition0#@desc Create column event_loop at index 3 based on column event using expression grel:value
#@param col-name:event
#@param newColumnName:"event_loop"
#@in table60
#@out table61
#@end core/column-addition0
#@begin core/mass-edit0#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table61
#@out table62
#@end core/mass-edit0
#@begin core/mass-edit1#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table62
#@out table63
#@end core/mass-edit1
#@begin core/mass-edit2#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table63
#@out table64
#@end core/mass-edit2
#@begin core/column-addition1#@desc Create column event_cluster at index 3 based on column event using expression grel:value
#@param col-name:event
#@param newColumnName:"event_cluster"
#@in table64
#@out table65
#@end core/column-addition1
#@begin core/mass-edit3#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table65
#@out table66
#@end core/mass-edit3
#@begin core/mass-edit4#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table66
#@out table67
#@end core/mass-edit4
#@begin core/mass-edit5#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table67
#@out table68
#@end core/mass-edit5
#@begin core/mass-edit6#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table68
#@out table69
#@end core/mass-edit6
#@begin core/mass-edit7#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table69
#@out table70
#@end core/mass-edit7
#@begin core/mass-edit8#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table70
#@out table71
#@end core/mass-edit8
#@begin core/mass-edit9#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table71
#@out table72
#@end core/mass-edit9
#@begin core/mass-edit10#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table72
#@out table73
#@end core/mass-edit10
#@begin core/mass-edit11#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table73
#@out table74
#@end core/mass-edit11
#@begin core/mass-edit12#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table74
#@out table75
#@end core/mass-edit12
#@begin core/mass-edit13#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table75
#@out table76
#@end core/mass-edit13
#@begin core/mass-edit14#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table76
#@out table77
#@end core/mass-edit14
#@begin core/mass-edit15#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table77
#@out table78
#@end core/mass-edit15
#@begin core/mass-edit16#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table78
#@out table79
#@end core/mass-edit16
#@begin core/mass-edit17#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table79
#@out table80
#@end core/mass-edit17
#@begin core/mass-edit18#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table80
#@out table81
#@end core/mass-edit18
#@begin core/mass-edit19#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table81
#@out table82
#@end core/mass-edit19
#@begin core/mass-edit20#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table82
#@out table83
#@end core/mass-edit20
#@begin core/mass-edit21#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table83
#@out table84
#@end core/mass-edit21
#@begin core/mass-edit22#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table84
#@out table85
#@end core/mass-edit22
#@begin core/mass-edit23#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table85
#@out table86
#@end core/mass-edit23
#@begin core/mass-edit24#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table86
#@out table87
#@end core/mass-edit24
#@begin core/mass-edit25#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table87
#@out table88
#@end core/mass-edit25
#@begin core/mass-edit26#@desc Mass edit cells in column event_loop
#@param col-name:event_loop
#@in table88
#@out table89
#@end core/mass-edit26
#@begin core/column-removal4#@desc Remove column event_cluster
#@param col-name:event_cluster
#@in table89
#@out table90
#@end core/column-removal4
#@begin core/column-rename0#@desc Rename column event_loop to event_cluster
#@param oldColumnName:event_loop
#@param newColumnName:event_cluster
#@in table90
#@out table91
#@end core/column-rename0
#@begin core/text-transform56#@desc Text transform on cells in column date using expression grel:toString(toDate(value),\"yyyy-MM-dd\")
#@param col-name:date
#@param expression:grel:toString(toDate(value),"yyyy-MM-dd")
#@in table91
#@out table92
#@end core/text-transform56
#@begin core/column-addition2#@desc Create column sponsor_grel at index 2 based on column sponsor using expression grel:value
#@param col-name:sponsor
#@param newColumnName:"sponsor_grel"
#@in table92
#@out table93
#@end core/column-addition2
#@begin core/mass-edit27#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table93
#@out table94
#@end core/mass-edit27
#@begin core/mass-edit28#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table94
#@out table95
#@end core/mass-edit28
#@begin core/mass-edit29#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table95
#@out table96
#@end core/mass-edit29
#@begin core/mass-edit30#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table96
#@out table97
#@end core/mass-edit30
#@begin core/mass-edit31#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table97
#@out table98
#@end core/mass-edit31
#@begin core/mass-edit32#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table98
#@out table99
#@end core/mass-edit32
#@begin core/mass-edit33#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table99
#@out table100
#@end core/mass-edit33
#@begin core/mass-edit34#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table100
#@out table101
#@end core/mass-edit34
#@begin core/mass-edit35#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table101
#@out table102
#@end core/mass-edit35
#@begin core/mass-edit36#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table102
#@out table103
#@end core/mass-edit36
#@begin core/mass-edit37#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table103
#@out table104
#@end core/mass-edit37
#@begin core/mass-edit38#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table104
#@out table105
#@end core/mass-edit38
#@begin core/mass-edit39#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table105
#@out table106
#@end core/mass-edit39
#@begin core/mass-edit40#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table106
#@out table107
#@end core/mass-edit40
#@begin core/mass-edit41#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table107
#@out table108
#@end core/mass-edit41
#@begin core/mass-edit42#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table108
#@out table109
#@end core/mass-edit42
#@begin core/mass-edit43#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table109
#@out table110
#@end core/mass-edit43
#@begin core/mass-edit44#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table110
#@out table111
#@end core/mass-edit44
#@begin core/mass-edit45#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table111
#@out table112
#@end core/mass-edit45
#@begin core/mass-edit46#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table112
#@out table113
#@end core/mass-edit46
#@begin core/mass-edit47#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table113
#@out table114
#@end core/mass-edit47
#@begin core/mass-edit48#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table114
#@out table115
#@end core/mass-edit48
#@begin core/mass-edit49#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table115
#@out table116
#@end core/mass-edit49
#@begin core/mass-edit50#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table116
#@out table117
#@end core/mass-edit50
#@begin core/mass-edit51#@desc Mass edit cells in column sponsor_grel
#@param col-name:sponsor_grel
#@in table117
#@out table118
#@end core/mass-edit51
#@begin core/column-rename1#@desc Rename column sponsor_grel to sponsor_cluster
#@param oldColumnName:sponsor_grel
#@param newColumnName:sponsor_cluster
#@in table118
#@out table119
#@end core/column-rename1
#@begin core/column-addition3#@desc Create column venue_cluster at index 6 based on column venue using expression grel:value
#@param col-name:venue
#@param newColumnName:"venue_cluster"
#@in table119
#@out table120
#@end core/column-addition3
#@begin core/mass-edit52#@desc Mass edit cells in column venue_cluster
#@param col-name:venue_cluster
#@in table120
#@out table121
#@end core/mass-edit52
#@begin core/mass-edit53#@desc Mass edit cells in column venue_cluster
#@param col-name:venue_cluster
#@in table121
#@out table122
#@end core/mass-edit53
#@begin core/mass-edit54#@desc Mass edit cells in column venue_cluster
#@param col-name:venue_cluster
#@in table122
#@out table123
#@end core/mass-edit54
#@begin core/mass-edit55#@desc Mass edit cells in column venue_cluster
#@param col-name:venue_cluster
#@in table123
#@out table124
#@end core/mass-edit55
#@begin core/mass-edit56#@desc Mass edit cells in column venue_cluster
#@param col-name:venue_cluster
#@in table124
#@out table125
#@end core/mass-edit56
#@begin core/mass-edit57#@desc Mass edit cells in column venue_cluster
#@param col-name:venue_cluster
#@in table125
#@out table126
#@end core/mass-edit57
#@begin core/column-addition4#@desc Create column place_cluster at index 8 based on column place using expression grel:value
#@param col-name:place
#@param newColumnName:"place_cluster"
#@in table126
#@out table127
#@end core/column-addition4
#@begin core/mass-edit58#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table127
#@out table128
#@end core/mass-edit58
#@begin core/mass-edit59#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table128
#@out table129
#@end core/mass-edit59
#@begin core/mass-edit60#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table129
#@out table130
#@end core/mass-edit60
#@begin core/mass-edit61#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table130
#@out table131
#@end core/mass-edit61
#@begin core/mass-edit62#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table131
#@out table132
#@end core/mass-edit62
#@begin core/mass-edit63#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table132
#@out table133
#@end core/mass-edit63
#@begin core/mass-edit64#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table133
#@out table134
#@end core/mass-edit64
#@begin core/mass-edit65#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table134
#@out table135
#@end core/mass-edit65
#@begin core/mass-edit66#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table135
#@out table136
#@end core/mass-edit66
#@begin core/mass-edit67#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table136
#@out table137
#@end core/mass-edit67
#@begin core/mass-edit68#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table137
#@out table138
#@end core/mass-edit68
#@begin core/mass-edit69#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table138
#@out table139
#@end core/mass-edit69
#@begin core/mass-edit70#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table139
#@out table140
#@end core/mass-edit70
#@begin core/mass-edit71#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table140
#@out table141
#@end core/mass-edit71
#@begin core/mass-edit72#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table141
#@out table142
#@end core/mass-edit72
#@begin core/mass-edit73#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table142
#@out table143
#@end core/mass-edit73
#@begin core/mass-edit74#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table143
#@out table144
#@end core/mass-edit74
#@begin core/mass-edit75#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table144
#@out table145
#@end core/mass-edit75
#@begin core/mass-edit76#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table145
#@out table146
#@end core/mass-edit76
#@begin core/mass-edit77#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table146
#@out table147
#@end core/mass-edit77
#@begin core/mass-edit78#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table147
#@out table148
#@end core/mass-edit78
#@begin core/mass-edit79#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table148
#@out table149
#@end core/mass-edit79
#@begin core/mass-edit80#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table149
#@out table150
#@end core/mass-edit80
#@begin core/mass-edit81#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table150
#@out table151
#@end core/mass-edit81
#@begin core/mass-edit82#@desc Mass edit cells in column place_cluster
#@param col-name:place_cluster
#@in table151
#@out table152
#@end core/mass-edit82
#@begin core/mass-edit83#@desc Mass edit cells in column venue_cluster
#@param col-name:venue_cluster
#@in table152
#@out table153
#@end core/mass-edit83
#@begin core/mass-edit84#@desc Mass edit cells in column venue_cluster
#@param col-name:venue_cluster
#@in table153
#@out table154
#@end core/mass-edit84
#@begin core/mass-edit85#@desc Mass edit cells in column currency_symbol
#@param col-name:currency_symbol
#@in table154
#@out table155
#@end core/mass-edit85
#@begin core/column-addition5#@desc Create column location_cluster at index 15 based on column location using expression grel:value
#@param col-name:location
#@param newColumnName:"location_cluster"
#@in table155
#@out table156
#@end core/column-addition5
#@begin core/column-removal5#@desc Remove column location
#@param col-name:location
#@in table156
#@out table157
#@end core/column-removal5
#@begin core/column-removal6#@desc Remove column location_cluster
#@param col-name:location_cluster
#@in table157
#@out table158
#@end core/column-removal6
#@begin core/column-addition6#@desc Create column occasion_cluster at index 11 based on column occasion using expression grel:value
#@param col-name:occasion
#@param newColumnName:"occasion_cluster"
#@in table158
#@out table159
#@end core/column-addition6
#@begin core/mass-edit86#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table159
#@out table160
#@end core/mass-edit86
#@begin core/mass-edit87#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table160
#@out table161
#@end core/mass-edit87
#@begin core/mass-edit88#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table161
#@out table162
#@end core/mass-edit88
#@begin core/mass-edit89#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table162
#@out table163
#@end core/mass-edit89
#@begin core/mass-edit90#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table163
#@out table164
#@end core/mass-edit90
#@begin core/mass-edit91#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table164
#@out table165
#@end core/mass-edit91
#@begin core/mass-edit92#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table165
#@out table166
#@end core/mass-edit92
#@begin core/mass-edit93#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table166
#@out table167
#@end core/mass-edit93
#@begin core/mass-edit94#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table167
#@out table168
#@end core/mass-edit94
#@begin core/text-transform57#@desc Text transform on cells in column occasion_cluster using expression grel:value.replace(\";\", \"\")
#@param col-name:occasion_cluster
#@param expression:grel:value.replace(";",_"")
#@in table168
#@out table169
#@end core/text-transform57
#@begin core/text-transform58#@desc Text transform on cells in column occasion_cluster using expression grel:value.replace(\"\"\", \"\")
#@param col-name:occasion_cluster
#@param expression:grel:value.replace(""",_"")
#@in table169
#@out table170
#@end core/text-transform58
#@begin core/mass-edit95#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table170
#@out table171
#@end core/mass-edit95
#@begin core/mass-edit96#@desc Mass edit cells in column occasion_cluster
#@param col-name:occasion_cluster
#@in table171
#@out table172
#@end core/mass-edit96
#@begin core/text-transform59#@desc Text transform on cells in column occasion_cluster using expression grel:value.replace(\"[\",\"\")
#@param col-name:occasion_cluster
#@param expression:grel:value.replace("[","")
#@in table172
#@out table173
#@end core/text-transform59
#@begin core/text-transform60#@desc Text transform on cells in column occasion_cluster using expression grel:value.replace(\"]\",\"\")
#@param col-name:occasion_cluster
#@param expression:grel:value.replace("]","")
#@in table173
#@out table174
#@end core/text-transform60
#@begin core/text-transform61#@desc Text transform on cells in column occasion_cluster using expression grel:value.replace(\"(\",\"\")
#@param col-name:occasion_cluster
#@param expression:grel:value.replace("(","")
#@in table174
#@out table175
#@end core/text-transform61
#@begin core/text-transform62#@desc Text transform on cells in column occasion_cluster using expression grel:value.replace(\")\",\"\")
#@param col-name:occasion_cluster
#@param expression:grel:value.replace(")","")
#@in table175
#@out table176
#@end core/text-transform62
#@begin core/text-transform63#@desc Text transform on cells in column occasion_cluster using expression grel:value.replace(\"?\",\"\")
#@param col-name:occasion_cluster
#@param expression:grel:value.replace("?","")
#@in table176
#@out Menu_clean
#@end core/text-transform63
#@end Menu.csv
