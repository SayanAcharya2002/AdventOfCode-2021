// #include <bits/stdc++.h>
#include <map>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <set>
#include <regex>
#include <fstream>


//ignore the comments, a lot of logging is there. Took me a long time to debug this monster. Though i optimized as much as i could, still it takes mammoth amount of time to run.
//Dont know what i could do better. Feel free to let me know.


using namespace std;

bool is_overlapping(int x1,int x2,int x3,int x4)
{
  if(x1>x2 || x3>x4)
  {
    return false;
  }
  vector<int64_t> v={x1,x2,x3,x4};
  sort(v.begin(),v.end());
  auto full_length=abs(v.back()-v[0])+1;
  auto first_length=abs(x2-x1)+1;
  auto second_length=abs(x3-x4)+1;
  if( first_length+second_length>full_length)
  {
    return true;
  }
  else
  {
    return false;
  }
}

struct stuff{
  bool messed=0;
  vector<pair<int,int>> pat,protrude,both,original;
  void print_vector(string s,const vector<pair<int,int>>& v)const
  {
    cout<<s<<": ";
    for(auto& x:v)
    {
      cout<<x.first<<" "<<x.second<<',';
    }
    cout<<"\n";
  }
  void print_data()const
  {
    print_vector("pat",pat);
    print_vector("protrude",protrude);
    print_vector("both",both);
    print_vector("original",original);
  }
};

stuff split_ranges(int patx1,int patx2,int x1,int x2)
{
  if(!is_overlapping(patx1,patx2,x1,x2)) 
  {
    //return something invalid
    stuff ans;
    ans.messed=1;
    return ans;
  }
  vector<int> v={patx1,patx2,x1,x2};
  sort(v.begin(),v.end());
  // v.erase(v.begin(),unique(v.begin(),v.end()));

  vector<pair<int,int>> ranges;
  for(int i=0;i<(int)v.size()-1;++i)
  {
    ranges.push_back(make_pair(v[i],v[i+1]));
  }
  ranges[0].second-=1;
  ranges.back().first+=1;

  stuff ans;
  for(auto& t:ranges)
  {
    bool pat_overlap=is_overlapping(patx1,patx2,t.first,t.second);
    bool ori_overlap=is_overlapping(x1,x2,t.first,t.second);

    if(pat_overlap && ori_overlap)
    {
      ans.both.push_back(t);
      ans.original.push_back(t);
    }
    else
    {
      if(pat_overlap)
      {
        if(t.second==v.back())
        {
          ans.protrude.push_back(t);
        }
        else
        {
          ans.pat.push_back(t);
        }
      }
      else if(ori_overlap)
      {
        ans.original.push_back(t);
      }
    }
  }

  return ans;
}

template<class T>
vector<T> vector_slice(vector<T> v,int a,int b=-1)
{
  vector<T> ans;
  if(b==-1)
  {
    b=v.size()-1;
  }
  for(int i=a;i<=b;++i)
  {
    ans.push_back(v[i]);
  }
  return ans;
}

void func(int& mappa,vector<pair<int,int>> v,int on, int depth)
{
  if(!mappa)
    mappa=1+on;
}

template<class T>
void func(T& mappa,vector<pair<int,int>> v,int on,int depth)
{
  // if(depth==3)//check value here
  // {
  //   *(bool*)(&mappa)=on;
  //   return;
  // }
  bool anything_to_do=true;
  auto value=v[0];
  // cout<<"came"<<"\n";
  // auto it=mappa.lower_bound(value);
  // if(it!=mappa.begin())
  // {
  //   it--;
  // }
  auto it=mappa.begin();
  T add_mappa;
  set<pair<int,int>> delete_mappa;
  while(it!=mappa.end() && value.second>=it->first.first)//check this stuff
  {
    // cout<<it->first.first<<" "<<it->first.second<<"\n";
    // cout<<"here1"<<"\n";
    stuff stuff_ans=split_ranges(value.first,value.second,it->first.first,
    it->first.second);
    if(stuff_ans.messed)
    {
      ++it;
      continue;
    }
    // stuff_ans.print_data();
    for(auto& t:stuff_ans.original)
    {
      add_mappa[t]=it->second;//setting it equal to current content
      delete_mappa.insert(it->first);
    }
    for(auto& t:stuff_ans.pat)
    {
      add_mappa[t];
      func(add_mappa[t],vector_slice(v,1),on,depth+1);
    }
    for(auto& t:stuff_ans.both)
    {
      func(add_mappa[t],vector_slice(v,1),on,depth+1);
    }

    if(stuff_ans.protrude.size())
    {
      value=stuff_ans.protrude[0];
    }
    else
    {
      anything_to_do=false;
    }
    it++;
  }
  if(anything_to_do)
  {
    add_mappa[value];
    func(add_mappa[value],vector_slice(v,1),on,depth+1);
  }

  //cleaning the map
  for(auto& t:delete_mappa)
  {
    mappa.erase(t);
  }
  for(auto& t:add_mappa)
  {
    mappa[t.first]=t.second;
  }
}
template<class T>
int64_t count_total(T mappa)
{
  int64_t total=0;
  for(auto& p_x:mappa)
  {
    int64_t x_val=p_x.first.second-p_x.first.first+1;
    for(auto& p_y:p_x.second)
    {
      int64_t y_val=p_y.first.second-p_y.first.first+1;
      for(auto& p_z:p_y.second)
      {
        int64_t z_val=p_z.first.second-p_z.first.first+1;
        // cout<<x_val<<" "<<y_val<<" "<<z_val<<"\n";
        if(p_z.second==0)
        {
          continue;
        }
        // cout<<x_val<<" "<<y_val<<" "<<z_val<<"\n";
        total+=(int64_t)x_val*(int64_t)y_val*(int64_t)z_val*(int64_t)(p_z.second-1);
      }
    }
  }
  return total;
}


auto reg_parse(string s)
{
  bool on;
  if(s[1]=='n')
  {
    on=true;
  }
  else
  {
    on=false;
  }
  s=s.substr(3+!on,(int)s.size()-(3+!on));
  // cout<<s<<"\n";
  auto split=[](string t)->vector<string>{
    vector<string> ans;
    vector<int> cut_pos;
    cut_pos.push_back(-1);
    for(int i=0;i<t.size();++i)
    {
      // cout<<t[i];
      if(t[i]==',')
      {
        // cout<<"here"<<"\n";
        cut_pos.push_back(i);
      }
    }
    cut_pos.push_back(t.size());
    for(int i=0;i<cut_pos.size()-1;++i)
    {
      ans.push_back(t.substr(cut_pos[i]+1,cut_pos[i+1]-cut_pos[i]-1));
    }
    return ans;
  };
  vector<string> split_strings=split(s);
  // for(auto& t:split_strings)
  // {
  //   cout<<t<<"\n";
  // }
  // static const regex pat(R"regex([x,y,z]=([+-]?\d+)\.+([+-]?\d+))regex");
  static const regex pat(R"regex([xyz]=([+-]?\d+)\.+([+-]?\d+))regex");
  // static const regex pat("[xyz]=([+-]?\\d+)\\.+([+-]?\\d+)");

  vector<pair<int,int>> ans;
  for(auto& t:split_strings)
  {
    // cout<<t<<"\n";
    smatch m;
    if(!regex_match(t,m,pat))
    {
      cerr<<"malformatted data"<<"\n";
      throw exception();
    }
    ans.push_back(make_pair(stoi(m[1]),stoi(m[2])));
  }
  return make_pair(on,ans);
}

bool validate(vector<pair<int,int>> v)
{
  for(auto& t:v)
  {
    if(t.first>t.second)
    {
      return false;
    }
  }
  return true;
}


int main(int argc,char** argv)
{
  typedef pair<int,int> pii;

  int l_bound=-50;
  int u_bound=50;
  map<pii,map<pii,map<pii,int>>> mappa;

  ifstream fin(argv[1],ios_base::in);
  vector<pair<bool,vector<pair<int,int>>>> val_vec;
  while(!fin.eof())
  {
    string s;
    getline(fin,s);
    // fin.ignore(0);
    // cout<<s<<"\n";
    auto val=reg_parse(s);
    // cout<<"size: "<<val.second.size()<<"\n";
    for(auto& t:val.second)
    {
      // t.first=max(t.first,l_bound);
      // t.second=min(t.second,u_bound);
      // cout<<t.first<<" "<<t.second<<"\n";
    }
    val_vec.push_back(val);
    // func(mappa,val.second,val.first,0);
  }
  // int LEN=101;
  // vector<vector<vector<int>>> v(LEN,vector<vector<int>>(LEN,vector<int>(LEN,0)));
  // for(auto& t:val_vec)
  // {
  //   for(int i=t.second[0].first+50;i<=t.second[0].second+50;++i)
  //   {
  //     for(int j=t.second[1].first+50;j<=t.second[1].second+50;++j)
  //     {
  //       for(int k=t.second[2].first+50;k<=t.second[2].second+50;++k)
  //       {
  //         v[i][j][k]=t.first;
  //       }
  //     }
  //   }
  // }
  // int total=0;
  // for(int i=0;i<LEN;++i)
  // {
  //   for(int j=0;j<LEN;++j)
  //   {
  //     for(int k=0;k<LEN;++k)
  //     {
  //       total+=v[i][j][k];
  //     }
  //   }
  // }
  // cout<<total<<"\n";

  reverse(val_vec.begin(),val_vec.end());
  int index=0;
  for(auto& val:val_vec)
  {
    cout<<"indexing: "<<index<<"\n";
    index++;
    if(validate(val.second))
      func(mappa,val.second,val.first,0);
    cout<<"counting: "<<count_total(mappa)<<"\n";
  }
  
}

