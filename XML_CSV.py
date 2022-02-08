import pandas as pd
import xml.etree.ElementTree as et

class ProjectDetails:
    
    def __init__(self,tags,paths):
        self.tags = tags
        self.paths = paths
        
    def Project(self):
        rows=[]
        cols = []
        temp_dict = {}
        check = 1
        for elem in root.iter(self.tags):
            temp=[]
            temp_dict = elem.attrib
            if check == 1:
                for x in temp_dict.keys():
                    cols.append(x)
                check = check + 1
            c = len(cols) 
            for x in range(c):
                temp.append(elem.attrib[cols[x]])
            
        rows.append(temp)
        
        df = pd.DataFrame(rows,columns=cols)
        df.to_csv(path+self.paths,index = False)
    
class Parts:
    
    def __init__(self,tags,paths):
        self.x = tags
        self.y = paths
    
    def Part(self):
        rows = []
        cols = []
        col = ['UserAtrributes (Name,Value)','GainDirection(X,Y,Z,Align)','Reference Side(Side,Align)']
        temp_dict={}
        check = 1
        counter = 1
        
        for elem in root.iter(self.x):   
            temp=[]
            temp_dict = elem.attrib
            if check == 1:
                for x in temp_dict.keys():
                    cols.append(x)
                check = check + 1
            c = len(cols) 
            for x in range(c):
                temp.append(elem.attrib[cols[x]])
                
            root1 = et.Element
            root1 = elem
            
            temp_gainDir = []
            temp_gainDirection = []
            temp_refSide = []
            temp_refSides = []
            
            for userAttributes in root1.iter('{http://www.design2machine.com}UserAttributes'):
                root2 = et.Element
                root2 = userAttributes
                temp_userAttribute = []
                temp_userAttributes = []

                for userAttribute in root2.iter('{http://www.design2machine.com}UserAttribute'):
                    temp_userAttribute.append(userAttribute.attrib['Name'])
                    temp_userAttribute.append(userAttribute.attrib['Value'])
                    string = ' , '.join(temp_userAttribute)
                    temp_userAttributes.append('('+string+')')
                    
            for gainDir in root1.iter('{http://www.design2machine.com}GrainDirection'):
                    temp_gainDir.append(gainDir.attrib['X'])
                    temp_gainDir.append(gainDir.attrib['Y'])
                    temp_gainDir.append(gainDir.attrib['Z'])
                    temp_gainDir.append(gainDir.attrib['Align'])
                    string = ' , '.join(temp_gainDir)
                    temp_gainDirection.append('('+string+')')
            
            for Referenceside in root1.iter('{http://www.design2machine.com}ReferenceSide'):
                    temp_refSide.append(Referenceside.attrib['Side'])
                    temp_refSide.append(Referenceside.attrib['Align'])
                    string = ' , '.join(temp_refSide)
                    temp_refSides.append('('+string+')')
                    
            stringUserAttributes = ' , '.join(temp_userAttributes)
            stringGainDir = ' , '.join(temp_gainDirection)
            stringRefSide = ' , '.join(temp_refSides)
            
            temp.append(stringUserAttributes)
            temp.append(stringGainDir)   
            temp.append(stringRefSide) 
            counter = counter + 1
            rows.append(temp)
            
        cols = cols + col
        
        df = pd.DataFrame(rows,columns= cols)
        df.to_csv(path+self.y,index= False)
    
class Transformations:  
    
    def __init__(self,tags,paths):
        self.tags = tags
        self.paths = paths
        
    def transformation(self):
        rows = []
        col = ['GUID','RefrencePoint (X,Y,Z)','XVector (X,Y,Z)','YVector (X,Y,Z)'] 
        for elem in root.iter(self.tags):  
            root1 = et.Element
            root1 = elem
            temp=[]
            tempGUID=[]
            tempRefrencePoint = []
            tempXVector=[]
            tempYVector=[]
            for innerElem in root1.iter('{http://www.design2machine.com}Transformation'):
                tempGUID.append(innerElem.attrib['GUID'])
                root2 = et.Element
                root2 = innerElem
                for innerInner in root2.iter('{http://www.design2machine.com}Position'):
                    root3 = et.Element
                    root3 = innerInner
                    temp_referencepoint=[]
                    temp_xvector=[]
                    temp_yvector=[]
                    for position in root3.iter('{http://www.design2machine.com}ReferencePoint'):
                        
                        temp_referencepoint.append(position.attrib['X'])
                        temp_referencepoint.append(position.attrib['Y'])
                        temp_referencepoint.append(position.attrib['Z'])
                        string = ' , '.join(temp_referencepoint)
                        tempRefrencePoint.append('('+string+')')
                        
                    for position in root3.iter('{http://www.design2machine.com}XVector'):
                        temp_xvector.append(position.attrib['X'])
                        temp_xvector.append(position.attrib['Y'])
                        temp_xvector.append(position.attrib['Z'])
                        string = ' , '.join(temp_xvector)
                        tempXVector.append('('+string+')')
                        
                    for position in root3.iter('{http://www.design2machine.com}YVector'):
                        temp_yvector.append(position.attrib['X'])
                        temp_yvector.append(position.attrib['Y'])
                        temp_yvector.append(position.attrib['Z'])
                        string = ' , '.join(temp_yvector)
                        tempYVector.append('('+string+')')
            stringG = ' , '.join(tempGUID)
            stringR = ' , '.join(tempRefrencePoint)
            stringX = ' , '.join(tempXVector)
            stringY = ' , '.join(tempYVector)
            temp.append(stringG)
            temp.append(stringR)
            temp.append(stringX)
            temp.append(stringY)
            rows.append(temp)    
            
        df = pd.DataFrame(rows,columns= col)
        df.to_csv(path+self.paths,index= False)

class Processings:
    
    def __init__(self,tags,paths):
        self.tags = tags
        self.paths = paths
            
    def Processing(self):
        rows=[]
        cols =['FreeCountour(CounterSink , ToolID , ToolPosition , ReferencePlaneID , Name)','CountourStartPoint(X,Y,Z)','ContourLineInclination','ContourLineEndpoint(X,Y,Z)']

        for elem in root.iter(self.tags):
            root1 = et.Element
            root1 = elem
            temp=[]
            
            for processing in root1.iter('{http://www.design2machine.com}Processings'):
                root2 = et.Element
                root2 = processing
                
                temp_FreeContourAll = []
                temp_startPointAll = []
                temp_LineInclination = []
                temp_EndPointS = []
                for freecontour in root2.iter('{http://www.design2machine.com}FreeContour'):
                    temp_FreeContour = []
                    temp_FreeContour.append(freecontour.attrib['CounterSink'])
                    temp_FreeContour.append(freecontour.attrib['ToolID'])
                    temp_FreeContour.append(freecontour.attrib['ToolPosition'])
                    temp_FreeContour.append(freecontour.attrib['ReferencePlaneID']) 
                    temp_FreeContour.append(freecontour.attrib['Name'])
                    string = ','.join(temp_FreeContour)
                    temp_FreeContourAll.append('('+string+')')
                    
                    root3 = et.Element
                    root3 = freecontour
    
                    for contour in root3.iter('{http://www.design2machine.com}Contour'):
                        root4 = et.Element
                        root4 = contour
                        for startPoint in root4.iter('{http://www.design2machine.com}StartPoint'):
                            temp_startPoint = []
                            temp_startPoint.append(startPoint.attrib['X'])
                            temp_startPoint.append(startPoint.attrib['Y'])
                            temp_startPoint.append(startPoint.attrib['Z'])
                            string =','.join(temp_startPoint)
                            temp_startPointAll.append('('+string+')')
                            
                            temp_Line = []
                            temp_Endpoints = []
                            
                        for Line in root4.iter('{http://www.design2machine.com}Line'):
                            temp_Line.append(Line.attrib['Inclination'])
                    
                        
                            root5 = et.Element
                            root5 = Line
                            
                            temp_Endpoint = []
                            
                            for EndPoint in root5.iter('{http://www.design2machine.com}EndPoint'):
                                temp_Endpoint.append(EndPoint.attrib['X'])
                                temp_Endpoint.append(EndPoint.attrib['Y'])
                                temp_Endpoint.append(EndPoint.attrib['Y'])
                                string = ','.join(temp_Endpoint)
                                temp_Endpoints.append('('+string+')')
                                
                        string =','.join(temp_Endpoints)
                        temp_EndPointS.append('{'+string+'}')
        
                        string =','.join(temp_Line)
                        temp_LineInclination.append('('+string+')')
                        
                stringFreeContour = ' , '.join(temp_FreeContourAll)
                stringStartPoint = ' , '.join(temp_startPointAll)
                stringLineInclination = ' , '.join(temp_LineInclination)
                stringEndpoints = ' , '.join(temp_EndPointS)
                temp.append(stringFreeContour)   
                temp.append(stringStartPoint)   
                temp.append(stringLineInclination)
                temp.append(stringEndpoints)
                rows.append(temp)      

        df = pd.DataFrame(rows,columns= cols)
        df.to_csv(path+self.paths,index= False)        


XmlFile = input(r'''Enter File Directory(Eg: C:\Users\Karan\Desktop\New folder\00002.BTLX) :  ''') #Example input as complete Directory of XmlFIle C:\Users\Karan\Desktop\New folder\00002.BTLX
tree = et.parse(XmlFile)
root = tree.getroot()
newFile = XmlFile.split('\\')
CsvFile = newFile[-1].split('.')
del newFile[-1]
path = '\\'.join(newFile) + '\\' #Path where converted files are saved


ProjectDetail = ProjectDetails(r'{http://www.design2machine.com}Project',('ProjectDetails'+'_'+('_').join(CsvFile)+'.csv'))  
Parts = Parts(r'{http://www.design2machine.com}Part',('Parts'+'_'+('_').join(CsvFile)+'.csv'))   
Transformations = Transformations(r'{http://www.design2machine.com}Transformations',('Transformations'+'_'+('_').join(CsvFile)+'.csv'))  
Processign = Processings(r'{http://www.design2machine.com}Part',('Processings'+'_'+('_').join(CsvFile)+'.csv'))  

ProjectDetail.Project()
Parts.Part()
Transformations.transformation()  
Processign.Processing()



