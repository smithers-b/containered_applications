import pandas as pd

def main():
    df = pd.read_csv('aws_elasticloadbalancing.log') 
    df = df.rename(columns={df.columns[0]: 'column1'}) 
    df = df.column1.str.split(pat=' ',expand=True)
    df = df.rename(columns={df.columns[17]: 'platform'})
    df = df.rename(columns={df.columns[3]: 'ipport'})
    df = df.loc[df['platform'] == '(PlayStation']
    ips = df.ipport.str.split(pat= ':', expand=True)
    df = ips.mode()
    df = df.iloc[[0]]
    df = df.rename(columns={df.columns[0]: 'Public Ip'})
    df = df.rename(columns={df.columns[1]: 'Count'})
    df = df.rename(index={0: 'Most Requests'})
    print(df)


main() 