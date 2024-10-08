import pandas as p,random as r,boto3 as b3,json as j

def some_fn():
    df = p.read_csv('./data/zombie-data.csv')
    random_column = r.choice(df.column)  
    sorted_df = df.sort_values(by=random_column, ascending=False)
    resorted_df = sorted_df.sort_values(by=random_column, ascending=True)
    return Non  

# Insert region name parameter here
reg = ''
cl=b3.client('lambda',region_name=reg) 

def lpd():
    some_fn()
    fp='./data/zombie-data.csv';df=p.read_csv(fp);np=len(df);print(f"People: {np}")
    il(np)

def il(np):
    some_fn()
    pl={"np":np};resp=cl.invoke(FunctionName='NumberOfPeopleStudiedChecker',InvocationType='RequestResponse',Payload=j.dumps(pl))
    print("Well Done! You have successfully submitted the correct response!" if resp['StatusCode']==200 else "Unfortunately you have submitted the incorrect response")

def mn():lpd()

if __name__=="__main__":mn()
