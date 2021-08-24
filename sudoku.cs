using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace mmt{
    class Program
    {
        public static List<T> Shuffle<T> (List<T> list)
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

        static int[,] box1= new int[3,3]{{0,0,0},{0,0,0},{0,0,0}};
        static int[,] box2= new int[3,3]{{0,0,0},{0,0,0},{0,0,0}};
        static int[,] box3= new int[3,3]{{0,0,0},{0,0,0},{0,0,0}};
        static int[,] box4= new int[3,3]{{0,0,0},{0,0,0},{0,0,0}};
        static int[,] box5= new int[3,3]{{0,0,0},{0,0,0},{0,0,0}};
        static int[,] box6= new int[3,3]{{0,0,0},{0,0,0},{0,0,0}};
        static int[,] box7= new int[3,3]{{0,0,0},{0,0,0},{0,0,0}};
        static int[,] box8= new int[3,3]{{0,0,0},{0,0,0},{0,0,0}};
        static int[,] box9= new int[3,3]{{0,0,0},{0,0,0},{0,0,0}};
        static List<int> x = new List<int>(new int[]{1,2,3});
        static List<int> y = new List<int>(new int[]{1,2,3});
        static List<int> x1=new List<int>();
        static List<int> x2=new List<int>();
        static List<int> x3=new List<int>();
        static List<int> x4=new List<int>();
        static List<int> x5=new List<int>();
        static List<int> x6=new List<int>();
        static List<int> x7=new List<int>();
        static List<int> x8=new List<int>();
        static List<int> x9=new List<int>();
        //static string s;
        static void Main(string[] args){ 
            System.Diagnostics.Stopwatch sw = new Stopwatch();
            sw.Reset();         // 초기화
            sw.Start();         // 
            clear(x,y,7);
            print(box1,box2,box3);
            print(box4,box5,box6);
            print(box7,box8,box9);
            
            sw.Stop();          // 종료
            Console.WriteLine("수행 시간 : {0}", sw.ElapsedMilliseconds / 1000.0F);
            }
        static void print(int[,] x_1,int[,] x_2,int[,] x_3){
          for(int x=0; x<3; x++){
            for(int i=0; i<9; i++){
              if(i<3){
                Console.Write(x_1[x,i]);
                Console.Write(" ");
              }
              else if (2<i&&i<6){
                Console.Write(x_2[x,i-3]);
                Console.Write(" ");
              }
              else if(5<i&&i<9){
                Console.Write(x_3[x,i-6]);
                Console.Write(" ");
              }
              if(7<i&&i<9){
                Console.Write("\n");
              }
            }
            }
        }
        static void clear(List<int> a_1,List<int> a_2,int i)
        {
            int u=1;
            while (true)
            {
                x1.Clear();
                x2.Clear();
                x3.Clear();
                x4.Clear();
                x5.Clear();
                x6.Clear();
                x7.Clear();
                x8.Clear();
                x9.Clear();
                
                Shuffle(a_1);
                x1.Add(a_1[0]);
                x2.Add(a_1[1]);
                x3.Add(a_1[2]);
                Shuffle(a_1);
                x4.Add(a_1[0]);
                x5.Add(a_1[1]);
                x6.Add(a_1[2]);
                Shuffle(a_1);
                x7.Add(a_1[0]);
                x8.Add(a_1[1]);
                x9.Add(a_1[2]);
                Shuffle(a_2);
                x1.Add(a_2[0]);
                x4.Add(a_2[1]);
                x7.Add(a_2[2]);
                Shuffle(a_2);
                x2.Add(a_2[0]);
                x5.Add(a_2[1]);
                x8.Add(a_2[2]);
                Shuffle(a_2);
                x3.Add(a_2[0]);
                x6.Add(a_2[1]);
                x9.Add(a_2[2]);
                if (u>i){
                    break;}
                back:
                    if (box1[x1[0]-1,x1[1]-1]==0){
                        if (box2[x2[0]-1,x2[1]-1]==0){
                            if (box3[x3[0]-1,x3[1]-1]==0){
                                if (box4[x4[0]-1,x4[1]-1]==0){
                                    if (box5[x5[0]-1,x5[1]-1]==0){
                                        if (box6[x6[0]-1,x6[1]-1]==0){
                                            if (box7[x7[0]-1,x7[1]-1]==0){
                                                if (box8[x8[0]-1,x8[1]-1]==0){
                                                    if (box9[x9[0]-1,x9[1]-1]==0){
                                                        box1[x1[0]-1,x1[1]-1]=u;
                                                        box2[x2[0]-1,x2[1]-1]=u;
                                                        box3[x3[0]-1,x3[1]-1]=u;
                                                        box4[x4[0]-1,x4[1]-1]=u;
                                                        box5[x5[0]-1,x5[1]-1]=u;
                                                        box6[x6[0]-1,x6[1]-1]=u;
                                                        box7[x7[0]-1,x7[1]-1]=u;
                                                        box8[x8[0]-1,x8[1]-1]=u;
                                                        box9[x9[0]-1,x9[1]-1]=u;
                                                        u+=1;}
                                                    else{
                                                        reset(9);
                                                        goto back;
                                                }}
                                                else{
                                                    reset(8);
                                                    goto back;
                                                }}
                                            else{
                                                reset(7);
                                                goto back;
                                            }}
                                        else{
                                            reset(6);
                                            goto back;
                                        }}
                                    else{
                                        reset(5);
                                        goto back;
                                    }}
                                else{
                                    reset(4);
                                    goto back;
                                }}
                            else{
                                reset(3);
                                goto back;
                            }}
                        else{
                            reset(2);
                            goto back;
                        }}
                    else{
                        reset(1);
                        goto back;
                    }
                //for(int v=0; v<3; v++){
                //    for(int b=0; b<3; b++){
                //        if(box1[v,b]==0){
                //            box1[v,b]=9;
                //        }
                //        if(box2[v,b]==0){
                //            box2[v,b]=9;
                //        }
                //        if(box3[v,b]==0){
                //            box3[v,b]=9;
                //        }
                //        if(box4[v,b]==0){
                //            box4[v,b]=9;
                //        }
                //        if(box5[v,b]==0){
                //            box5[v,b]=9;
                //        }
                //        if(box6[v,b]==0){
                //            box6[v,b]=9;
                //        }
                //        if(box7[v,b]==0){
                //            box7[v,b]=9;
                //        }
                //        if(box8[v,b]==0){
                //            box8[v,b]=9;
                //        }
                //        if(box9[v,b]==0){
                //            box9[v,b]=9;
                //        }
                //}

            }}
            //Console.WriteLine(x[0]);
        
        static void reset(int iii){
            switch (iii)
            {
                case 1:
                    Shuffle(x);
                    x1[0]=x[0];
                    x2[0]=x[1];
                    x3[0]=x[2];
                    Shuffle(y);
                    x1[1]=y[0];
                    x4[1]=y[1];
                    x7[1]=y[2];
                    break;
                case 2:
                    Shuffle(x);
                    x1[0]=x[0];
                    x2[0]=x[1];
                    x3[0]=x[2];
                    Shuffle(y);
                    x2[1]=y[0];
                    x5[1]=y[1];
                    x8[1]=y[2];
                    break;
                case 3:
                    Shuffle(x);
                    x1[0]=x[0];
                    x2[0]=x[1];
                    x3[0]=x[2];
                    Shuffle(y);
                    x3[1]=y[0];
                    x6[1]=y[1];
                    x9[1]=y[2];
                    break;
                case 4:
                    Shuffle(x);
                    x4[0]=x[0];
                    x5[0]=x[1];
                    x6[0]=x[2];
                    Shuffle(y);
                    x1[1]=y[0];
                    x4[1]=y[1];
                    x7[1]=y[2];
                    break;
                case 5:
                    Shuffle(x);
                    x4[0]=x[0];
                    x5[0]=x[1];
                    x6[0]=x[2];
                    Shuffle(y);
                    x2[1]=y[0];
                    x5[1]=y[1];
                    x8[1]=y[2];
                    break;
                case 6:
                    Shuffle(x);
                    x4[0]=x[0];
                    x5[0]=x[1];
                    x6[0]=x[2];
                    Shuffle(y);
                    x3[1]=y[0];
                    x6[1]=y[1];
                    x9[1]=y[2];
                    break;
                case 7:
                    Shuffle(x);
                    x7[0]=x[0];
                    x8[0]=x[1];
                    x9[0]=x[2];
                    Shuffle(y);
                    x1[1]=y[0];
                    x4[1]=y[1];
                    x7[1]=y[2];
                    break;
                case 8:
                    Shuffle(x);
                    x7[0]=x[0];
                    x8[0]=x[1];
                    x9[0]=x[2];
                    Shuffle(y);
                    x2[1]=y[0];
                    x5[1]=y[1];
                    x8[1]=y[2];
                    break;
                case 9:
                    Shuffle(x);
                    x7[0]=x[0];
                    x8[0]=x[1];
                    x9[0]=x[2];
                    Shuffle(y);
                    x3[1]=y[0];
                    x6[1]=y[1];
                    x9[1]=y[2];
                    break;
                default:
                    break;
            }
        }
    }
    }
