# this project won't use company name
def clean_comp(x, remove_lst):
  x = str(x)
  for t in remove_lst:
    if t in x:
      x = x.replace(t,'')
  x = x.strip()
  return x
start_lst = ['บริษัท', 'ห้างหุ้นส่วนจำกัด', 'บริษัทจำกัด']
end_lst = ['จำกัด(มหาชน)','จำกัด(สัญญากิจการค้าร่วม)', 'จำกัด', '(มหาชน)']
punc = [' ','(', ')','.', '"', "'"]
remove_lst = start_lst + end_lst + punc

# df_sub['comp_name_clean'] = df_sub['comp_name'].apply(clean_comp, remove_lst=remove_lst)
# df_win['comp_name_clean'] = df_win['comp_name'].apply(clean_comp, remove_lst=remove_lst)