#@begin CleanMenuPage
#@desc or2yw conversion
#@param col-name:uuid
#@param col-name:id
#@param col-name:menu_id
#@param expression:value.trim()
#@param col-name:page_number
#@param col-name:image_id
#@param expression:value.toNumber()
#@param expression:value.replace(/\\s+/,'_')
#@param col-name:full_width
#@param col-name:full_height
#@in MenuPage @URI file:../raw_data/MenuPage.csv.gz
#@out MenuPage_clean @URI file:../01_openrefine/MenuPage_clean.csv.gz
#@begin core/text-transform0#@desc Text transform on cells in column id using expression value.toNumber()
#@param col-name:id
#@param expression:value.toNumber()
#@in table0
#@out table1
#@end core/text-transform0
#@begin core/text-transform1#@desc Text transform on cells in column menu_id using expression value.toNumber()
#@param col-name:menu_id
#@param expression:value.toNumber()
#@in table1
#@out table2
#@end core/text-transform1
#@begin core/text-transform2#@desc Text transform on cells in column page_number using expression value.toNumber()
#@param col-name:page_number
#@param expression:value.toNumber()
#@in table2
#@out table3
#@end core/text-transform2
#@begin core/text-transform3#@desc Text transform on cells in column image_id using expression value.toNumber()
#@param col-name:image_id
#@param expression:value.toNumber()
#@in table3
#@out table4
#@end core/text-transform3
#@begin core/text-transform4#@desc Text transform on cells in column full_height using expression value.toNumber()
#@param col-name:full_height
#@param expression:value.toNumber()
#@in table4
#@out table5
#@end core/text-transform4
#@begin core/text-transform5#@desc Text transform on cells in column full_width using expression value.toNumber()
#@param col-name:full_width
#@param expression:value.toNumber()
#@in table5
#@out table6
#@end core/text-transform5
#@begin core/text-transform6#@desc Text transform on cells in column uuid using expression value.trim()
#@param col-name:uuid
#@param expression:value.trim()
#@in table6
#@out table7
#@end core/text-transform6
#@begin core/text-transform7#@desc Text transform on cells in column uuid using expression value.replace(/\\s+/,' ')
#@param col-name:uuid
#@param expression:value.replace(/\\s+/,'_')
#@in table7
#@out table8
#@end core/text-transform7
#@begin core/text-transform8#@desc Text transform on cells in column full_width using expression value.trim()
#@param col-name:full_width
#@param expression:value.trim()
#@in table8
#@out table9
#@end core/text-transform8
#@begin core/text-transform9#@desc Text transform on cells in column full_height using expression value.trim()
#@param col-name:full_height
#@param expression:value.trim()
#@in table9
#@out table10
#@end core/text-transform9
#@begin core/text-transform10#@desc Text transform on cells in column image_id using expression value.trim()
#@param col-name:image_id
#@param expression:value.trim()
#@in table10
#@out table11
#@end core/text-transform10
#@begin core/text-transform11#@desc Text transform on cells in column page_number using expression value.trim()
#@param col-name:page_number
#@param expression:value.trim()
#@in table11
#@out table12
#@end core/text-transform11
#@begin core/text-transform12#@desc Text transform on cells in column menu_id using expression value.trim()
#@param col-name:menu_id
#@param expression:value.trim()
#@in table12
#@out table13
#@end core/text-transform12
#@begin core/text-transform13#@desc Text transform on cells in column id using expression value.trim()
#@param col-name:id
#@param expression:value.trim()
#@in table13
#@out MenuPage_clean
#@end core/text-transform13
#@end CleanMenuPage
