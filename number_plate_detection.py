import pandas as pd
col=['License-plate-no', 'Owner name','phone number:', 'Vehicle model:', 'License-issued-date:','FIR:']
database=pd.DataFrame(columns=col)
database['License-plate-no']=['HR26DA2330', 'CG04MF2250', 'HR26DK8337', 'TN31AP1243', 'TN01AV0001', 'KL01AQ1424', 'PY01AA0090' , 'TN01BC1010', 'TN081BE3389', 'TN87CA8790', 'KL45BC5542', 'TN91PA2341', 'HR01CD542', 'TN5AL8768', 'UP14BN4001']
database['Owner name']=['vijay kummar', 'Rnajith','Anu', 'Archana','Salmon', 'Vinai','Samson', 'Gokul', 'Vinayak', 'Dhana', 'Sekhar', 'Raj', 'Gaajapathii', 'Vimal', 'shanmugam']
database['phone number:']=['8134896473', '7612376521', '9123349879', '9841376897', '8532253819', '6382291009', '8182638101', '8898897898', '6789067543', '6876789765', '9867132561', '6273819263' ,'9762912839', '6789896504', '6787654329']
database['Vehicle model:']=['Maruthi Suzuki -shift dzire', 'Audi-Q8', 'Hyundai-ksg', 'Indica-LGI', 'Altoz', 'Indica-DLe', 'Mahindra-xuv500', 'Mahindra-scorpio', 'ford-echosport', 'Reynold-duster', 'Skoda-rapid', 'Skoda-superb', 'Skoda-activia', 'Volkswagen-polo', 'Ford-aspire',]
database['License-issued-date:']=['01-10-2002', '06-12-2001', '05-11-2009', '21-12-1990', '18-01-2020', '10-06-2006', '04-02-2019', '15-12-1998', '09-07-2005', '11-10-2004', '03-11-1989', '23-06-2002', '21-7-2003', '11-01-2005', '22-11-2008']
database['FIR:']=['NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'YES', 'NO', 'YES', 'NO' ,'YES']    
index=pd.Index(['HR26DA2330'])
k=index.get_loc('HR26DA2330')
lst=database.loc[k,:]
print(lst)
