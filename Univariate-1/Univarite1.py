class Univarite1():#Here we just copy and paste the function of quan and qual  and the dataframe function(for creating table).  What ever 
                      #inside in this .py this is called formula. we can use it in simplified form in faircopy.  And this part is very very 
    def init(self):  #important
        pass
    
    def QuanQual(self,dataset):
        Quan=[]
        Qual=[]
        for column in dataset.columns:
            #print(column) ##if we put hastag in print then only we get splittation in faircopy quan and qual.  if we dont put hastag means
            if(dataset[column].dtypes=='object'):                                                     #faircopy it will give all columns
                Qual.append(column)
            else:
                Quan.append(column)
        print("Quan:",Quan)# in faircopy it will show only the quan columns.The quan columns whatever in we did using append that will save                                                                                                                    # in the quan[] 
        print("Qual:",Qual)# in faircopy it will show only the qual columns. The quan columns whatever in we did using append that will save 
        return Quan,Qual                                                                                          # in the qual[] 

    def freqTable(self,columnName,dataset):
        import pandas as pd # without importing this library it shows error in faircopy
        frq=pd.DataFrame()
        frq["Unique_Values"]=dataset[columnName].value_counts().index
        frq["Frequency"]=dataset[columnName].value_counts().values
        frq["Relative_Fre"]=dataset[columnName].value_counts().values/len(dataset[columnName])*100
        frq["Cumulative"]=frq["Relative_Fre"].cumsum()
        return frq