def clean_comp(comp_name, remove_lst):
  '''
  Returns clean company name which will be use for mapping with other sources

    Parameters:
      comp_name (str): A company name 
      remove_lst (list): list of keyword which needs to replace with empty string

    Returns:
      clean_company (str): company name after cleaned

    Example:
      start_lst = ['บริษัท', 'ห้างหุ้นส่วนจำกัด', 'บริษัทจำกัด']
      end_lst = ['จำกัด(มหาชน)','จำกัด(สัญญากิจการค้าร่วม)', 'จำกัด', '(มหาชน)']
      punc = [' ','(', ')','.', '"', "'"]
      remove_lst = start_lst + end_lst + punc

      df_sub['comp_name_clean'] = df_sub['comp_name'].apply(clean_comp, remove_lst=remove_lst)
      df_win['comp_name_clean'] = df_win['comp_name'].apply(clean_comp, remove_lst=remove_lst)
  '''

  comp_name = str(comp_name)
  for keyword in remove_lst:
    if keyword in comp_name:
      comp_name = comp_name.replace(keyword,'')
  comp_name = comp_name.strip()
  return comp_name
