#include <bits/stdc++.h>
using namespace std;

using T=int;
using D=double;
map<pair<T,T>,T> m;
D dist(D a,D b,D c,D d)
{
  return sqrt((a-c)*(a-c)+(b-d)*(b-d));
}

bool same_line(const vector<T>& v,pair<T,T> p)
{
  D x1,x2,y1,y2;
  x1=v[0];
  y1=v[1];
  x2=v[2];
  y2=v[3];
  D tot=dist(x1,y1,p.first,p.second)+dist(x2,y2,p.first,p.second);
  return fabs(tot-dist(x1,y1,x2,y2))<=1e-6;
}

int main()
{
  T n=500;
  vector<vector<T>> v(n);
  for(int i=0;i<n;++i)
  {
    // cout<<"here on: "<<i<<"\n";
    T a,b,c,d;
    cin>>a>>b>>c>>d;
    v[i].push_back(a);
    v[i].push_back(b);
    v[i].push_back(c);
    v[i].push_back(d);
  }
  T count=0;
  for(int i=0;i<=1000;++i)
  {
    for(int j=0;j<=1000;++j)
    {
      for(int k=0;k<n;++k)
      {
        //uncomment these lines for the first part
        
        // if(!((v[k][0]==v[k][2]) || (v[k][1]==v[k][3])))
        //   continue;
        if(same_line(v[k],make_pair(i,j)))
        {
          auto val=make_pair(i,j);
          m[val]++;
          if(m[val]==2)
          {
            ++count;
          }
        }
      }
    }
  }
  cout<<"count: "<<count<<"\n";

}
