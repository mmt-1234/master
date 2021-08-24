using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace Mmt{
  class MainClass {
    public static void Main (string[] args) {
      System.Diagnostics.Stopwatch sw = new Stopwatch();
      sw.Reset();         // 초기화
      sw.Start();
      Sudoku sdk = new Sudoku();
      //int[] a = new int[]{1,2,3,4,5,6,7,8,9};
      sdk.Startup();
      sw.Stop();
      Console.WriteLine("수행 시간 : {0}", sw.ElapsedMilliseconds / 1000.0F);
    }
  } 
  class Sudoku{
    public Sudoku(){
      
    }
    private Control block1= new Control(1);
    private Control block2= new Control(2);
    private Control block3= new Control(3);
    private Control block4= new Control(4);
    private Control block5= new Control(5);
    private Control block6= new Control(6);
    private Control block7= new Control(7);
    private Control block8= new Control(8);
    private Control block9= new Control(9);
    public int[,] mainArr= new int[9,9];
    public void Startup(){
      List<int> numArr= new List<int>(new int[]{1,2,3,4,5,6,7,8,9});
      Shuffle(numArr);
      for(int t=0; t<3; t++){
        for(int f=0; f<3; f++){
          for(int s=0; s<3; s++){
            if(t==0){
              mainArr[f,s]= numArr[f*3+s];
              blockPlus(numArr[f*3+s], f+1,s+1,1);
            }
            else if(t==1){
              mainArr[f+3,s+3]=numArr[f*3+s];
              blockPlus(numArr[f*3+s], f+4,s+4,5);
            }
            else{
              mainArr[f+6,s+6]=numArr[f*3+s];
              blockPlus(numArr[f*3+s], f+7,s+7,9);
            }
          }
        }
        Shuffle(numArr);
      }
      mainArr=block1.input(mainArr);
      mainArr=block2.input(mainArr);
      mainArr=block3.input(mainArr);
      mainArr=block4.input(mainArr);
      mainArr=block5.input(mainArr);
      mainArr=block6.input(mainArr);
      mainArr=block7.input(mainArr);
      mainArr=block8.input(mainArr);
      mainArr=block9.input(mainArr);
      PrintAll(mainArr);
    }

    public void blockPlus(int n,int r, int c, int b){
      switch(n){
        case 1:
          block1.p_r(r);
          block1.p_c(c);
          block1.p_b(b);
          break;
        case 2:
          block2.p_r(r);
          block2.p_c(c);
          block2.p_b(b);
          break;
        case 3:
          block3.p_r(r);
          block3.p_c(c);
          block3.p_b(b);
          break;
        case 4:
          block4.p_r(r);
          block4.p_c(c);
          block4.p_b(b);
          break;
        case 5:
          block5.p_r(r);
          block5.p_c(c);
          block5.p_b(b);
          break;
        case 6:
          block6.p_r(r);
          block6.p_c(c);
          block6.p_b(b);
          break;
        case 7:
          block7.p_r(r);
          block7.p_c(c);
          block7.p_b(b);
          break;
        case 8:
          block8.p_r(r);
          block8.p_c(c);
          block8.p_b(b);
          break;
        case 9:
          block9.p_r(r);
          block9.p_c(c);
          block9.p_b(b);
          break;
      }
      
      }

    //shuffle list
    public List<T> Shuffle<T>  (List<T> list)
    {
      Random rnd = new Random();
      for (int i = 0; i < list.Count; i++)
      {
          int k = rnd.Next(0, i);
          T value = list[k];
          list[k] = list[i];
          list[i] = value;
      }
      return list;
    }
    

    //print array
    public void PrintAll(List<int> list){
    foreach(int l in list){
          Console.Write(l+" ");
        }
        Console.WriteLine("\n");
    }
    
    public void PrintAll(int[] oda){
    try{
      foreach(int o in oda){
          Console.Write(o+" ");
        }
        Console.WriteLine();
    }catch(Exception e){
      Console.WriteLine("error is {0}",e);
    }
    }

    public void PrintAll(int[,] tda){
      int c=0;
      try{
      foreach(int t in tda){
        Console.Write(t+" ");
        c++;
        if(c%9==0){
          Console.WriteLine();
        }
      }
      }catch(Exception e){
      Console.WriteLine("error is {0}",e);
    }
    }

}

  class Control{
    public Control(int _number){
      number=_number;
    }

    public void p_r(int ro){
      row.Add(ro);
    }

    public void p_c(int co){
      col.Add(co);
    }
    
    public void p_b(int bo){
      box.Add(bo);
    }
    private List<int> row = new List<int>();
    private List<int> col = new List<int>();
    private List<int> box = new List<int>();
    public int number;
    public int[,] input(int[,] mainarr){
      Sudoku sudo = new Sudoku();
      int[,] mainarray = new int[9,9];
      mainarray=mainarr;
      List<int> array= new List<int>(new int[]{1,2,3,4,5,6,7,8,9});
      List<int> R,C,B= new List<int>();
      List<int> n_r = new List<int>();
      List<int> n_c = new List<int>();
      R=array;
      R=remove(R,row);
      C=array;
      C=remove(C,col);
      B=array;
      B=remove(B,box);
      sudo.Shuffle(R);
      sudo.Shuffle(C);
      sudo.PrintAll(mainarray);
      for(int x=0; x<B.Count; x++){
        List<int> r= new List<int>(R);
        List<int> c= new List<int>(C);
        //REVIEW 행 구하기
        double trun=B[x]/3;
        if(System.Math.Truncate(trun)==0){//first row
          r.RemoveAll(item=>item>3);
        }
        else if(System.Math.Truncate(trun)==1){//second row
          r.RemoveAll(item => item>6||item<4);
        }
        else{//third row
          r.RemoveAll(item => item<7);
        }
        //REVIEW 열 구하기
        if(B[x]%3==1){//first column
          c.RemoveAll(item=>item>3);
        }
        else if(B[x]%3==2){//second column
          c.RemoveAll(item => item>6||item<4);
        }
        else{//third column
          c.RemoveAll(item => item<7);
        }
        Sub:
        Console.WriteLine("mainarray[{0},{1}]={2}",r[0],c[0],mainarray[r[0]-1,c[0]-1]);
        try{
        if(mainarray[r[0]-1,c[0]-1]==0){
          mainarray[r[0]-1,c[0]-1]=number;
          continue;
        }
        else{
        sudo.Shuffle(r);
        sudo.Shuffle(c);
        goto Sub;
        }
        }catch(Exception e){
          sudo.PrintAll(mainarray);
          Console.WriteLine("Error:{0}",e.Message);
        }
      }
      return mainarray;
    }
    
    public static List<T> remove<T>(List<T> list, List<T> rem){
      List<T> lists = new List<T>(list);
      List<T> removing = new List<T>(rem);
      foreach(var i in removing){
        if(list.Contains(i)==true){
          lists.Remove(i);
        }
      }
      return lists;
    }
    
  }
}
